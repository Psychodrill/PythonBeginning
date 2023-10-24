# Напишите функцию print_operation_table(operation, num_rows, num_columns), которая принимает в качестве аргумента функцию, вычисляющую элемент по номеру строки и столбца.

# Аргументы num_rows и num_columns указывают число строк и столбцов таблицы, которые должны быть распечатаны.

# Нумерация строк и столбцов идет с единицы (подумайте, почему не с нуля).

# Если строк меньше двух, выдайте текст
# ОШИБКА! Размерности таблицы должны быть больше 2!.

# Примечание: бинарной операцией называется любая операция, у которой ровно два аргумента, как, например, у операции умножения.

def print_operation_table(operation, num_rows, num_columns):
    if(num_rows>=2 and num_columns>=2):
        for i in range(1,num_rows+1):
            for j in range(1, num_columns+1):
                if(i==1):
                    print(j, end=' ')
                    continue
                if(j==1):
                    print(i, end=' ')
                    continue
                result = operation(i,j)
                print(result, end=' ')
            print('')
    else:
        print("ОШИБКА! Размерности таблицы должны быть больше 2!")
    
    
#print_operation_table(lambda x, y: x * y, 3, 3)
#print_operation_table(lambda x, y: x + y, 4, 4)
print_operation_table(lambda x, y: x / y, 4, 4)
#print_operation_table(lambda x, y: x * y, 3, 3)

#print(5, " ")