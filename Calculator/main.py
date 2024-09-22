# Here we gonna define a function which will add two numbers 
def add(n1 , n2):
    return n1 + n2
# Here we gonna define a function which will subtract two numbers
def subtract(n1 , n2):
    return n1 - n2
# Here we gonna define a function which will multiply two numbers
def multiply(n1 , n2):
    return n1 * n2
# Here we gonna define a function which will divide two numbers
def divide(n1 , n2):
    if n2 == 0:
        return "Error! Division by zero is not allowed."
    else:
        return n1 / n2
    
# Now we are going to define a main function
def main():
    print("Welcome! to python calculator.")
    try:
        n1 = float(input("Please, Enter the First Number: "))
        n2 = float(input("Please, Enter the Second Number: "))
    except ValueError:
        print("Invalid input. Please enter a number.")
        return main()
    
    # Now take a choice from the user which task he want to perform on the given numbers
    print("Please select the operator.")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    choice = int(input("Enter your choice (1, 2, 3, 4)"))

    if choice == 1:
        print(f"{n1} + {n2} = {add(n1, n2)}")
    elif choice == 2:
        print(f"{n1} - {n2} = {subtract(n1, n2)}")
    elif choice == 3:
        print(f"{n1} * {n2} = {multiply(n1, n2)}")
    elif choice == 4:
        print(f"{n1} / {n2} = {divide(n1, n2)}")
    else:
        print("Invalid choice. Please choose a valid option.")
        return main()

main()
