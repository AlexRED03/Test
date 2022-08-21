# Задание 1 

geo_logs = [
   {'visit1': ['Москва', 'Россия']},
   {'visit2': ['Дели', 'Индия']},
   {'visit3': ['Владимир', 'Россия']},
   {'visit4': ['Лиссабон', 'Португалия']},
   {'visit5': ['Париж',' Франция']},
   {'visit6': ['Лиссабон', 'Португалия']},
   {'visit7': ['Тула', 'Россия']},
   {'visit8': ['Тула', 'Россия']},
   {'visit9': ['Курск', 'Россия']},
   {'visit10': ['Архангельск', 'Россия']}
]
# geo_logs1 = []
# for a in geo_logs:
#     for b, c in a.values():
#         if c == 'Россия':
#             geo_logs1.append(a)
# geo_logs = geo_logs1          
# print(geo_logs)     

'''из за смещения эелементов в списке при однократной проходке он игнорирует часть элементов (точнее в данном случае один), пришлось проверять ещё раз, не уверен что правильно все но вот так получилось'''

# for a in geo_logs:
#     for b, c in a.values():
#         if c != 'Россия':
#             geo_logs.remove(a)
#             for g in geo_logs:
#                 for e, d in g.values():
#                     if d != 'Россия':
#                         geo_logs.remove(g)        
# print(geo_logs)       



# Задание 2

# ids = {'user1': [213, 213, 213, 15, 213],
#        'user2': [54, 54, 119, 119, 119],
#        'user3': [213, 98, 98, 35]}

# ids1 = set(ids['user1']) | set(ids['user2']) | set(ids['user3'])
# print(ids1)



# Задание 3

#queries = [
#    'смотреть сериалы онлайн',
#    'новости спорта',
#    'афиша кино',
#    'курс доллара',
#    'сериалы этим летом',
#    'курс по питону',
#    'сериалы про спорт'
#    ]
#b = []
#for a in queries:
#    result = len(a.split())
#    b.append(result)
#c = set(b)
#for e in c:
#    n = b.count(e)
#    f = round(n / len(queries) * 100, 2)
#    print (f'Запросов из {e} слов {f}%')

# Задание 4

stats = {'facebook': 55, 'yandex': 120, 'vk': 115, 'google': 99, 'email': 42, 'ok': 98}
meaning = []
for a in stats.values():
   meaning.append(a)
for c, d in stats.items():
   if d == max(meaning):
       print (c)


# Задание 5(Необязательное)
# list1 = ['2018-01-01', 'yandex', 'cpc', 100]
# list1.reverse()
# list2 = {}
# n = 0
# while n < len(list1) - 1:
#     list2[list1[n]] = list1[n+1]
#     n+=1
    
# print(list2.items())
