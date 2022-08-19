from django.urls import path
from recipe.views import (NewsfeedView,RecipeDetailView,RecipeCreateView,
    RecipeUpdateView,ReportRecipeCreateView,ReportCommentCreateView,
    CommentCreateView
)   

app_name = 'recipe'

urlpatterns = [
    path('', NewsfeedView.as_view(), name ='newsfeed'),
    path('recipe-detail/<int:pk>/', RecipeDetailView.as_view(), name ='recipe_detail'),
    path('recipe-create/', RecipeCreateView.as_view(), name ='recipe_create'),
    path('recipe-update/<int:id>/', RecipeUpdateView.as_view(), name ='recipe_update'),
    path('recipe-report/<int:id>/', ReportRecipeCreateView.as_view(), name ='recipe_report'),
    path('comment/', CommentCreateView.as_view(), name ='comment_create'),
    path('comment-report/<int:id>/', ReportCommentCreateView.as_view(), name ='comment_report'),
]