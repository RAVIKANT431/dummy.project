num1= input("enter first value:" )

num2= input("enter second value:" )
num3= input("enter third value:" )
num1=float(num1)
num2=float(num2)
num3=float(num3)

def max_num(num1,num2,num3):
    if num1>=num2 and num1>=num3:
        return num1
    elif num2>=num1 and num2>=num3:
        return num2
    else:
        return num3


print(max_num(num1,num2,num3))
