"""
Запросите у пользователя значения выручки и издержек фирмы.
Определите, с каким финансовым результатом работает фирма
(прибыль — выручка больше издержек, или убыток — издержки больше выручки).
Выведите соответствующее сообщение.
Если фирма отработала с прибылью, вычислите рентабельность выручки
(соотношение прибыли к выручке).
Далее запросите численность сотрудников фирмы и
определите прибыль фирмы в расчете на одного сотрудника.
"""
earnings = input("Введите Вашу прибыль за месяц: \n")
while True:
    earnings.isdigit()
    earnings = int(earnings)
    break

costs = input('Введите количество издержек за месяц: \n')
while True:
    costs.isdigit()
    costs = int(costs)
    break

profit = earnings - costs
profit = float(profit)
loss = costs - earnings
loss = float(loss)
profitability = profit / earnings
if earnings > costs:
    print("Ваша прибыль = {:.2f} р.".format(profit))
    print('Рентабельность вашей выручки = {:.2f}'.format(profitability))
    staff = input('Введите количество сотрудников: \n')
    while True:
        staff.isdigit()
        staff = int(staff)
        break
    profit_staff = profit / staff
    profit_staff = float(profit_staff)
    print('Прибыль фирмы в расчете на одного сотрудника = {:.2f} р.'.format(profit_staff))
else:
    print('Ваш убыток = {:.2f} р.'.format(loss))