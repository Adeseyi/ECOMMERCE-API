from django.contrib import admin
from ecommerce_app.models import Categories, Book, Product, Cart

from django.contrib import admin
# Register your models here.
admin.site.register(Categories)

from django.contrib import admin
# Register your models here.
admin.site.register(Book)

from django.contrib import admin
# Register your models here.
admin.site.register(Product)


admin.site.register(Cart)