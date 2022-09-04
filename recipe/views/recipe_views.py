from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import View, DetailView, CreateView
from recipe.models.recipe_models import Rating, Recipe, Comment
from recipe.utils.recipe_forms import CommentForm, RecipeForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Avg


class NewsfeedView(LoginRequiredMixin, View):
    template_name = "recipe/home_template.html"
    login_url = reverse_lazy('recipe:login')

    def get(self, request, *args, **kwargs):
        string_query = request.GET.get('string_query')
        recipes = Recipe.objects.all()
        filterd_recipies = self.filter_queryset(recipes, string_query).order_by("-id")
        return render(request, self.template_name, {"recipes": filterd_recipies})

    def filter_queryset(self, queryset, string_query):
        if string_query:
            queryset = queryset.filter(title__icontains=string_query)
        return queryset


class RecipeDetailView(LoginRequiredMixin, DetailView):
    template_name = "recipe/recipe_detail_template.html"
    model = Recipe
    login_url = reverse_lazy('recipe:login')

    def get_context_data(self, *args, **kwargs):
        recipe = self.object.id
        context = super().get_context_data(**kwargs)
        self.add_recipe_details(context,recipe)
        return context
    
    def add_recipe_details(self, context, recipe):

        context['comments'] = Comment.objects.filter(recipe=recipe)
        context['has_rated'] = Rating.objects.filter(rating_owner=self.request.user, recipe=recipe).exists()
        context['rating'] = Rating.objects.filter(recipe=recipe).aggregate(Avg('rating_value'))['rating_value__avg']

    

class RecipeCreateView(LoginRequiredMixin, CreateView):
    template_name = "recipe/recipe_create_template.html"
    success_url = reverse_lazy('recipe:newsfeed')
    login_url = reverse_lazy('recipe:login')
    redirect_field_name = 'recipe:newsfeed'
    form_class = RecipeForm

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.owner = self.request.user
        self.object.save()
        return super().form_valid(form)
    
    def form_invalid(self, form):
        print(form.errors)
        return super().form_invalid(form)

class RecipeUpdateView(LoginRequiredMixin, View):
    template_name = "recipe/recipe_update_template.html"
    login_url = reverse_lazy('recipe:login')
    form_class = RecipeForm

    def get_object(self):
        return Recipe.objects.get(id=self.kwargs['id'])

    def get(self, request, *args, **kwargs):
        form = self.form_class(instance=self.get_object())
        return render(request, self.template_name, {'form': form})
    
    def post(self, request, *args, **kwargs):
        form =  self.form_class(request.POST, request.FILES, instance=self.get_object())
        if form.is_valid():
            form.save()
            return redirect('recipe:recipe_detail', pk=self.get_object().id)
        return render(request, self.template_name, {'form': form})

class CommentCreateView(LoginRequiredMixin, View):
    login_url = reverse_lazy('recipe:login')

    def post(self, request, *args, **kwargs):
        form = CommentForm(request.POST)

        if form.is_valid():
            comment = form.save(commit=False)
            comment.comment_owner = request.user
            comment.save()

            return redirect('recipe:recipe_detail', pk=comment.recipe.pk)
        return redirect('recipe:recipe_detail', pk=request.POST.get('recipe'))
    

class RatingView(LoginRequiredMixin, View):
    login_url = reverse_lazy('recipe:login')

    def get(self, request, *args, **kwargs):
        rating_value = kwargs.get('value')
        recipe = Recipe.objects.get(id=kwargs.get('id'))
        rating = Rating.objects.create(recipe=recipe, rating_value=rating_value, rating_owner=request.user)
        return redirect('recipe:recipe_detail', pk=recipe.pk)
        

class CommentDeleteView(LoginRequiredMixin, View):
    login_url = reverse_lazy('recipe:login')

    def get(self, request, *args, **kwargs):
        comment = Comment.objects.get(id=kwargs.get("id"))
        pk = comment.recipe.pk
        comment.delete()
        return redirect('recipe:recipe_detail', pk=pk)

class RecipeDeleteView(LoginRequiredMixin, View):
    login_url = reverse_lazy('recipe:login')

    def get(self, request, *args, **kwargs):
        recipe = Recipe.objects.get(id=kwargs.get("id"))
        username = recipe.owner.username
        recipe.delete()
        return redirect('recipe:user_profile', username=username)
