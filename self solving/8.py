num1=int(input("enter your first number"))
num2=int(input("enter your second number"))
num3=int(input("enter your third number"))

if(num1>num2 & num1>num3):
    print("num 1 is greater")
elif(num2>num3 & num2<num1):
    print("num2 is greater")
else:
    print("num 3 is greater")