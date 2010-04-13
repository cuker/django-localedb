from localedb.models import Locale

class LocaleDBMiddleware(object):
    def process_request(self, request):
        try:
            request.locale = Locale.objects.get_site_locale()
        except Locale.DoesNotExist:
            request.locale = None
