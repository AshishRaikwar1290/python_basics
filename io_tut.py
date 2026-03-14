# read
# f = open('myfile.txt', 'r')
# print(f)
# text = f.read()
# print(text)
# f.close()



# f = open('myfile.txt', 'a')
# f.write("i am here3")
# f.close()

# with open('myfile.txt', 'a') as f:
#     f.write("i am inside")

f = open('myfile.txt', 'r')
while True:
    line = f.readline()
    if not line:
        break
    print(line)

f = open('myfile.txt', 'w')
lines = ['line 1\n', 'line 2\n', 'line3\n']
f.writelines(lines)
f.close()