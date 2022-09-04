from django.urls import path
from recipe.views.recipe_views import (NewsfeedView,RecipeDetailView,RecipeCreateView,
    RecipeUpdateView, CommentCreateView, CommentDeleteView, RecipeDeleteView, RatingView
) 
from recipe.views.user_views import UserProfileView,LoginView,RegistrationView,logoutView,UserProfileUpdateView

app_name = 'recipe'

urlpatterns = [
    path('', NewsfeedView.as_view(), name ='newsfeed'),
    path('recipe-detail/<int:pk>/', RecipeDetailView.as_view(), name ='recipe_detail'),
    path('recipe-create/', RecipeCreateView.as_view(), name ='recipe_create'),
    path('recipe-update/<int:id>/', RecipeUpdateView.as_view(), name ='recipe_update'),
    path('comment/', CommentCreateView.as_view(), name ='comment_create'),
    path('rating/<int:value>/<int:id>/', RatingView.as_view(), name ='rating_post'),
    path('comment-delete/<int:id>/', CommentDeleteView.as_view(), name ='comment_delete'),
    path('recipe-delete/<int:id>/', RecipeDeleteView.as_view(), name ='recipe_delete'),
    path('profile/<str:username>/', UserProfileView.as_view(), name ='user_profile'),
    path('login/', LoginView.as_view(), name ='login'),
    path('registration/', RegistrationView.as_view(), name ='registration'),
    path('user-profile-update/<str:username>/', UserProfileUpdateView.as_view(), name ='user_profile_update'),
    path('logout/', logoutView, name='logout'),
]