# Напишите функцию 
# print_operation_table(operation, num_rows=6, num_columns=6), 
# которая принимает в качестве аргумента функцию, вычисляющую элемент 
# по номеру строки и столбца. Аргументы num_rows и num_columns 
# указывают число строк и столбцов таблицы, которые должны быть 
# распечатаны. Нумерация строк и столбцов идет с единицы (подумайте, 
# почему не с нуля). Примечание: бинарной операцией называется любая 
# операция, у которой ровно два аргумента, как, например, у операции 
# умножения.

# *Пример:*

# **Ввод:** `print_operation_table(lambda x, y: x * y) ` 
# **Вывод:**

def print_operation_table(operation, num_rows=6, num_columns=6):
    rows = []
    for row in range(1, num_rows + 1):
        row_elements = []
        for column in range(1, num_columns + 1):
            element = operation(row, column)
            row_elements.append(element)
        rows.append(row_elements)

    for row in rows:
        row_formatted = [f"{element:8}" for element in row]
        table_row = "".join(row_formatted)
        print(table_row)


print_operation_table(lambda x, y: x * y, 8, 2)