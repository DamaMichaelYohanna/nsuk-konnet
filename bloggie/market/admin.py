from django.contrib import admin

from .models import Product, Store, Catalog, Order, StoreOrder

admin.site.register(Product)
admin.site.register(Store)
admin.site.register(Catalog)
admin.site.register(Order)
admin.site.register(StoreOrder)
