from django.test import TestCase
from recipe.models.recipe_models import Recipe 
from recipe.models.user_models import User


from recipe.utils.recipe_forms import RecipeForm, CommentForm, RatingForm



class TestForms(TestCase):
    
    def test_recipe_form_valid(self):

        form = RecipeForm({
            'title': 'test',
            'recipe_text': 'test',
        })

        self.assertTrue(form.is_valid())

    def test_recipe_form_invalid(self):
        form = RecipeForm({
        })
        self.assertFalse(form.is_valid())
    
    def test_comment_form_valid(self):
        user = User.objects.create(username="testuser")
        recipe = Recipe.objects.create(title="Test Recipe", owner=user)
        form = CommentForm({
            'comment': 'test',
            'recipe': recipe,
        })

        self.assertTrue(form.is_valid())

    def test_comment_form_invalid(self):
        form = CommentForm({
        })
        self.assertFalse(form.is_valid())

    def test_rating_form_valid(self):
        user = User.objects.create(username="testuser")
        recipe = Recipe.objects.create(title="Test Recipe", owner=user)
        form = RatingForm({
            'rating_value': 3,
            'recipe': recipe,
        })

        self.assertTrue(form.is_valid())

    def test_rating_form_invalid(self):
        form = RatingForm({
        })
        self.assertFalse(form.is_valid())