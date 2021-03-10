# Nicolas Campero
# 1856853

class FoodItem:

    def __init__(self, food_name='None', num_fat=0.0, num_carbs=0.0, num_protein=0.0):
        self.name = food_name
        self.fat = num_fat
        self.carbs = num_carbs
        self.protein = num_protein

    def get_calories(self, num_servings):
        # Calorie formula
        calories = ((self.fat * 9) + (self.carbs * 4) + (self.protein * 4)) * num_servings
        return calories

    def print_info(self):
        print('Nutritional information per serving of {}:'.format(self.name))
        print('   Fat: {:.2f} g'.format(self.fat))
        print('   Carbohydrates: {:.2f} g'.format(self.carbs))
        print('   Protein: {:.2f} g'.format(self.protein))

if __name__ == '__main__':
    food1 = FoodItem()

    food_name = input()
    num_fat = float(input())
    num_carbs = float(input())
    num_protein = float(input())
    num_servings = float(input())

    food2 = FoodItem(food_name, num_fat, num_carbs, num_protein)

    food1.print_info()
    print('Number of calories for {:.2f} serving(s): {:.2f}\n'.format(num_servings, food1.get_calories(num_servings)))

    food2.print_info()
    print('Number of calories for {:.2f} serving(s): {:.2f}'.format(num_servings, food2.get_calories(num_servings)))
