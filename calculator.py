x = int(input("Enter First Number "))
y = int(input("Enter Second Number "))
print("Enter 1 for Addition")
print("Enter 2 for Subtraction")
print("Enter 3 for Multiplication")
print("Enter 4 for Division")
z = int(input("Enter your choice "))
if(z==1):
    print("The Sum is ",(x+y))
elif(z==2):
    print("The difference is ",(x-y))
elif(z==3):
    print("Result is ",(x*y))
elif(z==4):
    print("Result is ",(x/y))
else:
    print("Invalid choice")
