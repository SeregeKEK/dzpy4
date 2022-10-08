# Вычислить число c заданной точностью d
from random import random
from random import randint

def Zadacha1():
    number = float(input('Введите число: '))
    count = int(input('Клоичество знаков после запятой: '))
    print(f'{number:.{count}f}')



# Задайте натуральное число N. Напишите программу, 
# которая составит список простых множителей числа N.
def Zadacha2():
    number = int(input('Введите число: '))
    i = 2
    myRange = []
    while i * i <= number:
        while number % i == 0:
            myRange.append(i)
            number = number // i
        i = i + 1
    if number > 1:
        myRange.append(number)
    print(myRange)



# Задайте последовательность чисел. Напишите программу, 
# которая выведет список неповторяющихся элементов исходной последовательности.
def Zadacha3():
    list1 = [randint(0, 10) for _ in range(10)]
    for i in list1:
        list2 = [i for i in list1 if list1.count(i) ==1]
    print(list1)
    print(list2)


# Задана натуральная степень k. Сформировать случайным образом список коэффициентов 
# (значения от 0 до 100) многочлена и записать в файл многочлен степени k.
def Zadacha4():
    import random

    number = int(input("Введите натуральную степень k: "))
    if number > 0:
        with open('test.txt', "w") as file:
            for i in reversed(range(1, number+1)):
                numberOne = random.randint(0,100)
                if numberOne != 0:
                        print(f"{numberOne}*x^{i} +", file=file, end=" ")
            print(f"{numberOne} = 0", file=file)



# Zadacha1()
# Zadacha2()
# Zadacha3()
Zadacha4()
