def get_fibo_numbers(numbers):
    """
    Accepts list of numbers
    Returns fibonnaci numbers
    """
    fibo_numbers = 0
    fibo_list = [0, 1]
    i = 0
    while i < max(numbers):
        fibo_numbers = fibo_list[i] + fibo_list[i+1]
        fibo_list.append(fibo_numbers)
        i += 1
    for i in numbers:
        print(fibo_list[i - 1])


users_option = list(map(int, input().split()))
get_fibo_numbers(users_option)
