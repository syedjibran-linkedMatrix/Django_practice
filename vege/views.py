from django.shortcuts import render, redirect, get_object_or_404
from .models import Recipe

def recipe_view(request):
    if request.method == 'POST':
        recipe_name = request.POST.get('recipe_name')
        recipe_description = request.POST.get('recipe_description')
        recipe_image = request.FILES.get('recipe_image')

        # Create a new Recipe instance
        recipe = Recipe(
            name=recipe_name,
            description=recipe_description,
            image=recipe_image
        )
        recipe.save()  # Save the instance to the database

        return redirect('recipes')  # Redirect to the recipe list

    recipes = Recipe.objects.all()  # Fetch all submitted recipes
    return render(request, 'receipes.html', {'recipes': recipes})

def delete_recipe(request, recipe_id):
    recipe = get_object_or_404(Recipe, id=recipe_id)
    recipe.delete()
    return redirect('recipes')  # Redirect to the recipes page after deletion
