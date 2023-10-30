
# Создать телефонный справочник с  возможностью импорта и экспорта данных в
# формате .txt. Фамилия, имя, отчество, номер  телефона - данные, которые
# должны находиться в файле.
# 1. Программа должна выводить данные 
# 2. Программа должна сохранять данные в текстовом файле
# 3. Пользователь может ввести одну из характеристик для поиска определенной
# записи(Например имя или фамилию человека)
# 4. Использование функций. Ваша программа не должна быть линейной


def WorkWithPhonebook():
    choice = ShowMenu()
    #phonebook = ReadFile('phonebook.csv')
    while(choice!=8):
        phonebook = ReadFile('phonebook.csv')
        if(choice==1):
            PrintResult(phonebook)
        elif(choice==2):
            lastname=input('Input lastname: ')
            print(FindByLastname(phonebook,lastname))
            input()
        elif(choice==3):
            lastname=input('Input lastname: ')
            phoneNumber=input('Input new phone: ')
            print(ChangePhone(phonebook,lastname,phoneNumber))
            input()
        elif(choice==4):
            lastname=input('Input lastname: ')
            DeleteByLastname(phonebook,lastname)
            input()
        elif(choice==5):
            phoneNumber=input('Input phonenumber: ')
            print(FindByPhoneNumber(phonebook,phoneNumber))
            input()
        elif(choice==6):
            userData=input('Input user data: ')
            AddUser(phonebook, userData)
            #WriteFile('phonebook.csv', phonebook)
        elif(choice==7):
            record=int(input('Input record number: '))
            WriteToOtherFile('phonebook1.csv', phonebook,record)
            input()
        choice = ShowMenu()
        
def ShowMenu():
    print('1. Вывести справочник\n'
          '2. Найти телефон по фамилии\n'
          '3. Изменить номер телефона абонента\n'
          '4. Удалить запись\n'
          '5. Найти абонента по номеру телефона\n'
          '6. Добавить абонента в справочник\n'
          '7. Копировать строку записи в другой файл\n'
          '8. Закончить работу', sep='\n')
    choice= int(input())
    return choice

def ReadFile(filename):
    phonebook = []
    fields=['Фамилия', 'Имя', 'Телефон', 'Описание']
    with open (filename, 'r', encoding='utf8') as fileData:
        for line in fileData:
            record = dict(zip(fields, line.split(',')))
            phonebook.append(record)
    return phonebook

def WriteFile(filename, phonebook, isAdding):
    with open (filename, 'w', encoding='utf8') as fileData:
        for i in range(len(phonebook)):
            s=''
            for v in phonebook[i].values():
                s+=v+','
            fileData.write(f'{s[:-1]}')
        if(isAdding):
            fileData.write('\n')

def PrintResult(phonebook):
    for rec in phonebook:
        row=[]
        for v in rec.values():
            row.append(v)
        print(row)


def FindByLastname(phonebook, lastname):
    result=[]
    for record in phonebook:
        for key in record:
            if  key=='Фамилия' and record[key] ==lastname:
                result.append(record)
    return result

def FindByPhoneNumber(phonebook, phoneNumber):
    result=[]
    for record in phonebook:
        for key in record:
            if  key=='Телефон' and record[key] ==phoneNumber:
                result.append(record)
    return result

def ChangePhone(phonebook, lastname, phoneNumber):
    record = FindByLastname(phonebook,lastname)
    if(len(record)==1):
        record[0]['Телефон']=phoneNumber
    elif(len(record)==0):
        print("Not founded records!")
    elif(len(record)>1):
        print("More than one record founded!")
    WriteFile('phonebook.csv', phonebook, False)
    return record

def DeleteByLastname(phonebook,lastname):
    record = FindByLastname(phonebook,lastname)
    for item in record:
        phonebook.remove(item)
    WriteFile('phonebook.csv', phonebook, False)

def AddUser(phonebook, userData):
    values =userData.split(",")
    keys = phonebook[0].keys()
    newRecord = dict(zip(keys,values))
    phonebook.append(newRecord)
    WriteFile('phonebook.csv', phonebook, True)

def WriteToOtherFile(filename,phonebook,record):
    with open (filename, 'w', encoding='utf8') as fileData:
        for i in range(len(phonebook)):
            if (i==record-1):
                s=''
                for v in phonebook[i].values():
                    s+=v+','
                fileData.write(f'{s[:-1]}')
        fileData.write('\n')


WorkWithPhonebook()