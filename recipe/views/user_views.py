from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.views.generic import View
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy



from recipe.utils.user_forms import CustomUserCreationForm, UserUpdateForm

# Create your views here.

class UserProfileView(LoginRequiredMixin, View):
    template_name = "user/user_profile.html"
    login_url = reverse_lazy('recipe:login')


    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, {"user": request.user})

class LoginView(View):
    template_name = 'user/login.html'



    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('recipe:newsfeed')
        form = AuthenticationForm()
        return render(request, self.template_name, {'form':form})

    def post(self, request, *args, **kwargs):
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is None:
            return render(request, self.template_name, {'error': 'Username/password Invalid'})
        login(request, user)

        return redirect('recipe:newsfeed')


class RegistrationView(View):
    template_name = "user/registration.html"

    form_class = CustomUserCreationForm
    login_url = reverse_lazy('recipe:login')


    def get(self, request, *args, **kwargs):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})
    
    def post(self, request, *args, **kwargs):
        print(request.POST)
        form =  self.form_class(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('recipe:newsfeed')
        print(form.errors)
        return render(request, self.template_name, {'form': form})

    # def get(self, request, *args, **kwargs):
    #     if request.user.is_authenticated:
    #         return redirect('recipe:newsfeed')
    #     return render(request, self.template_name)

    # def post(self, request, *args, **kwargs):
    #     username = request.POST.get('username')
    #     password = request.POST.get('password')
    #     email = request.POST.get('email')
    #     first_name = request.POST.get('first_name')
    #     last_name = request.POST.get('last_name')

    #     try:
    #         user = get_user_model().objects.create_user(username=username, password=password,
    #                                         email=email, first_name=first_name, last_name=last_name)
    #         user.set_password(password)
    #         user.save()

    #     except Exception as e:
    #         print(e)
    #         return render(request, self.template_name, {'error': 'Username already exists!'})

    #     if recipe:
    #         login(request, user)
    #         return redirect('recipe:newsfeed')
    #     return render(request, self.template_name, {'error': 'Unknown Error!'})

@login_required(login_url='recipe:login')
def logoutView(request):
    logout(request)
    return redirect('recipe:login')

class UserProfileUpdateView(LoginRequiredMixin, View):
    template_name = "user/user_update.html"
    form_class = UserUpdateForm
    login_url = reverse_lazy('recipe:login')


    def get(self, request, *args, **kwargs):
        form = self.form_class(instance=request.user)
        return render(request, self.template_name, {'form': form})
    
    def post(self, request, *args, **kwargs):
        form =  self.form_class(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('recipe:user_profile', username=request.user.username)
        # print(form.errors)
        return render(request, self.template_name, {'form': form})

