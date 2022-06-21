# Уважаемые проверяющие!
# Снова прошу прощения!

# К настоящему моменту успел сделать лишь 1 из 3-х заданий по теме "Открытие и чтение файла"!
# Направляю в целях выиграть время для доработки данного ДЗ...


def file_dict(file):
    recipe = None
    num_ingredients = 0
    ingredient_name = None
    quantity = 0
    measure = None
    cook_book = dict()

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

        print(cook_book)

    if file.closed:
        print('\nOK')


file_dict('recipe_book.txt')
