def appl(fx, value):
    return 6 + fx(value)

double = lambda x: x*2
avg = lambda x,y : (x+y)/2

print(double(5))
print(avg(3,5))
print(appl(double, 2))