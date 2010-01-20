from django.conf.urls.defaults import *

urlpatterns = patterns('',
    (r'^currency-info/$', 'localedb.views.ajax_currency_info'),
)
