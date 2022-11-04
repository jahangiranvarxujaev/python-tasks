def search_dublicate(option):
    comparative_list = option
    counter = 0
    for element in option:
        for i in range (0, len(option)):
            if comparative_list[i] == element:
                counter += 1
    if counter >= 2:
        print("Yes")
    else:
        print("NO")

users_option = input().split(' ')
search_dublicate(users_option)