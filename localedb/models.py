# -*- coding: utf-8 -*-
from decimal import Decimal

from django.db import models
from django.conf import settings
from django.contrib.sites.models import Site

class LocaleManager(models.Manager):
    def get_site_locale(self):
        return Locale.objects.get(localesitedefault__site__pk=settings.SITE_ID)

class Locale(models.Model):
    name = models.CharField(max_length=10, unique=True)
    
    #below are fields for numarical representations
    mon_decimal_point = models.CharField(max_length=2, blank=True, help_text='Decimal point used for monetary values.')
    mon_thousands_sep = models.CharField(max_length=2, blank=True, help_text='Group separator used for monetary values.')
    mon_grouping = models.CharField(max_length=256, blank=True, help_text="Equivalent to 'grouping', used for monetary values.")
    
    currency_symbol = models.CharField(max_length=4, blank=True, help_text='Local currency symbol.')
    int_curr_symbol = models.CharField(max_length=4, blank=True, help_text='International currency symbol.')
    int_frac_digits = models.PositiveIntegerField(help_text='Number of fractional digits used in international formatting of monetary values.')
    
    p_sep_by_space = models.BooleanField(help_text='Whether the currency symbol is separated from the value by a space for positive values.')
    n_sep_by_space = models.BooleanField(help_text='Whether the currency symbol is separated from the value by a space for negative values.')
    
    thousands_sep = models.CharField(max_length=2, blank=True, help_text='Character used between groups.')
    p_sign_posn = models.PositiveSmallIntegerField(help_text='The position of the sign positive values.')
    n_sign_posn = models.PositiveSmallIntegerField(help_text='The position of the sign negative values.')
    decimal_point = models.CharField(max_length=2, help_text='Decimal point character.')
    
    p_cs_precedes = models.BooleanField(help_text='Whether the currency symbol precedes the value for positive values.')
    n_cs_precedes = models.BooleanField(help_text='Whether the currency symbol precedes the value for negative values.')
    
    positive_sign = models.CharField(max_length=2, blank=True, help_text="Symbol used to annotate a positive monetary value.")
    negative_sign = models.CharField(max_length=2, blank=True, help_text='Symbol used to annotate a negative monetary value.')
    
    grouping = models.CharField(max_length=256, blank=True,
                                help_text='''Sequence of numbers specifying which relative positions the 'thousands_sep' is expected.
                                If the sequence is terminated with CHAR_MAX, no further grouping is performed.
                                If the sequence terminates with a 0, the last group size is repeatedly used.''')

    #below are other fields, namely date and time related info
    codeset = models.CharField(max_length=10, help_text='The name of the character encoding used in the selected locale.') #this sould be equal to the encoding of the database, or a subset
    d_t_fmt = models.CharField(max_length=25, help_text='The string that can be used as a format string for strftime() to represent time and date in a locale-specific way.')
    d_fmt = models.CharField(max_length=20, help_text='The string that can be used as a format string for strftime() to represent a date in a locale-specific way.')
    t_fmt = models.CharField(max_length=20, help_text='The string that can be used as a format string for strftime() to represent a time in a locale-specific way.')
    t_fmt_ampm = models.CharField(max_length=25, help_text='The format string for strftime() to represent time in the am/pm format.')

    day_1 = models.CharField(max_length=20, help_text='The name of the n-th day of the week.')
    day_2 = models.CharField(max_length=20, help_text='The name of the n-th day of the week.')
    day_3 = models.CharField(max_length=20, help_text='The name of the n-th day of the week.')
    day_4 = models.CharField(max_length=20, help_text='The name of the n-th day of the week.')
    day_5 = models.CharField(max_length=20, help_text='The name of the n-th day of the week.')
    day_6 = models.CharField(max_length=20, help_text='The name of the n-th day of the week.')
    day_7 = models.CharField(max_length=20, help_text='The name of the n-th day of the week.')

    abday_1 = models.CharField(max_length=20, help_text='The abbreviated name of the n-th day of the week.')
    abday_2 = models.CharField(max_length=20, help_text='The abbreviated name of the n-th day of the week.')
    abday_3 = models.CharField(max_length=20, help_text='The abbreviated name of the n-th day of the week.')
    abday_4 = models.CharField(max_length=20, help_text='The abbreviated name of the n-th day of the week.')
    abday_5 = models.CharField(max_length=20, help_text='The abbreviated name of the n-th day of the week.')
    abday_6 = models.CharField(max_length=20, help_text='The abbreviated name of the n-th day of the week.')
    abday_7 = models.CharField(max_length=20, help_text='The abbreviated name of the n-th day of the week.')

    mon_1 = models.CharField(max_length=20, help_text='The name of the n-th month.')
    mon_2 = models.CharField(max_length=20, help_text='The name of the n-th month.')
    mon_3 = models.CharField(max_length=20, help_text='The name of the n-th month.')
    mon_4 = models.CharField(max_length=20, help_text='The name of the n-th month.')
    mon_5 = models.CharField(max_length=20, help_text='The name of the n-th month.')
    mon_6 = models.CharField(max_length=20, help_text='The name of the n-th month.')
    mon_7 = models.CharField(max_length=20, help_text='The name of the n-th month.')
    mon_8 = models.CharField(max_length=20, help_text='The name of the n-th month.')
    mon_9 = models.CharField(max_length=20, help_text='The name of the n-th month.')
    mon_10 = models.CharField(max_length=20, help_text='The name of the n-th month.')
    mon_11 = models.CharField(max_length=20, help_text='The name of the n-th month.')
    mon_12 = models.CharField(max_length=20, help_text='The name of the n-th month.')

    abmon_1 = models.CharField(max_length=20, help_text='The abbreviated name of the n-th month.')
    abmon_2 = models.CharField(max_length=20, help_text='The abbreviated name of the n-th month.')
    abmon_3 = models.CharField(max_length=20, help_text='The abbreviated name of the n-th month.')
    abmon_4 = models.CharField(max_length=20, help_text='The abbreviated name of the n-th month.')
    abmon_5 = models.CharField(max_length=20, help_text='The abbreviated name of the n-th month.')
    abmon_6 = models.CharField(max_length=20, help_text='The abbreviated name of the n-th month.')
    abmon_7 = models.CharField(max_length=20, help_text='The abbreviated name of the n-th month.')
    abmon_8 = models.CharField(max_length=20, help_text='The abbreviated name of the n-th month.')
    abmon_9 = models.CharField(max_length=20, help_text='The abbreviated name of the n-th month.')
    abmon_10 = models.CharField(max_length=20, help_text='The abbreviated name of the n-th month.')
    abmon_11 = models.CharField(max_length=20, help_text='The abbreviated name of the n-th month.')
    abmon_12 = models.CharField(max_length=20, help_text='The abbreviated name of the n-th month.')

    #radixchar = decimal_point
    #thousep = thousands_sep

    yesexpr = models.CharField(max_length=10, help_text='A regular expression that can be used with the regex function to recognize a positive response to a yes/no question.')
    noexpr = models.CharField(max_length=10, help_text='A regular expression that can be used with the regex(3) function to recognize a negative response to a yes/no question.')

    #crncystr ?    

    era = models.CharField(max_length=10, blank=True, help_text='A string that represents the era used in the current locale.')
    era_year = models.CharField(max_length=10, blank=True, help_text='The year in the relevant era of the locale.')
    era_d_t_fmt = models.CharField(max_length=25, blank=True, help_text='The format string for strftime() to represent dates and times in a locale-specific era-based way.')
    era_d_fmt = models.CharField(max_length=20, blank=True, help_text='The format string for strftime() to represent time in a locale-specific era-based way')
    alt_digits = models.TextField(blank=True, help_text='A representation of up to 100 values used to represent the values 0 to 99.')

    objects = LocaleManager()
    
    def __unicode__(self):
        return self.name
    
    def mon_grouping_list(self):
        return [int(i) for i in self.mon_grouping.split(',')]
    
    def grouping_list(self):
        return [int(i) for i in self.grouping.split(',')]
    
    def localconv(self):
        raise NotImplementedError
    
    def strcoll(self, string1, string2):
        raise NotImplementedError
    
    def strxfrm(self, string):
        raise NotImplementedError
    
    def format(self, val, grouping=False, monetary=False):
        raise NotImplementedError
    
    def format_string(self, format, val, grouping=False):
        raise NotImplementedError
    
    def currency(self, val, symbol=True, grouping=False, international=False):
        value = Decimal(str(val))
        q = Decimal(10) ** -self.int_frac_digits     # 2 places --> '0.01'
        neg, digits, exp = value.quantize(q).as_tuple()
        
        result = []
        digits = map(str, digits)
        build = lambda x: result.append(unicode(x))
        next = lambda: unicode(digits.pop())
        
        cs_precedes = ((neg and self.n_cs_precedes) or
                       (not neg and self.p_cs_precedes))
        
        if neg:
            sign_posn = self.n_sign_posn
        else:
            sign_posn = self.p_sign_posn
        
        if neg:
            sep_by_space = self.n_sep_by_space
        else:
            sep_by_space = self.p_sep_by_space
        
        if grouping:
            grouping = self.mon_grouping_list()
        else:
            grouping = list()
        
        def sign_symbol():
            if neg:
                build(self.negative_sign)
            else:
                build(self.positive_sign)
        
        def currency_symbol():
            if symbol:
                if cs_precedes and sep_by_space:
                    build(' ')
                if international:
                    build(self.int_curr_symbol)
                else:
                    build(self.currency_symbol)
                if not cs_precedes and sep_by_space:
                    build(' ')
        if sign_posn == 0:
            build(')')
        if sign_posn == 2:
            sign_symbol()
        if not cs_precedes:
            currency_symbol()
        if sign_posn == 4:
            sign_symbol()
        for i in range(self.int_frac_digits):
            build(next() if digits else '0')
        if self.int_frac_digits:
            build(self.mon_decimal_point)
        if not digits:
            build('0')
        i = 0
        while digits:
            build(next())
            i += 1
            if grouping and grouping[0] == i and digits:
                i = 0
                build(self.mon_thousands_sep.strip())
                if grouping[-1] != 0:
                    grouping.pop(0)
        if sign_posn == 3:
            sign_symbol()
        if cs_precedes:
            currency_symbol()
        if sign_posn == 1:
            sign_symbol()
        if sign_posn == 0:
            build('(')
        return u''.join(reversed(result))
    
    def str(self, val):
        raise NotImplementedError
    
    def atof(self, val):
        raise NotImplementedError
    
    def atoi(self, val):
        raise NotImplementedError
    
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
