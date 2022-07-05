x = int(input("? "))
y = int(input("? "))
x1 = int(input("? "))
y1 = int(input("? "))
a = abs(x - x1)
b = abs(y - y1)
if ((a == 1) & (b == 2)) | ((a == 2) & (b == 1)):
    print("может")
    '''
    if ((x % 2 == 0) & (y % 2 == 0)) | ((x1 % 2 != 0) & (y1 % 2 != 0)):
        print('white, black')
    else:
        print('black, white')
        '''
else:
    print("не может")



        
