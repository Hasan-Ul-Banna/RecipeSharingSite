from django.shortcuts import render
from django.views.generic import View

# Create your views here.

class NewsfeedView(View):
    template_name = "recipe/home.html"

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)
