# Создать телефонный справочник с возможностью импорта и экспорта данных в формате .txt. Фамилия, имя, отчество, номер телефона - данные, которые должны находиться в файле.
#
# Программа должна выводить данные
# Программа должна сохранять данные в текстовом файле
# Пользователь может ввести одну из характеристик для поиска определенной записи(Например имя или фамилию человека)
# Использование функций. Ваша программа не должна быть линейной
def imp():
    with open('dict.txt', 'a', encoding='utf-8') as file:
        record = {
            "firstname": input('введите имя: '),
            "surname": input('введите фамилию: '),
            "patronymic": input('введите отчество: '),
            "phone": input('введите номер телефона: ')
        }
        file.write(str(record)[1:-1] + '\n\n')

def exp():
    with open('dict.txt', 'r', encoding='utf-8') as file:
        records = file.readlines()
        search = input('Введите имя или фамилию человека, которого необходимо найти: ')
        count = records
        for i in range(len(records)):
            if search in records[i]:
                count = i
        if count == records:
            print('Человек по запрашиваемым данным не найден, весь справочник ниже:')
            print(records)
        else:
            print(records[count])


def main():
    task = int(input('Если вы хотите внести запись - введите 1, если найти запись - введите 2'))
    if task == 1:
        imp()
    elif task == 2:
        exp()
    return 0

main()