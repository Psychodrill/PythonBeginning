
# Даны два неупорядоченных набора целых чисел (может быть, с повторениями). Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
# На вход подается 2 числа через пробел: n m
# n - кол-во элементов первого множества.
# m - кол-во элементов второго множества.
# Затем подаются элементы каждого множества через пробел в виде строки. 


# firstSequence = '1 3 5 7 9'
# secondSequence = '2 3 4 5'

# firstList= firstSequence.split()
# secondList = secondSequence.split()
# firstSet = set(firstList)
# secondSet = set(secondList)
# resultSet = firstSet.intersection(secondSet)
# resultList = sorted(resultSet)
# result=' '.join(resultList)
# print(result)


# В фермерском хозяйстве в Карелии выращивают чернику. Черника растет на круглой грядке, и кусты черники высажены по окружности грядки. Каждый куст черники имеет урожайность, которая соответствует количеству ягод на этом кусте.

# Урожайность черничных кустов представлена в виде списка arr, где arr[i] - это урожайность (количество ягод) i-го куста.

# В фермерском хозяйстве внедрена система автоматического сбора черники. Эта система состоит из управляющего модуля и нескольких собирающих модулей. Каждый собирающий модуль может собрать ягоды с одного куста и с двух соседних кустов. Собирающий модуль находится перед определенным кустом, и он может выбирать, с какого куста начать сбор ягод.

# Ваша задача - написать программу, которая определит максимальное число ягод, которое может собрать один собирающий модуль за один заход, находясь перед некоторым кустом грядки.

# Входные данные:

# На вход программе подается список arr, где arr[i] (1 ≤ arr[i] ≤ 1000) - урожайность i-го куста черники. Размер списка не превышает 1000 элементов.

# Выходные данные:

# Программа должна вывести одно целое число - максимальное количество ягод, которое может собрать собирающий модуль, находясь перед некоторым кустом грядки.


arr = [5, 8, 6, 4, 9, 2, 7, 3]
resultMaxSum=0
for i in range(0, len(arr)):
    if(i-1<0):
        leftElement=arr[len(arr)-1]
    else:
        leftElement=arr[i-1]
    if(i+1>=len(arr)):
        rightElement = arr[0]
    else:
        rightElement=arr[i+1]
    print(f"{leftElement} {arr[i]} {rightElement}")
    currentSum =leftElement+arr[i]+rightElement
    if(resultMaxSum< currentSum):
        resultMaxSum=currentSum
print(resultMaxSum)