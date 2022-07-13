#Напишите функцию, которая принимает словарь с параметрами и возвращает строку запроса, сформированную из отсортированных в лексикографическом порядке параметров.
#Пример:
#Код print(query({'course': 'python', 'lesson': 2, 'challenge': 17})) должен возвращать строку:
#challenge=17&course=python&lesson=2
dict1 = {'name':'Jahongir', 'age':'15', 'hobby':'pyrhon coding'}
for x, y in dict1.items():
    print(x, '=', y, '&' )