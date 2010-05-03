# -*- coding: utf-8 -*-
from django.test import TestCase
# from django import template

from models import Locale, get_locale

from decimal import Decimal

# import mockup
import sys

class BaseLocalizedTest(TestCase):
    """
    Base class for tests using a real locale
    """
    
    # TODO: Need to think of a way to set this up
    pass
    # def setUp(self):
    #     self.oldlocale = locale.setlocale(self.locale_type)
    #     locale.setlocale(self.locale_type, enUS_locale)
    #     if verbose:
    #         print "testing with \"%s\"..." % enUS_locale,
    # 
    # def tearDown(self):
    #     locale.setlocale(self.locale_type, self.oldlocale)


class BaseFormattingTest(TestCase):
    """
    Utility functions for formatting tests
    """
    fixtures = ['locale_data']

    def setUp(self):
        self.locale = Locale.objects.get(name='C')

    def test_current_locale(self):
        self.assertEqual(self.locale.name, 'C')

    def _test_formatfunc(self, format, value, out, func, **format_opts):
        self.assertEqual(func(format, value, **format_opts), out)

    def _test_format(self, format, value, out, **format_opts):
        self._test_formatfunc(format, value, out, func=self.locale.format, **format_opts)

    def _test_format_string(self, format, value, out, **format_opts):
        self._test_formatfunc(format, value, out, func=self.locale.format_string, **format_opts)

    def _test_currency(self, value, out, **format_opts):
        self.assertEqual(self.locale.currency(value, **format_opts), out)


class EnUSNumberFormatting(BaseFormattingTest):
    """
    XXX there is a grouping + padding bug when the thousands separator
    is empty but the grouping array contains values (e.g. Solaris 10)
    """

    def setUp(self):
        BaseFormattingTest.setUp(self)
        self.locale = Locale.objects.get(name='en_US')
        self.sep = self.locale.thousands_sep

    def test_current_locale(self):
        self.assertEqual(self.locale.name, 'en_US')

    def test_grouping(self):
        self._test_format("%f", 1024, grouping=1, out='1%s024.000000' % self.sep)
        self._test_format("%f", 102, grouping=1, out='102.000000')
        self._test_format("%f", -42, grouping=1, out='-42.000000')
        self._test_format("%+f", -42, grouping=1, out='-42.000000')

    def test_grouping_and_padding(self):
        self._test_format("%20.f", -42, grouping=1, out='-42'.rjust(20))
        if self.sep:
            self._test_format("%+10.f", -4200, grouping=1,
                out=('-4%s200' % self.sep).rjust(10))
            self._test_format("%-10.f", -4200, grouping=1,
                out=('-4%s200' % self.sep).ljust(10))

    def test_integer_grouping(self):
        self._test_format("%d", 4200, grouping=True, out='4%s200' % self.sep)
        self._test_format("%+d", 4200, grouping=True, out='+4%s200' % self.sep)
        self._test_format("%+d", -4200, grouping=True, out='-4%s200' % self.sep)

    def test_integer_grouping_and_padding(self):
        self._test_format("%10d", 4200, grouping=True,
            out=('4%s200' % self.sep).rjust(10))
        self._test_format("%-10d", -4200, grouping=True,
            out=('-4%s200' % self.sep).ljust(10))

    def test_simple(self):
        self._test_format("%f", 1024, grouping=0, out='1024.000000')
        self._test_format("%f", 102, grouping=0, out='102.000000')
        self._test_format("%f", -42, grouping=0, out='-42.000000')
        self._test_format("%+f", -42, grouping=0, out='-42.000000')

    def test_padding(self):
        self._test_format("%20.f", -42, grouping=0, out='-42'.rjust(20))
        self._test_format("%+10.f", -4200, grouping=0, out='-4200'.rjust(10))
        self._test_format("%-10.f", 4200, grouping=0, out='4200'.ljust(10))

    def test_complex_formatting(self):
        # Spaces in formatting string
        self._test_format_string("One million is %i", 1000000, grouping=1,
            out='One million is 1%s000%s000' % (self.sep, self.sep))
        self._test_format_string("One  million is %i", 1000000, grouping=1,
            out='One  million is 1%s000%s000' % (self.sep, self.sep))
        # Dots in formatting string
        self._test_format_string(".%f.", 1000.0, out='.1000.000000.')
        # Padding
        if self.sep:
            self._test_format_string("-->  %10.2f", 4200, grouping=1,
                out='-->  ' + ('4%s200.00' % self.sep).rjust(10))
        # Asterisk formats
        self._test_format_string("%10.*f", (2, 1000), grouping=0,
            out='1000.00'.rjust(10))
        if self.sep:
            self._test_format_string("%*.*f", (10, 2, 1000), grouping=1,
                out=('1%s000.00' % self.sep).rjust(10))
        # Test more-in-one
        if self.sep:
            self._test_format_string("int %i float %.2f str %s",
                (1000, 1000.0, 'str'), grouping=1,
                out='int 1%s000 float 1%s000.00 str str' %
                (self.sep, self.sep))


class TestNumberFormatting(BaseLocalizedTest, EnUSNumberFormatting):
    # Test number formatting with a real English locale.

    # locale_type = locale.LC_NUMERIC

    def setUp(self):
        BaseLocalizedTest.setUp(self)
        EnUSNumberFormatting.setUp(self)


class TestEnUSNumberFormatting(EnUSNumberFormatting):
    # Test number formatting with a cooked "en_US" locale.

    def setUp(self):
        EnUSNumberFormatting.setUp(self)

    def test_currency(self):
        self._test_currency(50000, "$50000.00")
        self._test_currency(50000, "$50,000.00", grouping=True)
        self._test_currency(50000, "USD 50,000.00",
            grouping=True, international=True)

    def test_differing_currency_code(self):
        class Money(Decimal):
            def __init__(self, value, currency):
                super(Money, self).__init__(value)
                self.currency = currency
        five_thousand_gbp = Money(5000, 'GBP')
        self._test_currency(five_thousand_gbp, "GBP 5000.00")


class TestCNumberFormatting(BaseFormattingTest):
    # Test number formatting with a cooked "C" locale.

    def test_grouping(self):
        self._test_format("%.2f", 12345.67, grouping=True, out='12345.67')

    def test_grouping_and_padding(self):
        self._test_format("%9.2f", 12345.67, grouping=True, out=' 12345.67')


class TestFrFRNumberFormatting(BaseFormattingTest):
    """
    Test number formatting with a cooked "fr_FR" locale.
    """

    def setUp(self):
        BaseFormattingTest.setUp(self)
        self.locale = Locale.objects.get(name='fr_FR')
    
    def test_current_locale(self):
        self.assertEqual(self.locale.name, 'fr_FR')
    
    def test_decimal_point(self):
        self._test_format("%.2f", 12345.67, out='12345,67')

    def test_grouping(self):
        self._test_format("%.2f", 345.67, grouping=True, out='345,67')
        self._test_format("%.2f", 12345.67, grouping=True, out='12 345,67')

    def test_grouping_and_padding(self):
        self._test_format("%6.2f", 345.67, grouping=True, out='345,67')
        self._test_format("%7.2f", 345.67, grouping=True, out=' 345,67')
        self._test_format("%8.2f", 12345.67, grouping=True, out='12 345,67')
        self._test_format("%9.2f", 12345.67, grouping=True, out='12 345,67')
        self._test_format("%10.2f", 12345.67, grouping=True, out=' 12 345,67')
        self._test_format("%-6.2f", 345.67, grouping=True, out='345,67')
        self._test_format("%-7.2f", 345.67, grouping=True, out='345,67 ')
        self._test_format("%-8.2f", 12345.67, grouping=True, out='12 345,67')
        self._test_format("%-9.2f", 12345.67, grouping=True, out='12 345,67')
        self._test_format("%-10.2f", 12345.67, grouping=True, out='12 345,67 ')

    def test_integer_grouping(self):
        self._test_format("%d", 200, grouping=True, out='200')
        self._test_format("%d", 4200, grouping=True, out='4 200')

    def test_integer_grouping_and_padding(self):
        self._test_format("%4d", 4200, grouping=True, out='4 200')
        self._test_format("%5d", 4200, grouping=True, out='4 200')
        self._test_format("%10d", 4200, grouping=True, out='4 200'.rjust(10))
        self._test_format("%-4d", 4200, grouping=True, out='4 200')
        self._test_format("%-5d", 4200, grouping=True, out='4 200')
        self._test_format("%-10d", 4200, grouping=True, out='4 200'.ljust(10))

    def test_currency(self):
        euro = u'\u20ac'
        self._test_currency(50000, "50000,00 " + euro)
        self._test_currency(50000, "50 000,00 " + euro, grouping=True)
        # XXX is the trailing space a bug?
        self._test_currency(50000, "50 000,00 EUR ",
            grouping=True, international=True)

    def test_atof(self):
        self.assertEqual(self.locale.atof('12 345,67'), 12345.67)


class TestStringMethods(BaseLocalizedTest):
    # locale_type = locale.LC_CTYPE

    if sys.platform != 'sunos5' and not sys.platform.startswith("win"):
        # Test BSD Rune locale's bug for isctype functions.

        def test_isspace(self):
            self.assertEqual('\x20'.isspace(), True)
            self.assertEqual('\xa0'.isspace(), False)
            self.assertEqual('\xa1'.isspace(), False)

        def test_isalpha(self):
            self.assertEqual('\xc0'.isalpha(), False)

        def test_isalnum(self):
            self.assertEqual('\xc0'.isalnum(), False)

        def test_isupper(self):
            self.assertEqual('\xc0'.isupper(), False)

        def test_islower(self):
            self.assertEqual('\xc0'.islower(), False)

        def test_lower(self):
            self.assertEqual('\xcc\x85'.lower(), '\xcc\x85')

        def test_upper(self):
            self.assertEqual('\xed\x95\xa0'.upper(), '\xed\x95\xa0')

        def test_strip(self):
            self.assertEqual('\xed\x95\xa0'.strip(), '\xed\x95\xa0')

        def test_split(self):
            self.assertEqual('\xec\xa0\xbc'.split(), ['\xec\xa0\xbc'])


# class TestMiscellaneous(TestCase):
#     def test_getpreferredencoding(self):
#         # Invoke getpreferredencoding to make sure it does not cause exceptions.
#         enc = locale.getpreferredencoding()
#         if enc:
#             # If encoding non-empty, make sure it is valid
#             codecs.lookup(enc)
# 
#     if hasattr(locale, "strcoll"):
#         def test_strcoll_3303(self):
#             # test crasher from bug #3303
#             self.assertRaises(TypeError, locale.strcoll, u"a", None)

##
# Old testage
##
# class CurrencyTestCase(TestCase):
#     fixtures = ['locale_data']
# 
#     def test_localconv(self):
#         return  #  TODO  use or lose test_localconv
#         for loc in Locale.objects.all():
#             loc.localconv()
# 
#     def test_strcoll(self):
#         return  #  TODO  use or lose test_strcoll
#         # TODO  assert that any locales exist - else this test goes silently void!
#         for loc in Locale.objects.all():
#             locale = mockup.LocaleMockup(loc.name)
#             self.assertEqualSign(locale.strcoll("foobar", "barfoo"),
#                                  loc.strcoll("foobar", "barfoo"))
#             self.assertEqualSign(locale.strcoll("12foobar", "15barfoo"),
#                                  loc.strcoll("12foobar", "15barfoo"))
#             self.assertEqualSign(locale.strcoll("1foobar", "1barfoo"),
#                                  loc.strcoll("1foobar", "1barfoo"))
#             self.assertEqualSign(locale.strcoll("foobar12", "foobar15"),
#                                  loc.strcoll("foobar12", "foobar15"))
#             self.assertEqualSign(locale.strcoll("Foobar", "Barfoo"),
#                                  loc.strcoll("Foobar", "Barfoo"))
# 
#     def assert_currency_equal(self, a, b, **kw):
#             locale = mockup.LocaleMockup(self.loc.locale_name())
#             self.assertEqual(self.loc.currency(a, **kw), locale.currency(b, **kw))
# 
#     def test_currency(self):
#         assert len(mockup.AVAILABLE_LOCALES)
#         queryset = Locale.objects.all().filter(name__in=[item.split('.')[0] for item in mockup.AVAILABLE_LOCALES])
#         assert queryset.count()
#         for self.loc in queryset:
#             locale = mockup.LocaleMockup(self.loc.locale_name())
#             #print self.loc.name
#             self.assert_currency_equal(      5      ,      5       )
#             self.assert_currency_equal(    -57.00005,    -57.00005 )
#             self.assert_currency_equal( 500000      , 500000       )
#             self.assert_currency_equal(      5      ,      5,       grouping=True)
#             self.assert_currency_equal(    -57.00005,    -57.00005, grouping=True)
#             self.assert_currency_equal( 500000      , 500000      , grouping=True)
#             self.assert_currency_equal(      5      ,      5      , international=True)
#             self.assert_currency_equal(    -57.00005,    -57.00005, international=True)
#             self.assert_currency_equal( 500000      , 500000      , international=True)
#             self.assert_currency_equal(      5      ,      5      , symbol=False)
#             self.assert_currency_equal(    -57.00005,    -57.00005, symbol=False)
#             self.assert_currency_equal( 500000      , 500000      , symbol=False)
#             self.assert_currency_equal(    -57.05   ,    -57.05   , international=True, grouping=True)
# 
#     def test_template_tag_currency(self):
#         from localedb.templatetags.currencies import currency
# 
#         self.assertEqual('$5.00', currency(5.00))
#         self.assertEqual('$15.16', currency(15.15555, 'en_US'))
# 
#     def test_template_tag_withlocale(self):
#         info = '''
#         {% load currencies %}
#         {% withlocale "en_SG" as locale %}
#             {en_SG:"{{ locale.d_t_fmt }}",
#         {% endwithlocale %}
# 
#         {% withlocale locale %}{#retrieves default locale #}
#             default:"{{ locale.d_t_fmt }}"}
#         {% endwithlocale %}
#         '''
#         t = template.Template(info)
#         c = template.Context({})
#         result = t.render(c)
#         self.assertNotEqual(-1, result.find(Locale.objects.get(name='en_US').d_t_fmt))

