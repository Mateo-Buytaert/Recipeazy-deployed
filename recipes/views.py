from django.shortcuts import render, reverse, redirect, get_object_or_404, HttpResponse
from .models import Recipe, Rating, Category
from .forms import RecipeForm, CreateUserForm, UserUpdateForm, ProfileUpdateForm, RatingForm
from django.db.models import Q, Avg
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.db.models import Avg, Count

def index(request):
    if request.method == "GET":
        recipes = Recipe.objects.annotate(avg_rating = Avg("ratings__value")).order_by("-avg_rating")[:3]
        return render(request, 'recipes/index.html', {'recipes': recipes})

def recipe_list(request):
    recipes = Recipe.objects.all()[:15]
    ingredients = []
    for recipe in recipes:
        ingredients.append(recipe.ingredients)
    return render(request,"recipes/recipe_list.html",{"recipes":recipes, "ingredients":ingredients})

def recipe_list_category(request, category):
    recipes = Recipe.objects.filter(Q(category__name__icontains=category))
    ingredients = []
    for recipe in recipes:
        ingredients.append(recipe.ingredients)
    return render(request,"recipes/recipe_list.html",{"recipes":recipes, "ingredients":ingredients})

@login_required(login_url="login")
def recipe_create(request):
    if request.method == 'POST':
        form = RecipeForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = RecipeForm()
    return render(request, 'recipes/recipe_form.html', {'form': form})

def recipe_detail(request, id):
    recipe = get_object_or_404(Recipe, id=id)
    ingredients = recipe.ingredients
    ingredients = ingredients.split(", ")
    if request.method == 'POST' and request.user.is_authenticated:
        rating_value = request.POST.get('rating')
        if rating_value:
            rating, created = Rating.objects.get_or_create(
                recipe=recipe,
                user=request.user,
                defaults={'value': rating_value}
            )
            if not created:
                rating.value = rating_value
                rating.save()
            return redirect('recipe-detail', id=id)

    rating_data = Recipe.objects.filter(id=id).annotate(
        avg_rating=Avg('ratings__value'),
        rating_count=Count('ratings')
    ).values('avg_rating', 'rating_count').first()
    
    avg_rating = rating_data['avg_rating'] or 0
    rating_count = rating_data['rating_count']
    
    user_rating = None
    if request.user.is_authenticated:
        user_rating = Rating.objects.filter(recipe=recipe, user=request.user).first()
    
    avg_rating = round(avg_rating)
    return render(request,"recipes/recipe_detail.html",{
        "recipe":recipe,
        "ingredients":ingredients,
        "avg_rating":avg_rating,
        "user_rating":user_rating,
        "rating_count":rating_count
    })
    
def search_recipe(request):
    query = request.GET.get("q")
    recipes = Recipe.objects.filter(
                Q(title__icontains=query) | 
                Q(category__name__icontains=query)
            ).distinct() 
    ingredients = []
    for recipe in recipes:
        ingredients.append(recipe.ingredients)
    return render(request,"recipes/recipe_list.html",{
        "recipes":recipes,
        "ingredients":ingredients,
    })

def registerPage(request):
    if request.user.is_authenticated:
        return redirect("index")
    else:
        form = CreateUserForm()

        if request.method == "POST":
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                user = form.cleaned_data.get("username")
                messages.success(request, "Account was created for "+user)
                return redirect("login")

        return render(request, "recipes/register.html",{
            "form":form
        })

def loginPage(request):
    if request.user.is_authenticated:
        return redirect("index")
    else:
        if request.method=="POST":
            username = request.POST.get("username")
            password = request.POST.get("password")
            user = authenticate(request, username=username,password=password)

            if user is not None:
                login(request,user)
                return redirect("index")
            else:
                messages.info(request,"Username or password is incorrect")

        return render(request,"recipes/login.html")

def logoutUser(request):
    logout(request)
    return redirect("index")

@login_required(login_url="login")
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST,
                                   request.FILES,
                                   instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your account has been updated!')
            return redirect('profile') # Redirect back to profile page

    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'u_form': u_form,
        'p_form': p_form
    }

    return render(request, 'recipes/profile.html', context)