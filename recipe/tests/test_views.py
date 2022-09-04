from django.test import TestCase, Client
from django.urls import reverse
from recipe.models.recipe_models import Recipe
from recipe.models.user_models import User



class TestViews(TestCase):

    def setUp(self):
            self.client = Client()
            self.user = User.objects.create_user(username='test')
            self.user.set_password('test')
            self.user.save()
            self.client.force_login(self.user)
            self.recipe = Recipe.objects.create(title='test_recipe', recipe_text='test recipe text', owner=self.user)

    def test_newsfeed_view(self):
        url = reverse("recipe:newsfeed")
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, "recipe/home_template.html")

    def test_recipe_detail_view(self):
        url = reverse("recipe:recipe_detail", args=[self.recipe.id])
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response,  "recipe/recipe_detail_template.html")

    def test_recipe_create_view(self):
        url = reverse("recipe:recipe_create")
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response,  "recipe/recipe_create_template.html")

    def test_recipe_update_view(self):
        url = reverse("recipe:recipe_update", args=[self.recipe.id])
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response,  "recipe/recipe_update_template.html")
    
    def test_user_profile_view(self):
        url = reverse("recipe:user_profile", args=[self.user.username])
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, "user/user_profile_template.html")

    def test_user_profile_update_view(self):
        url = reverse("recipe:user_profile_update", args=[self.user.username])
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, "user/user_update_template.html")

