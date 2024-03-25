from django.contrib import admin

from .models import *


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    readonly_fields = ('id', 'created_at', 'updated_at')


@admin.register(Review)
class ProductReview(admin.ModelAdmin):
    readonly_fields = ('id', 'created_at', 'updated_at')
