# Урок 1. Ввод-Вывод, операторы ветвления
# Задача 2: Найдите сумму цифр трехзначного числа.
#
# *Пример:*
#
# 123 -> 6 (1 + 2 + 3)
# 100 -> 1 (1 + 0 + 0) |

# a = input('Введите число: ')
# print(int(a) // 100 + int(a) // 10 % 10 + int(a) % 10)
# print(int(a[0]) + int(a[1]) + int(a[2]))
# answer = 0
# for i in a:
#     answer += int(i)
# print(answer)

# Задача 4: Петя, Катя и Сережа делают из бумаги журавликов. Вместе они сделали S журавликов.
# Сколько журавликов сделал каждый ребенок, если известно, что Петя и Сережа сделали одинаковое
# количество журавликов, а Катя сделала в два раза больше журавликов, чем Петя и Сережа вместе?
#
# *Пример:*
#
# 6 -> 1  4  1
# 24 -> 4  16  4
#     60 -> 10  40  10
#
# count = int(input('Введите число готовых журавликов: '))
# # kate = s * 0.66
# # boy = (s - kate) / 2
# # print(round(boy), round(kate), round(boy))
#
# kate = count / 3 * 2
# boy = (count - kate) / 2
# print(int(boy), int(kate), int(boy))
#



# Задача 6: Вы пользуетесь общественным транспортом? Вероятно, вы расплачивались за проезд и получали билет
# с номером. Счастливым билетом называют такой билет с шестизначным номером, где сумма первых трех цифр
# равна сумме последних трех. Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6.
# Вам требуется написать программу, которая проверяет счастливость билета.
#
# *Пример:*
#
# 385916 -> yes
# 123456 -> no

# a = input('Введете шестизначное число: ')
# d = int(a[0]) + int(a[1]) + int(a[2])
# n = int(a[3]) + int(a[4]) + int(a[5])
# if d == n:
#     print('yes')
# else:
#     print('no')


# Задача 8: Требуется определить, можно ли от шоколадки размером n × m долек отломить k долек,
# если разрешается сделать один разлом по прямой между дольками
# (то есть разломить шоколадку на два прямоугольника).
#
# *Пример:*
#
# 3 2 4 -> yes
# 3 2 1 -> no

n = int(input('Введите кол-во квадратиков в длину шоколадки'))
m = int(input('Введите кол-во квадратиков в ширину шоколадки'))
k = int(input('Введите кол-во квадратиков, которые хотите отломить'))
if k % n == 0 or k % m == 0:
    print('yes')
else:
    print('no')



Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом.
Определите минимальное число монеток, которые нужно перевернуть,
чтобы все монетки были повернуты вверх одной и той же стороной.
Выведите минимальное количество монет, которые нужно перевернуть

Задача 12: Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница.
Петя помогает Кате по математике. Он задумывает два натуральных числа X и Y (X,Y≤1000),
а Катя должна их отгадать. Для этого Петя делает две подсказки. Он называет сумму этих чисел S и их
произведение P. Помогите Кате отгадать задуманные Петей числа.

Задача 14: Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N.