# На столе лежат n монеток. Некоторые из монеток лежат вверх решкой, а некоторые – гербом. Ваша задача - определить минимальное количество монеток, которые нужно перевернуть, чтобы все монетки лежали одной и той же стороной вверх.

# Входные данные:

# На вход программе подается список coins, где coins[i] равно 0, если i-я монетка лежит гербом вверх, и равно 1, если i-я монетка лежит решкой вверх. Размер списка не превышает 1000 элементов.

# Выходные данные:

# Программа должна вывести одно целое число - минимальное количество монеток, которые нужно перевернуть.

import random


# coinsList = [random.randrange(0,2,1) for i in range(1, 1001)]

# print(coinsList)

# obverse=0
# reverse=0

# print(len(coinsList))
# for i in range(len(coinsList)):
#     if(coinsList[i]==0):
#         obverse+=1
#     else:
#         reverse+=1

# if(obverse< reverse):
#     print(f"obverse is less than reverse and is {obverse}")
# else:
#     print(f"reverse is less than obverse and is {reverse}")
    
#Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N.

# n = int(input())
# i=0
# while pow(2,i)<=n:
#     print (pow(2,i))
#     i+=1

# Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница. Петя помогает Кате по математике.
# Он задумывает два натуральных числа X и Y (X,Y≤1000), а Катя должна их отгадать. Для этого Петя делает две подсказки. Он называет сумму этих чисел S и их произведение P. Помогите Кате отгадать задуманные Петей числа.
# Примечание: числа S и P задавать не нужно, они будут передаваться в тестах. В результате вы должны вывести все возможные варианты чисел X и Y через пробел.

x=int(input())
y = int(input())
#x = random.randrange(0,1001,1)
#y = random.randrange(0,1001,1)

options = range(1001)


# for i in options:
#     x=i
#     y=numbersSum-x
#     if(x*y ==numbersProduct):
#         print(x, y)


for i in range(1001):
    s=i
    p=x-s
    if(s*p ==y):
        print(s, p)