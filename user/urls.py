from django.urls import path
from user.views import UserView

app_name = 'user'

urlpatterns = [
    path('profile/', UserView.as_view(), name ='userprofile'),

]