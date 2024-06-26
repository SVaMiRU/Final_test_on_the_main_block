# Final_test_on_the_main_block
Итоговая контрольная работа по основному блоку

## Описание задачи:

Задача заключается в фильтрации массива строк, оставляя только те строки, длина которых меньше или равна 3 символам. Для этого используется функция `filter_short_strings`, которая принимает на вход массив строк и возвращает новый массив, содержащий только отфильтрованные строки.

## Описание решения:

1. Функция `filter_short_strings`:
    * Принимает на вход массив строк `input_array`.
    * Создает пустой массив `output_array` для хранения отфильтрованных строк.
    * Перебирает каждую строку `string` в `input_array`:
        * Проверяет, является ли длина строки `string` меньше или равна 3.
        * Если условие выполняется, добавляет строку `string` в массив `output_array`.
    * Возвращает массив `output_array` с отфильтрованными строками.

2. Основная программа:
    * Создает пустой массив `input_array` для хранения строк, введенных пользователем.
    * Запрашивает у пользователя количество строк (`n`) для ввода.
    * В цикле запрашивает у пользователя `n` строк и добавляет их в массив `input_array`.
    * Вызывает функцию `filter_short_strings` с массивом `input_array` в качестве аргумента и сохраняет результат в переменной `result_array`.
    * Выводит на экран исходный массив `input_array` и отфильтрованный массив `result_array`. 

## Пример:

Входные данные:

* `Введите количество строк: 5`
* `Введите строку: привет`
* `Введите строку: мир`
* `Введите строку: солнце`
* `Введите строку: код`
* `Введите строку: yes`


Выходные данные:

* `Исходный массив строк: ['привет', 'мир', 'солнце', 'код', 'yes']`
* `Новый массив строк (длина <= 3): ['мир', 'код', 'yes']`
