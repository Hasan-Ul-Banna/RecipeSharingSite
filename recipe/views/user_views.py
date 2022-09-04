from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.views.generic import View
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy



from recipe.utils.user_forms import CustomUserCreationForm, UserUpdateForm


class UserProfileView(LoginRequiredMixin, View):
    template_name = "user/user_profile_template.html"
    login_url = reverse_lazy('recipe:login')


    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, {"user": request.user})


class LoginView(View):
    template_name = 'user/login_template.html'



    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('recipe:newsfeed')
        form = AuthenticationForm()
        return render(request, self.template_name, {'form':form})

    def post(self, request, *args, **kwargs):
        print(request.POST)
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is None:
            return render(request, self.template_name, {'error': 'Username/password Invalid'})
        login(request, user)

        return redirect('recipe:newsfeed')


class RegistrationView(View):
    template_name = "user/registration_template.html"

    form_class = CustomUserCreationForm
    login_url = reverse_lazy('recipe:login')

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})
    
    def post(self, request, *args, **kwargs):
        print(request.POST)
        form =  self.form_class(request.POST, request.FILES)
        if form.is_valid():
            user=form.save()
            login(request, user)
            return redirect('recipe:newsfeed')
        print(form.errors)
        return render(request, self.template_name, {'form': form})

@login_required(login_url='recipe:login')
def logoutView(request):
    logout(request)
    return redirect('recipe:login')

class UserProfileUpdateView(LoginRequiredMixin, View):
    template_name = "user/user_update_template.html"
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
        return render(request, self.template_name, {'form': form})

