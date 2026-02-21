# explicit 
# and implicit

c = 1.9
d = 8
print(c+d)


a = input("enter you name")
print(a)

apple = '''he is dog
why is he a dog'''

print(apple)

names = "Harry, Shubham"

print(names[0:5])
names = "Harry, Shubham"
length = len(names)
print(length)
print(names[0:5])
print(names[:7])
print(names[:])
print(names[0:-2])
print(names[-4:-2])


# string are immutable
a = "!!!Ha rry!!!"
print(len(a))
print(a.upper())
print(a.lower())
print(a.rstrip("!"))
print(a.replace("Harry", "John"))
print(a.split(" "))
print(a.capitalize())
print(a.center(50))


from doctest import OutputChecker
import time 
timestamp = time.strftime('%H:%M:%S')
print(timestamp)

# match case
x = 4
match x:
    case 0:
        print("x is zero")
    case 4 if x%2 == 0:
        print("i am 4")
    case _:
        print(x)


# for loop
name = "abhishek"

for i in name:
    if(i == 'b'):
        print("this is special")
        
        
colors = ["red", "blue"]

for col in colors:
    print(col)
    for i in col:
        print(i)

# output 
# this is special
# red
# r
# e
# d
# blue
# b
# l
# u
# e

for k in range(5):
    print(k+1)

for k in range(1, 9):
    print(k)

# increment by 3    
for k in range(1, 12, 3):
    print(k)

# output
# 1
# 2
# 3
# 4
# 5
# 1
# 2
# 3
# 4
# 5
# 6
# 7
# 8
# 1
# 4
# 7
# 10


# while loop
i=0
while(i<=3):
    print(i)
    i= i+1

# while with else
count = 5
while(count > 0):
    print(count)
    count = count - 1
else:
    print("i am inside")
    
# do while loop simulation
while True:
    user_input = input("Enter a number greater than 10: ")
    number = int(user_input)

    if number > 10:
        break


# output
# 0
# 1
# 2
# 3
# 5
# 4
# 3
# 2
# 1
# i am inside
# Enter a number greater than 10: 


# break and continue
for i in range(12):
    print("5 X", i+1, "=", 5*(i+1))
    if(i == 9):
        break
        
        
for i in range(12):
    if(i == 9):
        continue
    print("5 X", i+1, "=", 5*(i+1))

# output
# 5 X 1 = 5
# 5 X 2 = 10
# 5 X 3 = 15
# 5 X 4 = 20
# 5 X 5 = 25
# 5 X 6 = 30
# 5 X 7 = 35
# 5 X 8 = 40
# 5 X 9 = 45
# 5 X 10 = 50
# 5 X 1 = 5
# 5 X 2 = 10
# 5 X 3 = 15
# 5 X 4 = 20
# 5 X 5 = 25
# 5 X 6 = 30
# 5 X 7 = 35
# 5 X 8 = 40
# 5 X 9 = 45
# 5 X 11 = 55
# 5 X 12 = 60

# functions
def calsum(a, b):
    print(a+b)
    
calsum(4, 5)
calsum(5, 5)

# output
# 9
# 10


# argumemnts
# variable length
# required 
# default
# keywords

def average(a=9, b=1):
    print("This is average", (a+b)/2)
    
def avg(*numbers):
    # tuple
    sum = 0
    for i in numbers:
        sum = sum + i
    print("average", sum/len(numbers))
    
avg(5, 6, 7, 8)

def name(**name):
    # dict
    print("hello", name["fname"])
    
name(fname="James")

# Output
# average 6.5
# hello James



