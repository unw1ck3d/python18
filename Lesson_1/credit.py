# Считаем кредит

name1 = input("Введите имя первого человека: ")
name2 = input("Введите имя второго человека: ")
name3 = input("Введите имя третьего человека: ")

salary1 = input("зп первого: ")
salary2 = input("зп второго: ")
salary3 = input("зп третьего: ")

credit = float(input("Введите сумму кредита: "))
period = float(input("Введите срок в месяцах: "))
procent = float(input("Введите процент: "))

pay_per_month = credit / period + (credit / 100 * procent) / 12
print("Ежемесячный платёж составит -", pay_per_month, "рублей")
print(name1, "сможет потратить", float(salary1) - pay_per_month)
print(name2, "сможет потратить", float(salary2) - pay_per_month)
print(name3, "сможет потратить", float(salary3) - pay_per_month)