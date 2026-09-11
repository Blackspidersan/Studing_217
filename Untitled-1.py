id = int(input("Введите количество строк"))
for i in range(1, id + 1):
    name = str(input("Введите имя"))
    town = str(input("Из какого вы города?"))
    age = int(input("Ваш возраст?"))
    height = int(input("Ваш рост?"))
    weight = int(input("Ваш вес?"))
    print(i, name, town, age, height, weight)

