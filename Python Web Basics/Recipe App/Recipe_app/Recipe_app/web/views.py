

from django.shortcuts import render, redirect

from Recipe_app.web.forms import CreateRecipeForm, EditRecipeForm, DeleteRecipeForm
from Recipe_app.web.models import Recipe


def index(request):
    recipes = Recipe.objects.all()

    context = {
        'recipes': recipes,
    }

    return render(request, 'index.html', context)


def create_recipe(request):
    if request.method == "POST":
        form = CreateRecipeForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = CreateRecipeForm(request.FILES)
    context = {
        'form': form,
    }
    return render(request, 'create.html', context)


def edit_recipe(request, pk):
    recipe = Recipe.objects.get(pk=pk)
    if request.method == "POST":
        form = EditRecipeForm(request.POST, request.FILES, instance=recipe)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = EditRecipeForm(request.FILES, instance=recipe)
    context = {
        'form': form,
        'recipe': recipe,
    }
    return render(request, 'edit.html', context)


def details_recipe(request, pk):
    recipe = Recipe.objects \
        .filter(pk=pk) \
        .get()
    splitter = recipe.ingredients.split(', ')
    context = {
        'recipe': recipe,
        'splitter': splitter,
    }
    return render(request, 'details.html', context)


def delete_recipe(request, pk):
    recipe = Recipe.objects.get(pk=pk)
    if request.method == 'POST':
        form = DeleteRecipeForm(request.POST, request.FILES, instance=recipe)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = DeleteRecipeForm(instance=recipe)
    context = {
        'form': form,
        'recipe': recipe,
    }
    return render(request, 'delete.html', context)
