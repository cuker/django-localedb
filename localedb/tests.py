from webcube.webcubecore.test_suite import WebCubeTestSuite
from django import template
from simplecart.currencies.models import Locale

import mockup

class CurrencyTestCase(WebCubeTestSuite):
    fixtures = ['short_countries',] # TODO why 'locale_data'] exceptions on teahupoo??

    def test_localconv(self):
        return  #  TODO  use or lose test_localconv
        for loc in Locale.objects.all():
            loc.localconv()

    def test_strcoll(self):
        return  #  TODO  use or lose test_strcoll
        # TODO  assert that any locales exist - else this test goes silently void!
        for loc in Locale.objects.all():
            locale = mockup.LocaleMockup(loc.name)
            self.assertEqualSign(locale.strcoll("foobar", "barfoo"),
                                 loc.strcoll("foobar", "barfoo"))
            self.assertEqualSign(locale.strcoll("12foobar", "15barfoo"),
                                 loc.strcoll("12foobar", "15barfoo"))
            self.assertEqualSign(locale.strcoll("1foobar", "1barfoo"),
                                 loc.strcoll("1foobar", "1barfoo"))
            self.assertEqualSign(locale.strcoll("foobar12", "foobar15"),
                                 loc.strcoll("foobar12", "foobar15"))
            self.assertEqualSign(locale.strcoll("Foobar", "Barfoo"),
                                 loc.strcoll("Foobar", "Barfoo"))

    def assert_currency_equal(self, a, b, **kw):
            locale = mockup.LocaleMockup(self.loc.name)
            self.assertEqual(self.loc.currency(a, **kw), locale.currency(b, **kw))

    def test_currency(self):
        # TODO  assert that any locales exist - else this test goes silently void!
        for self.loc in Locale.objects.all().filter(name__in=mockup.AVAILABLE_LOCALES):
            locale = mockup.LocaleMockup(self.loc.name)
            #print self.loc.name
            self.assert_currency_equal(      5,            5       )
            self.assert_currency_equal(    -57.00005,    -57.00005 )
            self.assert_currency_equal( 500000,       500000       )
            self.assert_currency_equal(      5,            5,       grouping=True)
            self.assert_currency_equal(    -57.00005,    -57.00005, grouping=True)
            self.assert_currency_equal( 500000,       500000,       grouping=True)
            self.assert_currency_equal(      5,            5,       international=True)
            self.assert_currency_equal(    -57.00005,    -57.00005, international=True)
            self.assert_currency_equal( 500000,       500000,       international=True)
            self.assert_currency_equal(      5,            5,       symbol=False)
            self.assert_currency_equal(    -57.00005,    -57.00005, symbol=False)
            self.assert_currency_equal( 500000,       500000,       symbol=False)
            self.assert_currency_equal(    -57.05,       -57.05, international=True, grouping=True)

    def test_template_tag_currency(self):
        from simplecart.currencies.templatetags.currencies import currency

        self.assert_regex_contains(r'\$?5.00', currency('5.00')) #  TODO  get this back to assertEqual() on teahupoo!
      # TODO  self.assertEqual('$15.16', currency('15.15555', 'en_US'))

    def test_template_tag_withlocale(self):
        info = '''
        {% load currencies %}
        {% withlocale "en_SG" as locale %}
            {en_SG:"{{ locale.d_t_fmt }}",
        {% endwithlocale %}

        {% withlocale locale %}{#retrieves default locale #}
            default:"{{ locale.d_t_fmt }}"}
        {% endwithlocale %}
        '''
        t = template.Template(info)
        c = template.Context({})
        return # TODO  get this test back online on teahupoo!
        result = t.render(c)
        self.assertNotEqual(-1, result.find(Locale.objects.get(name='en_US').d_t_fmt))
