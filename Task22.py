# Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с повторениями). 
# Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
# Пользователь вводит 2 числа. n - кол-во элементов первого множества. m - кол-во элементов второго множества. Затем пользователь вводит сами элементы множеств.
# 11 6
# 2 4 6 8 10 12 10 8 6 4 2
# 3 6 9 12 15 18
# 6 12

n = int(input('Введите кол-во элементов первого множества: '))
print('Введите множество: ')
array1 = [int(i) for i in input().split()]
m = int(input('Введите кол-во элементов второго множества: '))
print('Введите множество: ')
array2 = [int(i) for i in input().split()]
print(f'Набор n:', array1)
print(f'Набор m:', array2)

result = set(array1) & set(array2)
if (len(result) > 0):
    print('Совпадения:', result)
else:
    print('Нет совпадений!')