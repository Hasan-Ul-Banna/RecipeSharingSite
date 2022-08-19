from django.forms import ModelForm
from recipe.models import Recipe,Comment

class RecipeModelForm(ModelForm):
    class Meta:
        model = Recipe
        fields = "__all__"

class CommentForm(ModelForm):
    class Meta:
        model = Comment
        exclude = ['comment_owner']
