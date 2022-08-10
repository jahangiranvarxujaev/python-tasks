# recoursive function is function into function
a = int(input())
def reverse_number(a):
    b = 1
    for i in range(1, (a + 1)):
        b = b * i
    print(b)
print(reverse_number(a))