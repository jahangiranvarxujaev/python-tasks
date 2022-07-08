paper = 1
scissors = 2
well = 3
print("write your option")
print("1 - бумага")
print("2 - ножницы")
print("3 - колодец")
users_option = int(input())
if users_option > 3:
    print('write number is less than 3. Please, write number that will be less than 3!')
set1 = {"бумага", "ножницы", "колодец"}
print(users_option)

#User's option
a = []
if users_option == 1:
    a.append("бумага")
elif users_option == 2:
    a.append("ножницы")
else:
    a.append("колодец")



#computer's option
komps_option = set1.pop()
print(komps_option)

#proccess
if komps_option == a:
    print(komps_option, a, 'ничья')
elif (komps_option == "бумага") and (a == "ножницы"):
    print(komps_option, a, 'выиграл пользователь')
elif (a == "бумага") and (komps_option == "ножницы"):
    print(komps_option, a, 'выиграл компьютер')
elif (a == "колодец") and (komps_option == "ножницы"):
    print(komps_option, a, 'выиграл пользователь')
elif (komps_option == "колодец") and (a == "ножницы"):
    print(komps_option, a, 'выиграл компьютер')
elif (a == "колодец") and (komps_option == "бумага"):
    print(komps_option, a, 'выиграл компьютер')
else:
    print(komps_option, a, 'выиграл пользователь')
