num1  = int(input("Введите Первое число: "))
num2  = int(input("Введите Второе число: "))

temp = num1
num1 = num2
num2 = temp
print("после обмена:")
print("Первое число",num1)
print("Второе число",num2)