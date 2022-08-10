#computers option
import random
comps_option = random.choice([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
print(comps_option)
#users option
users_option = 0
#process
"""if users_option == comps_option:
    print("Right!!")
else:
    users_option = int(input("Try again"))
    if users_option == comps_option:
        print("right")
    else:
        users_option = int(input("Try again"))
        if users_option == comps_option:
            print("right")
        else:
            users_option = int(input("Try again"))
    
"""
while users_option == comps_option:
    users_option = int(input("Choose the number from 1 to 10 "))
    if users_option == comps_option:
        print('YOu arE WinnEr')
        break
