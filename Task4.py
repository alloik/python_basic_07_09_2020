"""
Пользователь вводит целое положительное число.
Найдите самую большую цифру в числе.
Для решения используйте цикл while и арифметические операции.
"""
while True:
    n = input("Введите число больше 0: \n")
    if n.isdigit():
        n = int(n)
        break

count = 0
while n and count !=9:
    tmp = n % 10
    if tmp > count:
        count = tmp
    n //= 10

print(count)