from django.contrib.sitemaps import Sitemap
from django.urls import reverse
from recipes.models import Recipe

class StaticViewSitemap(Sitemap):
    priority = 0.5
    changefreq = 'daily'

    def items(self):
        return ['home', 'about']  # Your named URL patterns

    def location(self, item):
        return reverse(item)

class RecipeSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.8

    def items(self):
        return Recipe.objects.all()
