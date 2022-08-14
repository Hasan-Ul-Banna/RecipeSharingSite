from django.urls import path
from recipe.views import NewsfeedView

app_name = 'recipe'

urlpatterns = [
    path('', NewsfeedView.as_view(), name ='newsfeed' )

]