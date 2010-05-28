from django.template import Library, Node, NodeList, Template, Context, Variable
from django.template import TemplateSyntaxError

from localedb.models import Locale, get_locale

register = Library()

@register.filter
def currency(value, locale_name=None):
    if locale_name:
        locale = Locale.objects.get(name=locale_name)
    else:
        try:
            locale = get_locale(value)
        except Locale.DoesNotExist:
            if hasattr(value, 'currency') and hasattr(value, 'amount'):
                if hasattr(value.currency, 'code'):
                    return u'%s %s' % (value.currency.code, value.amount)
                return u'%s %s' % (value.currency, value.amount)
            return value
    return locale.currency(value)


class WithLocaleNode(Node):
    def __init__(self, var, name, nodelist):
        self.var = var
        self.name = name
        self.nodelist = nodelist

    def __repr__(self):
        return "<WithLocaleNode>"

    def render(self, context):
        if self.var:
            val = self.var.resolve(context)
            locale = Locale.objects.get(name=val)
        else:
            locale = get_locale()
        context.push()
        context[self.name] = locale
        output = self.nodelist.render(context)
        context.pop()
        return output

#@register.tag
def do_with_locale(parser, token):
    """
    Adds a value to the context (inside of this block) for caching and easy
    access.

    For example::

        {% withlocale "en_US" as locale %}
            {% now locale.d_t_fmt %}
        {% endwithlocale %}

        {% withlocale locale %}{#retrieves default locale #}
            {% now locale.d_t_fmt %}
        {% endwithlocale %}
    """
    bits = list(token.split_contents())
    if len(bits) == 2:
        var = None
    elif len(bits) != 4 or bits[2] != "as":
        raise TemplateSyntaxError("%r expected format is 'value as name'" %
                                  bits[0])
    else:
        var = parser.compile_filter(bits[1])
    name = bits[-1]
    nodelist = parser.parse(('endwithlocale',))
    parser.delete_first_token()
    return WithLocaleNode(var, name, nodelist)
do_with_locale = register.tag('withlocale', do_with_locale)

