def add(x,y):
    return x+y
def subtract(x,y):
    return x-y
def multiply(x,y):
    return x*y
def divide(x,y):
    if y==0:
        return"error!division by zero"
    return x/y
print("Welcome to simple calculator")
while True:
    print("\n select operation:")
    print("1.Addition:")
    print("2.Subtract:")
    print("3.multiply:")
    print("4.division:")
    print("5.Quit:")
    choice=input("Enter choice (1/2/3/4/5):")
    if choice in ['1','2','3','4']:
        num1=float(input("enter first number:"))
        num2=float(input("enter second number:"))
        if choice=='1':
            print("result",add(num1,num2))
        elif choice=='2':
            print("result",subtract(num1,num2))
        elif choice=='3':
            print("result",multiply(num1,num2))
        elif choice=='4':
            print("result",division(num1,num2))
        elif choice=='5':
            print("exiting program")
            break
        else:
            print("invalid input,please try again")
