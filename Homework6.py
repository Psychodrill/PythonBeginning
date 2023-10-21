# Вывести индексы массива (списка), значения элементов которых принадлежат заданному диапазону (т.е. не меньше заданного минимума и не больше заданного максимума).
# На вход подается список с элементамиlist_1 и границы диапазона в виде чисел min_number, max_number.

# list_1 = [-5, 9, 0, 3, -1, -2, 1, 4, -2, 10, 2, 0, -9, 8, 10, -9, 0, -5, -5, 7]
# min_number = 0
# max_number = 10

# for i in range(0, len(list_1)):
#     if(min_number<=list_1[i] <=max_number):
#         print(i) 


# Заполните массив элементами арифметической прогрессии. Её первый элемент a1, 
#разность d и количество элементов n будет задано автоматически. Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.

a1 = 2
d = 3
n = 4

def ArithmeticProgression(a, d, n, i=1):
    
    result= a + (i-1) * d

    if(n==i):
        print(result)
        return result
    else:
        print(result)
        i+=1
        return ArithmeticProgression(a,d,n,i)
   
ArithmeticProgression(a1,d,n)