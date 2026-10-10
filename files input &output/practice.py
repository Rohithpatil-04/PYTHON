# with open("practice.txt","w") as f:
#     f.write("hi everyone\n we are learning fileI/O\n")
# #     f.write("using java.\ni like programming in java."
# )


# with open("practice.txt","r") as f:
#     data=f.read()

# new_data = data.replace("java","python")
# print(new_data)


# with open("practice.txt","w")as f:
#     f.write(new_data)


# word="learning"
# with open("practice.txt","r") as f:
#     data = f.read()
#     if(data.find(word) != -1):
#         print("found")
#     else:
#         print("not found")




# def check_for_line():
#     word="learning"
#     data=True
#     line_no =1

#     with open("practice.txt","r") as f:
#         while data:
#             data=f.readline()
#             if(word in data):
#                 print(line_no)
#                 return
#             line_no+=1
#     return -1
# check_for_line()


# count=0
# with open("practice.txt","r") as f:
#     data=f.read()
#     print(data)

#     nums=data.split(",")
#     for val in nums:
#         if(int(val)%2 ==0):
#             count +=1
# print(count)