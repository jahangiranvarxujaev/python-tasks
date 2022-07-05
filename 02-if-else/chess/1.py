x = int(input()) 
y = int(input()) 
x1 = int(input()) 
y1 = int(input()) 
if x1 - x == -1 and y1 - y == -1: 
    print("не может") 
elif x == x1 and y < y1: 
    print("может") 
elif abs(x-x1) == 1 and abs(y-y1) == 1: 
    print("атакует") 
else: 
    print("не может")
