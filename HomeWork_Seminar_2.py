# Задача 1. Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# Пример:
# - 6782 -> 23
# - 0,56 -> 11


def sum_numbers(number):
    sum = 0
    for i in range(len(number)):
        if number[i].isdigit():
            sum += int(number[i])
    return sum


user_number = input('Введите число: ')
print(f'Сумма чисел в числе {user_number} ровна {sum_numbers(user_number)}')

# Задача 2. Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
# Пример:
# - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

def factorial(number: int):
    sum = 1
    for i in range (1, number + 1):
        sum *= i
        print(sum, end=' ')

user_number = int(input('Введите число: '))
factorial(user_number)

# Задача 3. Задайте список из n чисел последовательности $(1+\frac 1 n)^n$ и выведите на экран их сумму.
# Пример:
# - Для n = 6: {1: 4, 2: 7, 3: 10, 4: 13, 5: 16, 6: 19}

def mathematic(number: int):
    sum = 0
    for i in range(1, number + 1):
        sum = round((1 + (1 / i)) ** i, 3)
        print(sum, end=' ')


user_number = int(input('Введите число: '))
mathematic(user_number)

# Задача 4. Задайте список из N элементов, заполненных числами из промежутка [-N, N]. Найдите произведение элементов
#  на указанных позициях. Позиции хранятся в файле file.txt в  одной строке одно число.

num = int(input('Введите число N:  '))
col = list(range(-num, num + 1))
print(col)
data = open('file.txt', 'w')
for i in range(num*2+1):
    data.writelines(f'{i}\n')
data.close()
data = open('file.txt', 'r')
for e in data:
   print(e)
data.close()

# Задача 5. Реализуйте алгоритм перемешивания списка.

from random import shuffle

def fill_array(length):
    array = []
    for i in range(1, length + 1):
        array.append(i)
    return array


user_number = int(input('Введите длинну массива: '))
array = fill_array(user_number)
print(f'Начальный массив ----> {array} <-----')
shuffle(array)
print(f'Сортированный массив ----> {array} <-----')