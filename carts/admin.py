from django.contrib import admin
from .models import Cart, CartItem

# Register your models here.
class CartAddmin(admin.ModelAdmin):
    list_display = ('cart_id','date_added')

class CartItemAddmin(admin.ModelAdmin):
    list_display = ('product','cart','quantity','is_active')

admin.site.register(Cart,CartAddmin)
admin.site.register(CartItem,CartItemAddmin)