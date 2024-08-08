from recipe_module import get_recipe, get_difficulty_level, can_cook

def main():
    try:
        recipe  = get_recipe("Борщ")
        print(f"Рецепт для борща: {recipe}")
        складність = get_difficulty_level(recipe)
        print(f"Рівень складності: {складність}")
        ingradients = ["буряк", "капуста", "картопля", "морква", "томатна паста", "м'ясо"]
        print(f"Можна приготувати: {can_cook(ingradients, recipe)}")

    except ValueError as e: print(e)
    except KeyError as e:   print(e)

if __name__ == "__main__":
    main()
