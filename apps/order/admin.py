from django.contrib import admin

from .models import *


class OrderItemInline(admin.TabularInline):
    model = OrderItem
    extra = 1


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    inlines = (OrderItemInline,)
    readonly_fields = ('id', 'created_at', 'updated_at')


class CartItemInline(admin.TabularInline):
    model = CartItem
    extra = 1


class CartAdmin(admin.ModelAdmin):
    inlines = (CartItemInline,)
    readonly_fields = ('id', 'created_at', 'updated_at')
