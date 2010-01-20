from django.contrib import admin

from simplecart.orders import SHOP_ADMIN_SITE

from models import Locale, LocaleSiteDefault

SHOP_ADMIN_SITE.register(Locale)
SHOP_ADMIN_SITE.register(LocaleSiteDefault)
