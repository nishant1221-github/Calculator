# ..............Simple Calculator.................

# Take the input from the user.
num1 = eval(input("Enter your first number : "))

num2 = eval(input("Enter your second number : "))

# Print all the operators for using opeartions.
print("Choose your Operator : + , - , * , / , % , //")

# Choose your operator from given operators.
opr = input("Choose your operation : ")

# Use conditions for add(+), subtract(-), multiplication(*), division(/), mod(%) and floor division(//) operations.
if opr == '+' :
    print(num1+num2)

elif opr == '-' :
    print(num1-num2)

elif opr == '*' :
    print(num1*num2)

elif opr == '/' :
    print(num1/num2)

elif opr == '%' :
    print(num1%num2)

elif opr == '//' :
    print(num1//num2)

# Print the following statement if the user choose wrong input.
else:
    print("Wrong Input. Please choose valid input.")

