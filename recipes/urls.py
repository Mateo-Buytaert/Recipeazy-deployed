from . import views
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("", views.index, name="index"),
    path("recipe-list/", views.recipe_list, name = "recipe_list"),
    path("make-recipe", views.recipe_create,name="recipe-create"),
    path("recipe-list/<int:id>", views.recipe_detail,name="recipe-detail"),
    path("recipe-list/<str:category>", views.recipe_list_category,name="recipe-detail-category"),
    path("search-recipe/", views.search_recipe, name="search-recipe"),
    path("register/",views.registerPage, name = "register"),
    path("login/", views.loginPage, name="login"),
    path("logout/", views.logoutUser, name="logout"),
    path("profile/", views.profile, name="profile"),
    path("star/<int:recipe_id>/", views.star_recipe,name="star-recipe"),
    path("starred_recipes/",views.starred_recipes,name="starred_recipes"),
    path('search/', views.search_view, name='search'),
]
