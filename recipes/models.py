from django.db import models
import PIL
from django.conf import settings
from django.core.validators import MinValueValidator, MaxValueValidator
from django.contrib.auth.models import AbstractUser, User
from django.contrib.auth.models import AbstractUser
from django.db import models

class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    profile_pic = models.ImageField(upload_to="images/", default="images/default.png")

    def __str__(self):
        return f"{self.user.username} Profile"

class Cuisine(models.Model):
    name = models.CharField(max_length=250)
    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=250)
    def __str__(self):
        return self.name

class Recipe(models.Model):
    title = models.CharField(max_length=30)
    description = models.TextField(default="")
    ingredients = models.TextField(default="", help_text="Separate ingredients with commas.")
    cook_time = models.PositiveIntegerField(help_text="Cooking time in minutes.")
    servings = models.PositiveIntegerField()
    method = models.TextField(default="", help_text = "Enter each step in the format 'Step (number): (instructions)'")
    image = models.ImageField(upload_to="images/")
    cuisine = models.ManyToManyField(Cuisine)
    category = models.ManyToManyField(Category)
    DIFFICULTY_CHOICES = [
    ('easy', 'Easy'),
    ('medium', 'Medium'),
    ('hard', 'Hard'),
    ('expert', 'Expert')
]
    difficulty = models.CharField(max_length=250, choices = DIFFICULTY_CHOICES, default = "easy")
    def __str__(self):
        return self.title

    def average_rating(self):
        return self.ratings.aggregate(models.Avg('stars'))['stars__avg'] or 0

    def total_ratings(self):
        return self.ratings.count()
        
class Rating(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE, related_name='ratings')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    value = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)]
    )
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        unique_together = ('recipe', 'user')
