#Genesis C. Phillips
#Python Calculator (BasicCalculator.py)

def main():

    print("\nWelcome to the Basic Calculator \n")
    # This adds two numbers
    def add(x, y):
        return x + y
    #This subtracts two numbers
    def subtract(x, y):
        return x - y
    #This multiplies two numbers
    def multiply(x,y):
        return x * y
    #This divides two numbers
    def divide(x, y):
        return x / y

    print("SELECT OPERATION")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide \n")

    #Take input from the user
    choice = input("Enter choice | 1 | 2 | 3 | 4 |: ")
    num1 = int(input("\nEnter first number: "))
    num2 = int(input("Enter second number: "))

    if choice == '1':
        print(num1,"+",num2,"=", add(num1, num2))
    elif choice == '2':
        print(num1,"-",num2,"=", subtract(num1, num2))
    elif choice == '3':
        print(num1,"*",num2,"=", multiply(num1, num2))
    elif choice == '4':
        print(num1,"/",num2,"=", divide(num1, num2))
    else:
        print("Invalid input")
    print("\nThanks for using!")

    restart=input("Do you want to start again? (y/n) ")
    #This restarts the program
    if restart == "y":
        main()
    else:
        exit
main()