#types of all files
# text files :txt,docs,.log
# binary files : mp4,mov,png,jpeg


# f =open("demo.txt","r")
# data = f.read()
# print(data)
# print(type(data))
# f.close()

# f= open("demo.txt","r")
# data = f.read(5)
# print(data)
# print(type(data))
# f.close()


f=open("demo.txt","r")
line1 = f.readline()
print(line1)