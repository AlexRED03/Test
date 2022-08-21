documents = [
     {"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"},
        {"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"},
        {"type": "insurance", "number": "10006", "name": "Аристарх Павлов"}
      ]
directories = {
        '1': ['2207 876234', '11-2', '5455 028765'],
        '2': ['10006'],
        '3': []
      }

def people(documents):
    number = str(input('Введите номер документа '))
    for a in documents:
        if str(a['number']) == number:
            return(print(a['name']))
    else:
        print('Такого документа несуществует ')


def shelf(directories):
    number = str(input('Введите номер документа '))
    for keys, values in directories.items():
        for a in values:
            if a == number:
                return(print(keys))
    else:
        print('Такого документа несуществует ')


def list1(documents):
    for a in documents:
        b = list(a.values())
        print(f'{b[0]} {b[1]} {b[2]}')

    
def add1(documents,directories):
    type1 = input('Тип документа ')
    number = input('Номер документа ')
    name = input('Имя владельца ')
    namber_directorie = input('Номер полки ')
    document = {"type": type1, "number": number, "name": name}
    documents.append(document)
    for a in directories.keys():
        if namber_directorie == a:
            ((directories[namber_directorie]).append(number))
            return
    else:
        print('Такой полки несуществует ')        

    
def delete1(documents,directories):
    number = str(input('Введите номер документа '))
    for a in documents:
        if str(a['number']) == number:
            documents.remove(a)
            for keys, values in directories.items():
                for b in values:
                    if b == number:
                        values.remove(number)
                        return
    else:
        print('Такого документа несуществует ')


def move(directories):
    number_doc = str(input('Введите номер документа '))
    chek = []
    chek2 = []
    for a, b in directories.items():
        for e in b:
            chek.append(e)   
    if number_doc not in chek:
        return(print('Некоректные данные'))
    namber_directorie = str(input('Номер полки '))
    for a in directories.keys():
        chek2.append(a)
    if namber_directorie not in chek2:
        return(print('Некоректные данные'))
    for keys, values in directories.items():
        for b in values:            
            if b == number_doc: 
                 values.remove(number_doc)
        for c in  keys:
            if c == namber_directorie:
                values.append(number_doc)
       
def add_sheif(directories):
    namber_directorie = str(input('Номер полки '))
    chek2 = []
    for a in directories.keys():
        chek2.append(a)
    if namber_directorie in chek2:
        return(print('Полка уже существует'))
    directories[namber_directorie] = []

def main(documents, directories):        
    while True:
            comand = input('Введите команду ')
            if comand == 'p':
                people(documents)
            elif comand == 's':
                shelf(directories)
            elif comand == 'l':
                list1(documents)
            elif comand == 'a':
                add1(documents,directories)
            elif comand == 'd':
                delete1(documents,directories)
            elif comand == 'm':
                move(directories)
            elif comand == 'as':
                add_sheif(directories)
            elif comand == 'q':
                print('Выход из программы ')
                break        


main(documents, directories)           
        


#  people(documents)
#  shelf(directories)
# list1(documents)    
# add1(documents,directories)
# delete1(documents,directories)
# move(directories)
# add_sheif(directories)
# print(directories)
# print(documents)

