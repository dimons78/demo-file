# Александр, добрый день!
# Спапасибо за подсказку!
# Задание действительно не сложное.
# По сравнению с ООП, которое никак не доделаю... но, надеюсь, что доделаю! :)

def file_dict(file):
    # recipe = None
    # num_ingredients = 0
    # ingredient_name = None
    # quantity = 0
    # measure = None
    # # cook_book = dict()

    with open(file, encoding='utf-8') as file:
        while True:
            recipe = file.readline().rstrip()
            if not recipe:
                break
            num_ingredients = int(file.readline().rstrip())
            # print(recipe, num_ingredients)

            k1 = []
            for i in range(num_ingredients + 1):
                k = file.readline().rstrip().split()
                if len(k) == 0:
                    break
                # print(k, type(k))
                kDict = dict()
                if k[1] == '|':
                    kDict['ingredient_name'] = k[0]
                    kDict['quantity'] = int(k[2])
                    kDict['measure'] = k[4]
                else:
                    kDict['ingredient_name'] = k[0] + ' ' + k[1]
                    kDict['quantity'] = int(k[3])
                    kDict['measure'] = k[5]
                k1.append(kDict)
                # print(kDict)

            cook_book[recipe] = k1

    # if file.closed:
    #     print('\nOK\n')


cook_book = dict()

file_dict('recipe_book1.txt')
print(cook_book)
print()


def get_shop_list_by_dishes(dishes, person_count):
    for i in range(len(dishes)):

        if dishes[i] in cook_book.keys():
            # print(dishes[i], cook_book.get(dishes[i]))
            # print()
            for j in cook_book.get(dishes[i]):
                # print(j, type(j))
                # print(j['ingredient_name'])
                k2Dict = dict()

                if j['ingredient_name'] in dict_dishes.keys():
                    # Если ингридиент есть уже, то увеличиваем в нём quantity
                    dict_dishes.get(j['ingredient_name'])['quantity'] += j['quantity'] * person_count

                else:
                    k2Dict['quantity'] = j['quantity'] * person_count
                    k2Dict['measure'] = j['measure']
                    measure_quantity = k2Dict
                    dict_dishes[j['ingredient_name']] = measure_quantity


dict_dishes = dict()

get_shop_list_by_dishes(['Омлет', 'Запеченный картофель', 'Утка по-пекински'], 15)

print(dict_dishes)

# print('\nЗаказ:')
# for key, val in dict_dishes.items():
#     print(key)
#     print(val)
