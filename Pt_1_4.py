num = int(input("Введите число от 10 до 20: "))
while num < 10:
    print("Число меньше требуемого диапазона")
    num = int(input("Введите число от 10 до 20: "))
while num > 20:
    print("Число больше требуемого диапазона")
    num = int(input("Введите число от 10 до 20: "))
else:
    print("Спасибо")