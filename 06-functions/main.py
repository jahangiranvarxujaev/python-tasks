"""def multiply_numbers(number1, number2):
    return number1 * number2


multiply_numbers(2, 5)
"""



def sum_range(start, end):
    summa = 0
    for i in range(start, end+1):
        summa += i
    print(summa)

start2 = int(input())
end2 = int(input())
copy_of_start = start2
if start2 > end2:
    start2 = end2
    end2 = copy_of_start


print(sum_range(start2, end2))
