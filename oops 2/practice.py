# class circle:
#     def __init__(self,radius):
#         self.radius = radius

#     def area(self):
#         return (22/7) * self.radius **2

#     def perimeter(self):
#         return 2 *(22/7) * self.radius

# c1=circle(21)
# print(c1.area())
# print(c1.perimeter())





class Employee:
    def __init__(self,role,dept,salary):
        self.role = role
        self.dept = dept
        self.salary = salary

    def showDetails(self):
        print("role =",self.role)
        print("dept=",self.dept)
        print("salary=",self.salary)



class Engineer(Employee):
    def __int__(self,name,age,salary):
        self.name = name
        self.age = age
        self.salary= salary
        super().__init__("Engineer","it","75000")
        




# e1=Employee("accountant","finance","60000")
# e1.showDetails()


engg1=Engineer("elon musk",40)
engg1.showDetails()