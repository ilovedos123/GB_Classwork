# Напишите программу, в которой пользователь будет задавать две строки,
# а программа - определять количество вхождений одной строки в другой.
string_1 = input('Введите строку 1 : ')
string_2 = input('Введите строку 2 : ')
result = string_1.count(string_2) # функция "count" - количество вхождений одной строки в другую
print(result)