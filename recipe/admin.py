from django.contrib import admin
from recipe.models import Ingredient, Recipe, Rating, Comment, ReportRecipe, ReportComment


admin.site.register(Ingredient)
admin.site.register(Recipe)
admin.site.register(Rating)
admin.site.register(Comment)
admin.site.register(ReportRecipe)
admin.site.register(ReportComment)


# Register your models here.
