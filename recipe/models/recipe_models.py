from django.db import models
from django.contrib.auth import get_user_model
# Create your models here.

user_model = get_user_model()


class Recipe(models.Model):
    title = models.CharField(max_length=200)
    picture = models.ImageField(upload_to="media/images/recipe_pictures/", null=True, blank=True)
    owner = models.ForeignKey(user_model, on_delete=models.CASCADE)
    date_posted = models.DateField(auto_now_add=True)
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




