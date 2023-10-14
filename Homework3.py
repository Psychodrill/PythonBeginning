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
# list_1 = [1, 4, 3, 7, 8, 9, 2]
# k = 8

# minDeltaIndex =0
# minDelta=abs(list_1[minDeltaIndex]-k)

# for i in range(1,len(list_1)):
#     if (abs(k-list_1[i])<minDelta):
#         minDelta= abs(k-list_1[i])
#         minDeltaIndex=i
# print(list_1[minDeltaIndex])
# print(abs(list_1[minDeltaIndex]-k))

# В настольной игре Скрабл (Scrabble) каждая буква имеет определенную ценность.

# В случае с английским алфавитом очки распределяются так:

# A, E, I, O, U, L, N, S, T, R – 1 очко;
# D, G – 2 очка;
# B, C, M, P – 3 очка;
# F, H, V, W, Y – 4 очка;
# K – 5 очков;
# J, X – 8 очков;
# Q, Z – 10 очков.

# А русские буквы оцениваются так:
# А, В, Е, И, Н, О, Р, С, Т – 1 очко;
# Д, К, Л, М, П, У – 2 очка;
# Б, Г, Ё, Ь, Я – 3 очка;
# Й, Ы – 4 очка;
# Ж, З, Х, Ц, Ч – 5 очков;
# Ш, Э, Ю – 8 очков;
# Ф, Щ, Ъ – 10 очков.
# Напишите программу, которая вычисляет стоимость введенного пользователем слова k и выводит его. Будем считать, что на вход подается только одно слово, которое содержит либо только английские, либо только русские буквы.

scoresMatrixASCII ={'1':['A','E','I', 'O', 'U', 'L', 'N', 'S', 'T', 'R'], '2':['D','G'],'3':['B', 'C', 'M', 'P'], '4':['F', 'H', 'V', 'W', 'Y'], '5':['K'], '8':['J','X'],'10':['Q','Z']}
scoresMatrixCyrillic={'1':['А','В','Е', 'И', 'Н', 'О', 'С', 'Р', 'Т'], '2':['Д','К','K','М','П','У'],'3':['Б', 'Г', 'Ё', 'Ь','Я'], '4':['Й', 'Ы'], '5':['Ж', 'З', 'Х', 'Ц','Ч'], '8':['Ш','Ы','Ю'],'10':['Ф','Щ','Ъ']}
#print (scoresMatrixASCII)

# for key in scoresMatrix:
#     print(key)
sum=0
print('Input a word')
word= input()
for i in word:
    if(i.isascii()):
        for key in scoresMatrixASCII:
            for char in scoresMatrixASCII[key]:
                if(i.upper()==char):
                    sum+=int(key)
                continue
    else:
        for key in scoresMatrixCyrillic:
            for char in scoresMatrixCyrillic[key]:
                if(i.upper()==char):
                    sum+=int(key)
                continue

print(sum)