things = {'зажигалка': 20, 'компас': 100, 'фрукты': 500, 'рубашка': 300,
       'термос': 1000, 'аптечка': 200, 'куртка': 600, 'бинокль': 400, 'удочка': 1200,
          'салфетки': 40, 'бутерброды': 820, 'палатка': 5500, 'спальный мешок': 2250, 'жвачка': 10}
sorted_things = dict(sorted(things.items(), key=lambda item: item[1], reverse=True))
the_choice_of_user = int(input())
final_list = []
print(sorted_things)
for key, value in sorted_things.items():
    if value < the_choice_of_user:
        d.append(key)
        the_choice_of_user = the_choice_of_user - y
    else:
        continue
print(final_list)