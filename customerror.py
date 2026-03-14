a = int(input("Enter any value between 5 and 9 "))

if(a< 5 or a>9):
    raise ValueError("Value should be between 5 and 9")

# Enter any value between 5 and 9 3
# ERROR!
# Traceback (most recent call last):
#   File "<main.py>", line 4, in <module>
# ValueError: Value should be between 5 and 9