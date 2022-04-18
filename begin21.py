#Tomonini kooordinatalari berlgan holda uchburchak yuzi va peimetrini topish
x1=int(input("X1="))
x2=int(input("X2="))
x3=int(input("X3="))
y1=int(input("Y1="))
y2=int(input("Y2="))
y3=int(input("Y3="))
import math
a=math.sqrt((x1-x2)**2+(y1-y2)**2)
b=math.sqrt((x1-x3)**2+(y1-y3)**2)
c=math.sqrt((x2-x3)**2+(y2-y3)**2)
p=(a+b+c)/2
print("Yuzi=",math.sqrt(p*(p-a)*(p-b)*(p-c)),"\nPerimetri=",a+b+c)