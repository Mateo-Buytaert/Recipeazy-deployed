from django.contrib import admin
from .models import Recipe, Cuisine, Category, Profile

# Register your models here.

@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    list_display = ('title', 'cook_time', 'servings')
admin.site.register(Cuisine)
admin.site.register(Category)
admin.site.register(Profile)