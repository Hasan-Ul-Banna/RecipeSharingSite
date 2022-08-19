from django.db import models
from django.contrib.auth import get_user_model
# Create your models here.

user_model = get_user_model()

class Ingredient(models.Model):
    name = models.CharField(max_length=200)

class Recipe(models.Model):
    title = models.CharField(max_length=200)
    owner = models.ForeignKey(user_model, on_delete=models.CASCADE)
    date_posted = models.DateField(auto_now_add=True)
    ingredients = models.ManyToManyField(Ingredient)
    recipe_text = models.TextField()

class Rating(models.Model):
    rating_choices = (
        (1, '1 star'),
        (2, '2 stars'),
        (3, '3 stars'),
        (4, '4 stars'),
        (5, '5 stars'),
    )
    rating_value = models.IntegerField(
        choices = rating_choices
    )
    rating_owner = models.ForeignKey(user_model, on_delete=models.CASCADE)
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)

    class Meta:
        unique_together = ["rating_owner", "recipe"]


class Comment(models.Model):
    comment = models.TextField()
    comment_owner = models.ForeignKey(user_model, on_delete=models.CASCADE)
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)


class ReportRecipe(models.Model):
    reporter = models.ForeignKey(user_model, on_delete=models.CASCADE)
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    report_reason = models.TextField(blank=True)

class ReportComment(models.Model):
    reporter = models.ForeignKey(user_model, on_delete=models.CASCADE)
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE)
    report_reason = models.TextField(blank=True)



