import json

path = 'cleaned_foods.json'

f = open(path)

food_dict = json.load(f)

low_fat = 0
high_fiber = 0
low_glycemic = 0
for food in food_dict:
    good_food = 0
    if food['high fiber'] == 'yes':
        high_fiber += 1
        good_food += 1
    if food['low glycemic index'] == 'yes':
        low_glycemic += 1
        good_food += 1
    if food['low fat'] == 'yes':
        low_fat += 1
        good_food += 1
    if good_food == 3:
        print(f'{food["food"].capitalize()} is a recommended food')
fat_stat = round(low_fat/len(food_dict),4) * 100
fiber_stat = round(high_fiber/len(food_dict),4) * 100
glyc_stat = round(low_glycemic/len(food_dict),4) * 100
str_var = 'of the foods are'
print(f"\n{fat_stat}% or {low_fat} {str_var} low fat\n{fiber_stat}% or {high_fiber} {str_var} high fiber\n{glyc_stat}% or {low_glycemic} {str_var} low glycemic")