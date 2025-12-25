
print("Welcome to the calculator")
print("select an operation to perform:")
print("1. ADD")
print("2. SUBTRACT")
print("3. DIVIDE")
print("4. MULTIPLY")
print("\nKindly choose the operation above and enter it's    corresponding number")

operation = input("What is your operation : ")
num1 = float(input("Enter Number 1 : "))
num2 = float(input("Enter Number 2 : "))

if operation == "1":
    print ("Num 1 + Num 2 = " , float(num1) + float(num2)) or print("Num 2 + Num 1 = " , float(num1) + float(num2))
elif operation == "2":
    print ("Num 1 - Num 2 = " , float(num1) - float(num2)) or print("Num 2 - Num 1 = " , float(num1) - float(num2))
elif operation == "3":
    print ("Num 1 / Num 2 = " , float(num1) / float(num2)) or print("Num 2 / Num 1 = " , float(num1) / float(num2))
elif operation == "4":
    print ("Num 1 * Num 2 = " , float(num1) * float(num2)) or print("Num 2 * Num 1 = " , float(num1) * float(num2))
else:

    print("Invalid Entry")
