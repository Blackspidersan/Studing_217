import random

variants = [1, 2, 3, 4, 5, 6]
first_yours = random.choice(variants)
second_yours = random.choice(variants)
third_yours = random.choice(variants)
fourth_yours = random.choice(variants)
fifth_yours = random.choice(variants)
sixth_yours = random.choice(variants)
print(
    f"Первый кубик: {first_yours}, второй кубик: {second_yours}, третий кубик: {third_yours}\n"
    f"Четвертый кубик: {fourth_yours}, пятый кубик: {fifth_yours}, шестой кубик: {sixth_yours}"
)
first_pc = random.choice(variants)
second_pc = random.choice(variants)
third_pc = random.choice(variants)
fourth_pc = random.choice(variants)
fifth_pc = random.choice(variants)
sixth_pc = random.choice(variants)
combination = [
    first_pc,
    second_pc,
    third_pc,
    fourth_pc,
    fifth_pc,
    sixth_pc,
    first_yours,
    second_yours,
    third_yours,
    fourth_yours,
    fifth_yours,
    sixth_yours,
]
n = int(input("Ваша ставка(количество):"))
m = int(input("Ваша ставка(номинал):"))
line = ["Согласен", "Не верю"]
count = 0
while count == 0:
    if n <= 12 and m <= 6:
        stroka = random.choice(line)
        print(stroka)
        if stroka == "Не верю":
            if combination.count(m) >= n:
                print("Вы победили")
                print(
                    f"Первый кубик: {first_pc}, второй кубик: {second_pc}, третий кубик: {third_pc}\n"
                    f"Четвертый кубик: {fourth_pc}, пятый кубик: {fifth_pc}, шестой кубик: {sixth_pc}"
                )
                count += 1

            else:
                print("Вы проиграли")
                print(
                    f"Первый кубик: {first_pc}, второй кубик: {second_pc}, третий кубик: {third_pc}\n"
                    f"Четвертый кубик: {fourth_pc}, пятый кубик: {fifth_pc}, шестой кубик: {sixth_pc}"
                )
                count += 1

        elif stroka == "Согласен":
            n_plus = int(input("На сколько хотите увеличить количество?"))
            m_plus = int(input("На сколько хотите увеличеть номинал?"))
            n = n + n_plus
            m = m + m_plus
    else:
        print("Ваша ставка некорректна")
        break
print("Теперь компьютер делает ставку")
count_2 = 0
n_pc = random.choice([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
m_pc = random.choice(variants)
print(f"{n_pc} число, {m_pc} номинал")
while count_2 == 0:
    if n_pc <= 12 and m_pc <= 6:
        stroka_2 = input("Согласны ли вы?")
        if stroka_2 == "Не верю":
            if combination.count(m_pc) >= n_pc:
                print("Вы проиграли")
                print(
                    f"Первый кубик: {first_pc}, второй кубик: {second_pc}, третий кубик: {third_pc}\n"
                    f"Четвертый кубик: {fourth_pc}, пятый кубик: {fifth_pc}, шестой кубик: {sixth_pc}"
                )
                count_2 += 1
            else:
                print("Вы победили")
                print(
                    f"Первый кубик: {first_pc}, второй кубик: {second_pc}, третий кубик: {third_pc}\n"
                    f"Четвертый кубик: {fourth_pc}, пятый кубик: {fifth_pc}, шестой кубик: {sixth_pc}"
                )
                count_2 += 1
        elif stroka_2 == "Согласен":
            n_plus_2 = random.choice(range(1, 13))
            m_plus_2 = random.choice(range(1, 7))
            n_pc = n_pc + n_plus_2
            m_pc = m_pc + m_plus_2
    else:
        print("Ставка некорректна")
