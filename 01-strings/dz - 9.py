'''
Найдите наибольшее количество идущих подряд цифр.
'''


NUMBERS = '0123456789'
a = input("Word? ")
number_counter = 0
max_number = 0
b = 0
for letter in a:
    if letter in NUMBERS:
        number_counter += 1
        b = number
    else:
        max_number = number_counter
        
        print(max_number)
        print(number_counter)
        if max_number < number_counter:
            max_number = number_counter
            print(max_number)
        else:
            print(number_counter)
            
        continue

