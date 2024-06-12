from django.contrib import admin
from .models import Item, StoreInventory, Supplier

admin.site.register(Item)
admin.site.register(StoreInventory)
admin.site.register(Supplier)
