from django.contrib.sitemaps import Sitemap
from django.urls import reverse
from recipes.models import Recipe, Category

class StaticViewSitemap(Sitemap):
    priority = 0.5
    changefreq = 'daily'

    def items(self):
        return ['index', 'recipe_list', 'recipe-create','search-recipe','register','login','logout','profile','starred_recipes']


class RecipeSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.8

    def items(self):
        return Recipe.objects.all()

class CategorySitemap(Sitemap):
    changefreq = "monthly"
    priority = 0.7

    def items(self):
        return Category.objects.all()
