from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.views.generic import View,UpdateView,CreateView
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import get_user_model


# Create your views here.

class UserProfileView(View):
    template_name = "user/user_profile.html"

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

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('recipe:newsfeed')
        return render(request, self.template_name)

    def post(self, request, *args, **kwargs):
        username = request.POST.get('username')
        password = request.POST.get('password')
        email = request.POST.get('email')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')

        try:
            print(password)
            user = get_user_model().objects.create_user(username=username, password=password,
                                            email=email, first_name=first_name, last_name=last_name)
            user.set_password(password)
            user.save()

        except Exception as e:
            print(e)
            return render(request, self.template_name, {'error': 'Username already exists!'})

        if user:
            login(request, user)
            return redirect('recipe:newsfeed')
        return render(request, self.template_name, {'error': 'Unknown Error!'})

@login_required(login_url='user:login')
def logoutView(request):
    logout(request)
    return redirect('user:login')

class UserProfileUpdateView(UpdateView):
    template_name = "user/user_update.html"

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)


class ReportUserCreateView(CreateView):
    template_name = "user/user_report.html"

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)