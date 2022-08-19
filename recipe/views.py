from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import View, DetailView, CreateView, UpdateView
from recipe.models import Recipe, Comment
from recipe.forms import CommentForm
from django.contrib.auth.mixins import LoginRequiredMixin


class NewsfeedView(LoginRequiredMixin, View):
    template_name = "recipe/home.html"
    login_url = reverse_lazy('user:login')

    def get(self, request, *args, **kwargs):
        recipes = Recipe.objects.all()
        return render(request, self.template_name, {"recipes": recipes})


class RecipeDetailView(LoginRequiredMixin, DetailView):
    template_name = "recipe/recipe_detail.html"
    model = Recipe
    # redirect_field_name = 'user:login'
    login_url = reverse_lazy('user:login')

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comments'] = Comment.objects.filter(recipe=self.object.id)
        return context
    

class RecipeCreateView(LoginRequiredMixin, CreateView):
    template_name = "recipe/recipe_create.html"
    login_url = reverse_lazy('user:login')

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)

class RecipeUpdateView(LoginRequiredMixin, UpdateView):
    template_name = "recipe/recipe_update.html"
    login_url = reverse_lazy('user:login')

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)

class ReportRecipeCreateView(LoginRequiredMixin, CreateView):
    template_name = "recipe/recipe_report.html"
    login_url = reverse_lazy('user:login')

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)

class ReportCommentCreateView(LoginRequiredMixin, CreateView):
    template_name = "recipe/comment_report.html"
    login_url = reverse_lazy('user:login')

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)

class CommentCreateView(LoginRequiredMixin, View):
    login_url = reverse_lazy('user:login')

    def post(self, request, *args, **kwargs):
        form = CommentForm(request.POST)

        if form.is_valid():
            comment = form.save(commit=False)
            comment.comment_owner = request.user
            comment.save()

            return redirect('recipe:recipe_detail', pk=comment.recipe.pk)
        print(form.errors)
        return redirect('recipe:recipe_detail', pk=request.POST.get('recipe'))
