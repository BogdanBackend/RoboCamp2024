from typing import Dict, List, OrderedDict

recipes = {
    "борщ": OrderedDict({
        "інгредієнти": ["буряк", "капуста", "картопля", "морква", "томатна паста", "м'ясо"],
        "кроки": ["Підготувати овочі", "Зварити м'ясо", "Приготувати овочі", "Змішати все та тушкувати"]
    }),
    "паста": OrderedDict({
        "інгредієнти": ["паста", "помідори", "оливкова олія", "пармезан"],
        "кроки": ["Зварити пасту", "Приготувати соус", "Змішати та подавати"]
    })
}

def get_recipe(dish_name: str) -> OrderedDict:
    if dish_name.lower() in recipes:
        return recipes[dish_name.lower()]
    else:
        raise ValueError(f"Рецепт для {dish_name} не знайдено.")

def get_difficulty_level(recipe: Dict[str, List[str]]) -> int:
    try:
        difficulty = len(recipe["інгредієнти"]) + len(recipe["кроки"])
        if difficulty <= 6:          return 1
        elif 7 <= difficulty  <= 10: return 2
        else:                        return 3
    except KeyError:
        raise KeyError("Рецепт має містити ключі 'інгредієнти' та 'кроки'.")

def can_cook(user_ingredients: List[str], recipe: Dict[str, List[str]]) -> bool:
    try:
        return set(recipe["інгредієнти"]).issubset(set(user_ingredients))
    except KeyError:
        raise KeyError("Рецепт має містити ключ 'інгредієнти'.")
