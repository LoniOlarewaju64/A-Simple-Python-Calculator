# Subtraction "-"
#  Adding: "+"
# Mutliplication "*"
# Division "/"

num1 = int
num2 = int
answer_num3 = int

num1 = float(input("Please type in your first number."))

num2 = float(input("Now type in your second number."))


input = input("Would you like to add, subtract, multiply or divide both numbers? 1. = Add, 2. Subtract, 3. Multiply  4. Divide" )

# Addition
if input == "1":
    answer_num3 = num1 + num2
    print(f"The answer is: {answer_num3}")
    

# Subtraction
if input == "2":
   answer_num3 =  num1 - num2
   print(f"The answer is: {answer_num3}")
   

# Multiplication
if input == "3":
    answer_num3 = num1 * num2
    print(f"The answer is: {answer_num3}")
    

# Division
if input == "4":
    answer_num3 = num1 / num2
    print(f"The answer is: {answer_num3}")
    

else:
    "Your input is invalid. Please try again."
