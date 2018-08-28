from django.contrib import admin
from mysite import inventory

admin.site.register(inventory.models.Product)
admin.site.register(inventory.models.Customer)

