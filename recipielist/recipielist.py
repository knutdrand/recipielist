"""Main module."""
from pathlib import Path
import yaml
from pydantic import BaseModel

class Recipe(BaseModel):
    name: str
    ingredients: list


def get_recipes() -> list[Recipe]:
    base_path = Path(__file__).parent.parent
    recipe_path = base_path /'static/recipies.yaml'
    with open(recipe_path, 'r') as file:
        recipes = yaml.load(file, Loader=yaml.FullLoader)
    return [Recipe.model_validate(r) for r in recipes['recipes']]


def test():
    recipes = get_recipes()
    assert len(recipes) > 3
    for recipe in recipes:
        print(recipe)

