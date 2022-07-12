paper = 1
scissors = 2
well = 3
print("write your option  ")
print("1 - бумага")
print("2 - ножницы")
print("3 - колодец")
a = int(input())
if a > 3:
    print('write number is less than 3. Please, write number that will be less than 3!')



#User's option
users_option = []
if a == 1:
    users_option.append("бумага")
elif a == 2:
    users_option.append("ножницы")
else:
    users_option.append("колодец")



#computer's option
import random
b = random.choice([1, 2, 3])
print(b)
komps_option = []

if b == 1:
    komps_option.append("бумага")
elif b == 2:
    komps_option.append("ножницы")
else:
    komps_option.append("колодец")
#imagination

print('Компьютер выбрал - ', komps_option)
print('а вы выбрали',users_option )


#proccess
if  b == a:
    print('ничья')
elif (b == 1) and (a == 2):
    print('выиграл пользователь')
elif (a == 1) and (b == 2):
    print('выиграл компьютер')
elif (a == 3) and (b == 2):
    print('выиграл пользователь')
elif (b == 3) and (a == 2):
    print('выиграл компьютер')
elif (a == 3) and (b == 1):
    print('выиграл компьютер')
else:
    print('выиграл пользователь')
