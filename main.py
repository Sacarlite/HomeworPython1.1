'''
#1
day=int(input())
if day==6 and day==7:
    print("Yes")
else:
    print("No")
'''
'''
#2
x=bool(input())
y=bool(input())
z=bool(input())
if not(x and y and z):
    print("true")
else:
    print("false")
'''
'''
#3
x=int(input())
y=int(input())
if x>0 and y>0:
    print("1 quarter")
elif x<0 and y>0:
    print("2 quarter")
elif x<0 and y<0:
    print("3 quarter")
else:
    print("4 quarter")
'''
'''
#4
quarter=int(input())
if quarter==1:
    print("0<x<+∞ and 0<y<+∞")
elif quarter ==2:
    print("-∞<x<0 and 0<y<+∞")
elif quarter == 3:
    print("-∞<x<0 and -∞<y<0")
elif quarter == 4:
    print("0<x<+∞ and -∞<y<0")
else:
    print("error,quarter not found")
'''
'''
#5
import math
x1=int(input())
y1=int(input())
x2=int(input())
y2=int(input())
interval=math.sqrt(math.pow(x2-x1,2)+math.pow(y2-y1,2))
print(f'the interval is {interval}')
'''
