# -*- coding: utf-8 -*-

def filter_short_strings(input_array):
    output_array = []
    for string in input_array:
        if len(string) <= 3:
            output_array.append(string)
    return output_array

# Ввод массива строк с клавиатуры
input_array = []
n = int(input("Введите количество строк: "))
for i in range(n):
    string = input("Введите строку: ")
    input_array.append(string)

# Вызов функции filter_short_strings для фильтрации строк
result_array = filter_short_strings(input_array)
