from django.contrib import admin

from .models import Product,Productlogin,Cart

# Register your models here.

admin.site.register(Product)
admin.site.register(Productlogin)
admin.site.register(Cart)
