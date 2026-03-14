# with open('file.txt', 'r') as f:

#     # move to the 10th byte of file
#     f.seek(10)

#     # read the next 5 bytes
#     print(f.tell())
#     data = f.read(5)
#     print(data)

with open('sample.txt', 'w') as f:
    f.write("hellow world3")
    f.truncate(3)

