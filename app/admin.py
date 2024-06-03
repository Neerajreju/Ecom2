from django.contrib import admin
from .models import Products , Customers
# Register your models here.
@admin.register(Products)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['id' , 'title' , 'discounted_price' , 'category','product_image']

@admin.register(Customers)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ['id' , 'user' , 'locality' , 'city','state','zipcode']
