#!/usr/bin/python

import math

def recipe_batches(recipe, ingredients):
  batches = {}

  for ingredient in list(recipe.keys()):
    if ingredient not in list(ingredients.keys()):
      return 0
  
  for ingredient in ingredients:
    batches[ingredient] = ingredients[ingredient] // recipe[ingredient]

  min_batches = batches[ingredient]
  for ingredient in batches:
    if batches[ingredient] < min_batches:
      min_batches = batches[ingredient]
      
  return min_batches

if __name__ == '__main__':
  # Change the entries of these dictionaries to test 
  # your implementation with different inputs
  recipe = { 'milk': 100, 'butter': 50, 'flour': 5 }
  ingredients = { 'milk': 132, 'butter': 48, 'flour': 51 }
  print("{batches} batches can be made from the available ingredients: {ingredients}.".format(batches=recipe_batches(recipe, ingredients), ingredients=ingredients))