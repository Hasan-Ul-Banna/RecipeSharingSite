from django.test import SimpleTestCase
from django.urls import reverse, resolve

from recipe.views.recipe_views import (NewsfeedView, RecipeDetailView, RecipeCreateView, RecipeUpdateView, CommentCreateView,
 RatingView, CommentDeleteView, RecipeDeleteView)

from recipe.views.user_views import (UserProfileView, LoginView, 
 RegistrationView, logoutView, UserProfileUpdateView)

class TestUrls(SimpleTestCase):

    def test_newsfeed_url_is_resolved(self):
        url = reverse('recipe:newsfeed')
        self.assertEquals(resolve(url).func.view_class, NewsfeedView)
    
    def test_recipe_detail_url_is_resolved(self):
        url = reverse('recipe:recipe_detail', args=[10])
        self.assertEquals(resolve(url).func.view_class, RecipeDetailView)

    def test_recipe_create_url_is_resolved(self):
        url = reverse('recipe:recipe_create')
        self.assertEquals(resolve(url).func.view_class, RecipeCreateView)

    def test_recipe_update_url_is_resolved(self):
        url = reverse('recipe:recipe_update', args=[10])
        self.assertEquals(resolve(url).func.view_class, RecipeUpdateView)

    def test_comment_create_url_is_resolved(self):
        url = reverse('recipe:comment_create')
        self.assertEquals(resolve(url).func.view_class, CommentCreateView)

    def test_rating_post_url_is_resolved(self):
        url = reverse('recipe:rating_post', args=[10, 11])
        self.assertEquals(resolve(url).func.view_class, RatingView)

    def test_comment_delete_url_is_resolved(self):
        url = reverse('recipe:comment_delete', args=[10])
        self.assertEquals(resolve(url).func.view_class, CommentDeleteView)

    def test_recipe_delete_url_is_resolved(self):
        url = reverse('recipe:recipe_delete', args=[10])
        self.assertEquals(resolve(url).func.view_class, RecipeDeleteView)

    def test_user_profile_url_is_resolved(self):
        url = reverse('recipe:user_profile', args=['slug'])
        self.assertEquals(resolve(url).func.view_class, UserProfileView)

    def test_login_url_is_resolved(self):
        url = reverse('recipe:login')
        self.assertEquals(resolve(url).func.view_class, LoginView)

    def test_registration_url_is_resolved(self):
        url = reverse('recipe:registration')
        self.assertEquals(resolve(url).func.view_class, RegistrationView)

    def test_user_profile_update_url_is_resolved(self):
        url = reverse('recipe:user_profile_update', args=['slug'])
        self.assertEquals(resolve(url).func.view_class, UserProfileUpdateView)

    def test_logout_url_is_resolved(self):
        url = reverse('recipe:logout')
        self.assertEquals(resolve(url).func, logoutView)
