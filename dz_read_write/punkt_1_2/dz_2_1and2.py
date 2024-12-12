cook_book = {} # словарь - название : рецепт(список словарей)

with open ('recept.txt', 'r', encoding='UTF-8') as f:
  for line in f:
    name = line.strip() # имя блюда
    ingredients_count = int(f.readline().strip()) # количество ингредиентов
    ingredients = []
    for i in range(ingredients_count): # какие ингредиенты
      ingredient = f.readline().strip().split('|') # читаем строку и избавляемся от пробелов и разделителей, преобразуем в список
      ingredients.append({'ingredient_name': ingredient[0], 'quantity': int(ingredient[1]), 'measure': ingredient[2]}) # разносим ингридиенты и в список
    cook_book[name] = ingredients # получаем словарь со списоком словарей
    f.readline() # пропускаем пустую строку

def get_shop_list_by_dishes(names, person_count): # функция, расчитывает потребность по списку блюд и количеству персон
  list_r = {}
  for blyudo in names: # проходимся по списку блюд введенному пользователем
    for ingredient in cook_book[blyudo]: # забираем ингридиенты - из списка словарей
      if ingredient['ingredient_name'] in list_r:
        list_r[ingredient['ingredient_name']]['quantity'] += ingredient['quantity'] * person_count 
      else:
        list_r[ingredient['ingredient_name']] = {'measure': ingredient['measure'], 'quantity': ingredient['quantity'] * person_count}
  return list_r 

def print_list(list1):
  for ingredient in list1: # проходимся по ингридиентам
    print(f'{ingredient}: {list1[ingredient]["measure"]} {list1[ingredient]["quantity"]}')

def create_list():
  people_count = int(input('Введите количество человек: '))
  eats= (input('Введите блюда: ').split(', '))
  people_list = get_shop_list_by_dishes(eats, people_count)
  print_list(people_list)


create_list()