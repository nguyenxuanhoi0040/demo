#viết chương trình tính diện tích tam giác bằng ct heron
import math
a=float(input('a='))
b=float(input('b='))
c=float(input('c='))
p=(a+b+c)/2
s=math.sqrt(p*(p-a)*(p-b)*(p-c))
print('diện tích tam giác:',s)

