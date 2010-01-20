from django.conf.urls.defaults import *

urlpatterns = patterns('',
    (r'^currency-info/$', 'simplecart.currencies.views.ajax_currency_info'),
)
