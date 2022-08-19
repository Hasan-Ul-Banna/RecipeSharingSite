from django.urls import path
from user.views import UserProfileView,LoginView,RegistrationView,logoutView,UserProfileUpdateView,ReportUserCreateView

app_name = 'user'

urlpatterns = [
    path('profile/<str:username>/', UserProfileView.as_view(), name ='user_profile'),
    path('login/', LoginView.as_view(), name ='login'),
    path('registration/', RegistrationView.as_view(), name ='registration'),
    path('user-profile-update/<str:username>/', UserProfileUpdateView.as_view(), name ='user_profile_update'),
    path('user-report/<str:username>/', ReportUserCreateView.as_view(), name ='user_report'),
    path('logout/', logoutView, name='logout'),

]