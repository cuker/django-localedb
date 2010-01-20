from django.utils import simplejson
from django.http import HttpResponse

from models import Locale, get_locale

def ajax_currency_info(request, locale_name=None):
    if locale_name:
        locale = Locale.objects.get(name=locale_name)
    else:
        try:
            locale = get_locale()
        except Locale.DoesNotExist:
            return HttpResponse(simplejson.dumps(None), content_type="text/x-json")
    ret = dict()
    for field in locale._meta.fields:
        key = field.name
        ret[key] = getattr(locale, key, None)
    return HttpResponse(simplejson.dumps(ret), content_type="text/x-json")
    
def ajax_currency(request, value, locale_name=None):
    if locale_name:
        locale = Locale.objects.get(name=locale_name)
    else:
        try:
            locale = get_locale(value)
        except Locale.DoesNotExist:
            return HttpResponse(value)
    return HttpResponse(locale.currency(value))
