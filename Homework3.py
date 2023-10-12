# Требуется вычислить, сколько раз встречается некоторое число k в массиве list_1.

# Найдите количество и выведите его.

# list_1 = [1, 4, 3, 7, 8, 9, 2]
# k = 3
# count =0
# for i in range(0,len(list_1)):
#     if (list_1[i]==k):
#         count+=1
# print(count)

#Требуется найти в массиве list_1 самый близкий по величине элемент к заданному числу k и вывести его.
list_1 = [1, 4, 3, 7, 8, 9, 2]
k = 8

minDeltaIndex =0
minDelta=abs(list_1[minDeltaIndex]-k)

for i in range(1,len(list_1)):
    if (abs(k-list_1[i])<minDelta):
        minDelta= abs(k-list_1[i])
        minDeltaIndex=i
print(list_1[minDeltaIndex])
print(abs(list_1[minDeltaIndex]-k))

