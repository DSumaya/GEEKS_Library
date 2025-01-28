from django.shortcuts import render, get_object_or_404
from . import forms, models
from django.views import generic



class RecipeListView(generic.ListView):
    model = models.Recipe
    template_name = 'recipe/recipe_list.html'
    context_object_name = 'recipe_list'

    def get_queryset(self):
        return self.model.objects.all().order_by('-id')



class RecipeDetailView(generic.DetailView):
    model = models.Recipe
    template_name = 'recipes/recipe_detail.html'
    context_object_name = 'recipe_id'

    def get_object(self, **kwargs):
        recipe_id = self.kwargs.get('id')
        return get_object_or_404(models.Recipe, id=recipe_id)




class RecipeCreateView(generic.CreateView):
    model = models.Recipe
    form_class = forms.RecipeForm
    template_name = 'recipes/recipe_create.html'
    success_url = '/recipe_list/'

    def form_valid(self, form):
        print(form.cleaned_data)
        return super(RecipeCreateView, self).form_valid(form=form)



class RecipeDeleteView(generic.DeleteView):
    template_name = 'recipe/confirm_delete.html'
    success_url = '/recipe_list/'
    def get_object(self, **kwargs):
        recipe_id = self.kwargs.get('id')
        return get_object_or_404(models.Recipe, id=recipe_id)



class IngredientCreateView(generic.CreateView):
    model = models.Ingredient
    form_class = forms.IngredientForm
    template_name = 'recipes/ingredient_create.html'
    success_url = '/recipe_list/'

    def form_valid(self, form):
        print(form.cleaned_data)
        return super(IngredientCreateView, self).form_valid(form=form)

