import os
import locale
from pprint import pprint

from django.core.management.base import BaseCommand

from simplecart.currencies.models import Locale

LANGINFO_PROPERTIES = [
    'codeset',
    'd_t_fmt',
    'd_fmt',
    't_fmt',
    't_fmt_ampm',

    'day_1',
    'day_2',
    'day_3',
    'day_4',
    'day_5',
    'day_6',
    'day_7',
    'abday_1',
    'abday_2',
    'abday_3',
    'abday_4',
    'abday_5',
    'abday_6',
    'abday_7',

    'mon_1',
    'mon_2',
    'mon_3',
    'mon_4',
    'mon_5',
    'mon_6',
    'mon_7',
    'mon_8',
    'mon_9',
    'mon_10',
    'mon_11',
    'mon_12',
    'abmon_1',
    'abmon_2',
    'abmon_3',
    'abmon_4',
    'abmon_5',
    'abmon_6',
    'abmon_7',
    'abmon_8',
    'abmon_9',
    'abmon_10',
    'abmon_11',
    'abmon_12',
    'radixchar',
    'thousep',
    'yesexpr',
    'noexpr',
    'crncystr',
    'era',
    'era_year',
    'era_d_t_fmt',
    'era_d_fmt',
    'alt_digits',
]

def encode(val, encoding):
    if not isinstance(val, (str, unicode)):
        return val
    if isinstance(val, str):
        val = unicode(val, encoding)
    else:
        val = unicode(val)
    return unicode(val.encode('utf8', 'ignore'), 'utf8')

class Command(BaseCommand):
    help="""Scrapes the locale info from the current system (*nix only!)
    """

    def execute(self, *args,**options):
        for line in os.popen('locale -a').read().split('\n'):
            add_name = False
            line = line.strip()
            if not line or '.' not in line:
                continue
            name, encoding = line.split('.')
            try:
                unicode(name, encoding)
            except LookupError:
                #not an encoding that is recognized
                continue
            locale.setlocale(locale.LC_ALL, line)
            info = locale.localeconv()
            try:
                unicode(info['currency_symbol'], encoding)
            except (UnicodeDecodeError, LookupError):
                continue
            print line
            pprint(info)
            try:
                new_locale = Locale.objects.get(name=name)
            except Locale.DoesNotExist:
                new_locale = Locale(name=name)
            for key, value in info.items():
                if isinstance(value, list):
                    value = u','.join([unicode(val) for val in value])
                else:
                    value = encode(value, encoding)
                setattr(new_locale, key, value)
            langinfo_data = dict()
            for key in LANGINFO_PROPERTIES:
                lang_key = key.upper()
                if hasattr(locale, lang_key):
                    lang_key = getattr(locale, lang_key)
                    value = locale.nl_langinfo(lang_key)
                    try:
                        value = encode(value, encoding)
                    except UnicodeDecodeError:
                        print 'Error encoding:', key
                        continue
                    langinfo_data[key] = value
                    setattr(new_locale, key, value)
                else:
                    print "lang_key not found:", lang_key
            
            pprint(langinfo_data)
            new_locale.save()


