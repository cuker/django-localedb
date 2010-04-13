# -*- coding: utf-8 -*-
"""
This code is heavily borrowed from Python locale.py and modified to be thread safe.
"""
# from decimal import Decimal
import re, operator

from django.conf import settings
from django.contrib.sites.models import Site
from django.db import models
from django.utils.translation import ugettext_lazy as _

class LocaleManager(models.Manager):
    def get_site_locale(self):
        return Locale.objects.get(localesitedefault__site__pk=settings.SITE_ID)

class Locale(models.Model):
    name = models.CharField(_('name'), max_length=10, unique=True)

    #below are fields for numarical representations
    mon_decimal_point = models.CharField(_('monetary decimal point'), max_length=2, blank=True, help_text=_("Decimal point used for monetary values."))
    mon_thousands_sep = models.CharField(_('monetary thousands seperator'), max_length=2, blank=True, help_text=_("Group separator used for monetary values."))
    mon_grouping = models.CommaSeparatedIntegerField(_('monetary grouping'), max_length=256, blank=True, default='127', help_text=_("Equivalent to 'grouping', used for monetary values."))

    currency_symbol = models.CharField(_('currency symbol'), max_length=4, blank=True, help_text=_("Local currency symbol."))
    frac_digits = models.PositiveIntegerField(_('fractional digits'), help_text=_("Number of fractional digits used in formatting of monetary values."))
    int_curr_symbol = models.CharField(_('international currency symbal'), max_length=4, blank=True, help_text=_("International currency symbol."))
    int_frac_digits = models.PositiveIntegerField(_('international fractional digits'), help_text=_("Number of fractional digits used in international formatting of monetary values."))

    p_sep_by_space = models.BooleanField(_('positive seperate by space'), help_text=_("Whether the currency symbol is separated from the value by a space for positive values."))
    n_sep_by_space = models.BooleanField(_('negative seperate by space'), help_text=_("Whether the currency symbol is separated from the value by a space for negative values."))

    thousands_sep = models.CharField(_('thousands seperator'), max_length=2, blank=True, help_text=_("Character used between groups."))
    p_sign_posn = models.PositiveSmallIntegerField(help_text=_("The position of the sign positive values."))
    n_sign_posn = models.PositiveSmallIntegerField(help_text=_("The position of the sign negative values."))
    decimal_point = models.CharField(_('decimal point'), max_length=2, help_text=_("Decimal point character."))

    p_cs_precedes = models.BooleanField(help_text=_("Whether the currency symbol precedes the value for positive values."))
    n_cs_precedes = models.BooleanField(help_text=_("Whether the currency symbol precedes the value for negative values."))

    positive_sign = models.CharField(_('positive sign'), max_length=2, blank=True, help_text=_("Symbol used to annotate a positive monetary value."))
    negative_sign = models.CharField(_('negative sign'), max_length=2, blank=True, help_text=_("Symbol used to annotate a negative monetary value."))

    grouping = models.CommaSeparatedIntegerField(_('grouping'), max_length=256, blank=True, default='127',
                                help_text=_("""Sequence of numbers specifying which relative positions the 'thousands_sep' is expected.
                                If the sequence is terminated with CHAR_MAX, no further grouping is performed.
                                If the sequence terminates with a 0, the last group size is repeatedly used."""))

    #below are other fields, namely date and time related info
    codeset = models.CharField(_('codeset'), max_length=15, help_text=_("The name of the character encoding used in the selected locale.")) #this sould be equal to the encoding of the database, or a subset
    d_t_fmt = models.CharField(_('date time format'), max_length=30, help_text=_("The string that can be used as a format string for strftime() to represent time and date in a locale-specific way."))
    d_fmt = models.CharField(_('date format'), max_length=20, help_text=_("The string that can be used as a format string for strftime() to represent a date in a locale-specific way."))
    t_fmt = models.CharField(_('time format'), max_length=20, help_text=_("The string that can be used as a format string for strftime() to represent a time in a locale-specific way."))
    t_fmt_ampm = models.CharField(_('time format 12 hour'), max_length=25, help_text=_("The format string for strftime() to represent time in the am/pm format."))

    day_1 = models.CharField(_('day 1'), max_length=20, help_text=_("The name of the n-th day of the week."))
    day_2 = models.CharField(_('day 2'), max_length=20, help_text=_("The name of the n-th day of the week."))
    day_3 = models.CharField(_('day 3'), max_length=20, help_text=_("The name of the n-th day of the week."))
    day_4 = models.CharField(_('day 4'), max_length=20, help_text=_("The name of the n-th day of the week."))
    day_5 = models.CharField(_('day 5'), max_length=20, help_text=_("The name of the n-th day of the week."))
    day_6 = models.CharField(_('day 6'), max_length=20, help_text=_("The name of the n-th day of the week."))
    day_7 = models.CharField(_('day 7'), max_length=20, help_text=_("The name of the n-th day of the week."))

    abday_1 = models.CharField(_('abbreviated day 1'), max_length=20, help_text=_("The abbreviated name of the n-th day of the week."))
    abday_2 = models.CharField(_('abbreviated day 2'), max_length=20, help_text=_("The abbreviated name of the n-th day of the week."))
    abday_3 = models.CharField(_('abbreviated day 3'), max_length=20, help_text=_("The abbreviated name of the n-th day of the week."))
    abday_4 = models.CharField(_('abbreviated day 4'), max_length=20, help_text=_("The abbreviated name of the n-th day of the week."))
    abday_5 = models.CharField(_('abbreviated day 5'), max_length=20, help_text=_("The abbreviated name of the n-th day of the week."))
    abday_6 = models.CharField(_('abbreviated day 6'), max_length=20, help_text=_("The abbreviated name of the n-th day of the week."))
    abday_7 = models.CharField(_('abbreviated day 7'), max_length=20, help_text=_("The abbreviated name of the n-th day of the week."))

    mon_1 = models.CharField(_('month 1'), max_length=20, help_text=_("The name of the n-th month."))
    mon_2 = models.CharField(_('month 2'), max_length=20, help_text=_("The name of the n-th month."))
    mon_3 = models.CharField(_('month 3'), max_length=20, help_text=_("The name of the n-th month."))
    mon_4 = models.CharField(_('month 4'), max_length=20, help_text=_("The name of the n-th month."))
    mon_5 = models.CharField(_('month 5'), max_length=20, help_text=_("The name of the n-th month."))
    mon_6 = models.CharField(_('month 6'), max_length=20, help_text=_("The name of the n-th month."))
    mon_7 = models.CharField(_('month 7'), max_length=20, help_text=_("The name of the n-th month."))
    mon_8 = models.CharField(_('month 8'), max_length=20, help_text=_("The name of the n-th month."))
    mon_9 = models.CharField(_('month 9'), max_length=20, help_text=_("The name of the n-th month."))
    mon_10 = models.CharField(_('month 10'), max_length=20, help_text=_("The name of the n-th month."))
    mon_11 = models.CharField(_('month 11'), max_length=20, help_text=_("The name of the n-th month."))
    mon_12 = models.CharField(_('month 12'), max_length=20, help_text=_("The name of the n-th month."))

    abmon_1 = models.CharField(_('abbreviated month 1'), max_length=20, help_text=_("The abbreviated name of the n-th month."))
    abmon_2 = models.CharField(_('abbreviated month 2'), max_length=20, help_text=_("The abbreviated name of the n-th month."))
    abmon_3 = models.CharField(_('abbreviated month 3'), max_length=20, help_text=_("The abbreviated name of the n-th month."))
    abmon_4 = models.CharField(_('abbreviated month 4'), max_length=20, help_text=_("The abbreviated name of the n-th month."))
    abmon_5 = models.CharField(_('abbreviated month 5'), max_length=20, help_text=_("The abbreviated name of the n-th month."))
    abmon_6 = models.CharField(_('abbreviated month 6'), max_length=20, help_text=_("The abbreviated name of the n-th month."))
    abmon_7 = models.CharField(_('abbreviated month 7'), max_length=20, help_text=_("The abbreviated name of the n-th month."))
    abmon_8 = models.CharField(_('abbreviated month 8'), max_length=20, help_text=_("The abbreviated name of the n-th month."))
    abmon_9 = models.CharField(_('abbreviated month 9'), max_length=20, help_text=_("The abbreviated name of the n-th month."))
    abmon_10 = models.CharField(_('abbreviated month 10'), max_length=20, help_text=_("The abbreviated name of the n-th month."))
    abmon_11 = models.CharField(_('abbreviated month 11'), max_length=20, help_text=_("The abbreviated name of the n-th month."))
    abmon_12 = models.CharField(_('abbreviated month 12'), max_length=20, help_text=_("The abbreviated name of the n-th month."))

    yesexpr = models.CharField(_('yes expresion'), max_length=20, help_text=_("A regular expression that can be used with the regex function to recognize a positive response to a yes/no question."))
    noexpr = models.CharField(_('no expresion'), max_length=20, help_text=_("A regular expression that can be used with the regex(3) function to recognize a negative response to a yes/no question."))

    era = models.CharField(_('era'), max_length=10, blank=True, help_text=_("A string that represents the era used in the current locale."))
    era_year = models.CharField(_('era year'), max_length=10, blank=True, help_text=_("The year in the relevant era of the locale."))
    era_d_t_fmt = models.CharField(_('era date time format'), max_length=25, blank=True, help_text=_("The format string for strftime() to represent dates and times in a locale-specific era-based way."))
    era_d_fmt = models.CharField(_('era date format'), max_length=20, blank=True, help_text=_("The format string for strftime() to represent time in a locale-specific era-based way"))
    alt_digits = models.TextField(_('alternate digits'), blank=True, help_text=_("A representation of up to 100 values used to represent the values 0 to 99."))

    objects = LocaleManager()

    # C module constants
    CHAR_MAX = 127
    LC_ALL = 6
    LC_COLLATE = 3
    LC_CTYPE = 0
    LC_MESSAGES = 5
    LC_MONETARY = 4
    LC_NUMERIC = 1
    LC_TIME = 2

    def __unicode__(self):
        return self.name

    def _comma_int_list(self, data):
        return [int(i) for i in data.split(',')]

    # Iterate over grouping intervals
    def _grouping_intervals(self, grouping):
        for interval in grouping:
            # if grouping is -1, we are done
            if interval == self.CHAR_MAX:
                return
            # 0: re-use last group ad infinitum
            if interval == 0:
                while True:
                    yield self.last_interval
            yield interval
            self.last_interval = interval

    #perform the grouping from right to left
    def _group(self, s, monetary=False):
        thousands_sep = self.mon_thousands_sep if monetary else self.thousands_sep
        # thousands_sep = conv[monetary and 'mon_thousands_sep' or 'thousands_sep']
        grouping = self._comma_int_list(self.mon_grouping) if monetary else self._comma_int_list(self.grouping)
        # grouping = conv[monetary and 'mon_grouping' or 'grouping']
        if not grouping:
            return (s, 0)
        # result = ""
        # seps = 0
        if s[-1] == ' ':
            stripped = s.rstrip()
            right_spaces = s[len(stripped):]
            s = stripped
        else:
            right_spaces = ''
        left_spaces = ''
        groups = []
        for interval in self._grouping_intervals(grouping):
            if not s or s[-1] not in "0123456789":
                # only non-digit characters remain (sign, spaces)
                left_spaces = s
                s = ''
                break
            groups.append(s[-interval:])
            s = s[:-interval]
        if s:
            groups.append(s)
        groups.reverse()
        return (
            left_spaces + thousands_sep.join(groups) + right_spaces,
            len(thousands_sep) * (len(groups) - 1)
        )

    # Strip a given amount of excess padding from the given string
    def _strip_padding(self, s, amount):
        lpos = 0
        while amount and s[lpos] == ' ':
            lpos += 1
            amount -= 1
        rpos = len(s) - 1
        while amount and s[rpos] == ' ':
            rpos -= 1
            amount -= 1
        return s[lpos:rpos+1]

    # CONSIDER: This seems to have been replaced by class variables
    def localconv(self):
        raise NotImplementedError

    # CONSIDER: This doesn't seem relavant since our module is thread safe
    def strcoll(self, a,b):
        """ strcoll(string,string) -> int.
            Compares two strings according to the locale.
        """
        return cmp(a,b)

    # CONSIDER: This doesn't seem relavant since our module is thread safe
    def strxfrm(self, s):
        """ strxfrm(string) -> string.
            Returns a string that behaves for cmp locale-aware.
        """
        return s

    def format(self, percent, value, grouping=False, monetary=False, *additional):
        """Returns the locale-aware substitution of a %? specifier
        (percent).

        additional is for format strings which contain one or more
        '*' modifiers."""
        # this is only for one-percent-specifier strings and this should be checked
        if percent[0] != '%':
            raise ValueError("format() must be given exactly one %char "
                             "format specifier")
        if additional:
            formatted = percent % ((value,) + additional)
        else:
            formatted = percent % value
        # floats and decimal ints need special action!
        if percent[-1] in 'eEfFgG':
            seps = 0
            parts = formatted.split('.')
            if grouping:
                parts[0], seps = self._group(parts[0], monetary=monetary)
            decimal_point = self.mon_decimal_point if monetary else self.decimal_point
            # decimal_point = localeconv()[monetary and 'mon_decimal_point' or 'decimal_point']
            formatted = decimal_point.join(parts)
            if seps:
                formatted = self._strip_padding(formatted, seps)
        elif percent[-1] in 'diu':
            seps = 0
            if grouping:
                formatted, seps = self._group(formatted, monetary=monetary)
            if seps:
                formatted = self._strip_padding(formatted, seps)
        return formatted

    _percent_re = re.compile(r'%(?:\((?P<key>.*?)\))?'
                             r'(?P<modifiers>[-#0-9 +*.hlL]*?)[eEfFgGdiouxXcrs%]')

    def format_string(self, f, val, grouping=False):
        """Formats a string in the same way that the % formatting would use,
        but takes the current locale into account.
        Grouping is applied if the third parameter is true."""
        percents = list(self._percent_re.finditer(f))
        new_f = self._percent_re.sub('%s', f)

        if isinstance(val, tuple):
            new_val = list(val)
            i = 0
            for perc in percents:
                starcount = perc.group('modifiers').count('*')
                new_val[i] = self.format(perc.group(), new_val[i], grouping, False, *new_val[i+1:i+1+starcount])
                del new_val[i+1:i+1+starcount]
                i += (1 + starcount)
            val = tuple(new_val)
        elif operator.isMappingType(val):
            for perc in percents:
                key = perc.group("key")
                val[key] = self.format(perc.group(), val[key], grouping)
        else:
            # val is a single value
            val = self.format(percents[0].group(), val, grouping)

        return new_f % val

    def currency(self, val, symbol=True, grouping=False, international=False):
        """Formats val according to the currency settings
        in the current locale."""

        # check for illegal values
        digits = self.int_frac_digits if international else self.frac_digits
        # digits = conv[international and 'int_frac_digits' or 'frac_digits']
        if digits == 127:
            raise ValueError("Currency formatting is not possible using "
                             "the 'C' locale.")

        if val == None:  val = 0
        s = self.format('%%.%if' % digits, abs(val), grouping, monetary=True)
        # '<' and '>' are markers if the sign must be inserted between symbol and value
        s = '<' + s + '>'

        if symbol:
            smb = self.int_curr_symbol if international else self.currency_symbol
            # smb = conv[international and 'int_curr_symbol' or 'currency_symbol']
            precedes = self.n_cs_precedes if val<0 else self.p_cs_precedes
            # precedes = conv[val<0 and 'n_cs_precedes' or 'p_cs_precedes']
            separated = self.n_sep_by_space if val<0 else self.p_sep_by_space
            # separated = conv[val<0 and 'n_sep_by_space' or 'p_sep_by_space']

            if precedes:
                s = smb + (separated and ' ' or '') + s
            else:
                s = s + (separated and ' ' or '') + smb

        sign_pos = self.n_sign_posn if val<0 else self.p_sign_posn
        # sign_pos = conv[val<0 and 'n_sign_posn' or 'p_sign_posn']
        sign = self.negative_sign if val<0 else self.positive_sign
        # sign = conv[val<0 and 'negative_sign' or 'positive_sign']

        if sign_pos == 0:
            s = '(' + s + ')'
        elif sign_pos == 1:
            s = sign + s
        elif sign_pos == 2:
            s = s + sign
        elif sign_pos == 3:
            s = s.replace('<', sign)
        elif sign_pos == 4:
            s = s.replace('>', sign)
        else:
            # the default if nothing specified;
            # this should be the most fitting sign position
            s = sign + s

        return s.replace('<', '').replace('>', '')

    def str(self, val):
        """Convert float to integer, taking the locale into account."""
        return self.format("%.12g", val)

    def atof(self, string, func=float):
        "Parses a string as a float according to the locale settings."
        #First, get rid of the grouping
        ts = self.thousands_sep
        if ts:
            string = string.replace(ts, '')
        #next, replace the decimal point with a dot
        dd = self.decimal_point
        if dd:
            string = string.replace(dd, '.')
        #finally, parse the string
        return func(string)

    def atoi(self, str):
        "Converts a string to an integer according to the locale settings."
        return self.atof(str, int)

    def locale_name(self):
        return str('%s.%s' % (self.name, self.codeset))

    def country_code(self):
        if '_' in self.name:
            return self.name.split('_')[-1]
        return None

    def language_code(self):
        if '_' in self.name:
            return self.name.split('_')[0]
        return None

class LocaleSiteDefault(models.Model):
    site = models.OneToOneField(Site)
    locale = models.ForeignKey(Locale)

    def __unicode__(self):
        return u'%s (%s)' % (self.site, self.locale)

def get_locale(val=None):
    if hasattr(val, 'locale_name'):
        return Locale.objects.get(name=val.locale_name)
    else:
        return Locale.objects.get_site_locale()
