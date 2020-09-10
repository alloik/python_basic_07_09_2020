"""
Узнайте у пользователя число n.
Найдите сумму чисел n + nn + nnn.
Например, пользователь ввёл число 3.
Считаем 3 + 33 + 333 = 369
"""
while True:
    number = input("Введите число n: \n")
    if number.isdigit():
        break
n2 = number + number
n2 = int(n2)
n3 = number + number + number
n3 = int(n3)
number = int(number)
summ = number + n2 + n3
summ = str(summ)
print("Сумма чисел n + n + nnn = " + summ)