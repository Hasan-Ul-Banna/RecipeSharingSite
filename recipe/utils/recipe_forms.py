from django.forms import ModelForm
from recipe.models.recipe_models import Recipe, Comment, Rating

class RecipeModelForm(ModelForm):
    class Meta:
        model = Recipe
        exclude = ['owner']

class CommentForm(ModelForm):
    class Meta:
        model = Comment
        exclude = ['comment_owner']

class RatingForm(ModelForm):
    class Meta:
        model = Rating
        exclude = ['rating_owner']
