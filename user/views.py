from django.shortcuts import render
from django.views.generic import View

# Create your views here.

class UserView(View):
    template_name = "user/userprofile.html"

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)
