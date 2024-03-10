from django.contrib import admin
from .models import Category, Spent


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass


@admin.register(Spent)
class SpentAdmin(admin.ModelAdmin):
    pass
