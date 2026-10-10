text = input("Введите текст:")
massive = text.split()
count = 0
for i in massive:
    clear_i = i.lower().replace(" ", "")
    if clear_i == clear_i[::-1] and len(clear_i) > 1:
        print(f"Полиндром: {clear_i}")
        count = count + 1

if count > 0:
    print(f"Количество полиндромов: {count}")
else:
    print("Нет полиндромов")
