# #oop in python- to map with real world scenarios ,we started using objects in code
class Student:
   
    # name="karan"
    def __init__(self,fullname,marks):
       self.name=fullname
       self.marks=marks
       print("adding new student in dataabse")


s1=Student("karan",99)
# print(s1.name)

print(s1.name)

s2=Student("arjun",98)
print(s2.name)





# class Car:
#     color="blue"
# car1=Car()
# print(car1.color)