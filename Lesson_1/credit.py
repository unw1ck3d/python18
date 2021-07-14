# Считаем кредит

name1 = input("Введите имя первого человека: ")

salary1 = input("зп первого: ")

credit = float(input("Введите сумму кредита: "))
period = float(input("Введите срок в месяцах: "))
procent = float(input("Введите процент: "))

pay_per_month = credit / period + (credit / 100 * procent) / 12
print("Ежемесячный платёж составит -", pay_per_month, "рублей")
print(name1, "сможет потратить", float(salary1) - pay_per_month)
