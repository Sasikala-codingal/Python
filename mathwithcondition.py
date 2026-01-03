import math  

x = float('nan')
if math.isnan(x): 
    print('It is not a number')
x = float('inf')
y = 45
if math.isinf(x): 
    print('It is Infinity')
print(math.isfinite(x)) 
print(math.isfinite(y)) 
print(math.isnan(y))
