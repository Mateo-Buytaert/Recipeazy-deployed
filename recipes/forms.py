from django import forms
from .models import Recipe, Profile, Rating
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ModelForm

class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = ['title','cook_time', 'servings',"cuisine","category","description", 'ingredients',"method","image"]

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ["username","email","password1","password2"]

class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ["username","email"]

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ["profile_pic"]
class RatingForm(forms.ModelForm):
    class Meta:
        model = Rating
        fields = ["value"]
