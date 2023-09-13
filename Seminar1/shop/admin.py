from django.contrib import admin
from .models import Client, Product, Order


@admin.action(description="Уменьшить количество на одну единицу")
def reduce_quantity(modeladmin, request, queryset):
    for obj in queryset:
        obj.amount -= 1
        obj.save()


class CategoryClient(admin.ModelAdmin):
    list_display = ['name', 'email', 'phone', 'address', 'registration_date']
    fields = ['name', 'email', 'phone', 'address']


class CategoryProduct(admin.ModelAdmin):
    list_display = ['name', 'description', 'price', 'amount', 'added_date']
    ordering = ['-price', 'name']
    list_filter = ['added_date']
    search_fields = ['name', 'description']
    actions = [reduce_quantity]


class CategoryOrder(admin.ModelAdmin):
    list_display = ['client', 'total_amount', 'order_date']


# Register your models here.
admin.site.register(Client, CategoryClient)
admin.site.register(Product, CategoryProduct)
admin.site.register(Order, CategoryOrder)
