def recur_factorial(num, ):
    if num == 1:
        return num
    else:
        return num * recur_factorial(num - 1)


number = int(input())
print(recur_factorial(number))
