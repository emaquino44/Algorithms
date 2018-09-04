#!/usr/bin/python

import math


def recipe_batches(recipe, ingredients):
  batch = []                        # Empty array for our ingredients
  for ingredient in recipe.keys():  # Grabbing names of the required ingredients in the recipe
    if ingredient not in ingredients:  # If ingredients doesn't have an ingredient from recipe, no batches can be made
      return 0
    else:
       # Adds the number of batches per ingredient(s)
       batch.append(ingredients[ingredient] // recipe[ingredient])

  return min(batch)  # Returns how many batches we can make


if __name__ == '__main__':
  # Change the entries of these dictionaries to test
  # your implementation with different inputs
  recipe = { 'milk': 100, 'butter': 50, 'flour': 5 }
  ingredients = { 'milk': 132, 'butter': 48, 'flour': 51 }
  print("{batches} batches can be made from the available ingredients: {ingredients}.".format(batches=recipe_batches(recipe, ingredients), ingredients=ingredients))
