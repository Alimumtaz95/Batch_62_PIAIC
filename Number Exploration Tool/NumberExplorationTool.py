# Get the user's name and favorite numbers
name = input("Enter your name: ")
numbers = []
for i in range(3):
    num = int(input(f"Enter your favorite number {i+1}: "))
    numbers.append(num)

# Greet the user with a personalized message
print(f"Hello, {name}! Let's explore your favorite numbers:")

# Check if each number is even or odd and store in a list of tuples
even_odd_list = []
for num in numbers:
    if num % 2 == 0:
        even_odd_list.append((num, "even"))
    else:
        even_odd_list.append((num, "odd"))

# Print the even/odd information in a creative format
print("Here's some interesting info about your numbers:")
for num, parity in even_odd_list:
    print(f"  {num} is {parity}!")

# Calculate the sum of the numbers and print the result
sum_of_numbers = sum(numbers)
print(f"The sum of your numbers is: {sum_of_numbers}")

# Print an encouraging message
print("Wow, that's a great sum! Let's see if it's a prime number...")

# Check if the sum is a prime number
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

if is_prime(sum_of_numbers):
    print("And... it's a prime number! Congratulations!")
else:
    print("Not a prime number, but still a great sum!")