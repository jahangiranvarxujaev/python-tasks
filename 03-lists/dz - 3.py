#найти количество чисел в массиве, которые делятся на 3, но не делятся на 7

def get_division_of_numbers(numbers: list):
    final_result = 0
    for number in numbers:
        if (number / 3) and (number % 7 != 0):
            final_result += 1
        else:
            continue

    return final_result


input_numbers = list(map(int, input().split()))

get_division_of_numbers(input_numbers)
