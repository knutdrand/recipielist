"""Console script for recipielist."""
# todo
from cyclopts import App

from recipielist.recipielist import get_recipes
from recipielist.sms_service import send_sms_to_me

app = App()


@app.command()
def list_recipies():
    '''
    This function should just be type hinted with common types,
    and it will run as a command line function
    Simple function

    >>> main_function()

    '''
    for recipe in get_recipes():
        print(recipe.name)

@app.command()
def get_ingredients(recipe_names: list[str], send_sms: bool = False):
    all_recipes = get_recipes()
    all_ingredients = set()
    for recipe in all_recipes:
        if recipe.name in recipe_names:
            all_ingredients.update(recipe.ingredients)
    for ingredient in all_ingredients:
        print(ingredient)
    if send_sms:
        ingreditents = '\n'.join(all_ingredients)
        body = f"Ingredients for {recipe_names}: {ingreditents}"
        send_sms_to_me(body)




def main():
    app()


if __name__ == "__main__":
    main()
