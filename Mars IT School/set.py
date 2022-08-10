'''
set1 = {"uzum", "olma", "anor", "qulupnay", "banan", "olma", True, 13, 45}
print(set1)
print(type(set1))
set1.add("qovun")
print(set1)
print(len(set1))
set2 = {"jafar", "olxo'ri"}
list1 = ["9-a", "10-b"]

for i in set1:
    print(i)
print("banan" in set1)
set1.update(set2)
print(set1)
set1.update(list1)
print(set1)
set1.remove("banan")
print(set1)
set1.disscard("olma")
print(set1)
a = set1.pop()
print(a)
set1.clear()
print(set1)
del set1
print(set1)

set1.intersection_update(set2)
print(set1)
'''

set1 = {"uzum", "olma", "anor", "qulupnay", "banan", "olma", True, 13, 45}
set2 = {"jafar", "olxo'ri", "olma"}
#set1.intersection_update(set2)
#set3 = set1.intersection(set2)
#set1.symmetric_difference_update(set2)
#set3 = set1.symmetric_difference(set2)

print(set1)
