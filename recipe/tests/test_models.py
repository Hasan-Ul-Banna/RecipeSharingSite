from django.test import TestCase
from recipe.models.recipe_models import Recipe, Rating, Comment
from recipe.models.user_models import User



class TestModels(TestCase):
    def setUp(self):
        self.user = User.objects.create(
            username='testuser'
        )
        self.recipe = Recipe.objects.create(
            title='testcategory',
            owner = self.user,
            recipe_text = "Test recipe text"
        )   

    def test_user_model(self):
        user = User.objects.create(
            username='testuser2')

        self.assertEqual(user.username, 'testuser2')
        self.assertEqual(User.objects.count(), 2)

    def test_recipe_model(self):
        recipe = Recipe.objects.create(
            title='test recipe',
            owner = self.user,
            recipe_text = "Test recipe text"
        ) 
        self.assertEqual(Recipe.objects.count(), 2)

    def test_comment_model(self):
        comment = Comment.objects.create(
            comment='test comment',
            comment_owner = self.user,
            recipe = self.recipe
        ) 

        self.assertEqual(Comment.objects.count(), 1)

    def test_rating_model(self):
        rating = Rating.objects.create(
            rating_value= 4,
            rating_owner = self.user,
            recipe = self.recipe
        ) 

        self.assertEqual(Rating.objects.count(), 1)