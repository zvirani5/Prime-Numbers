'''
CS1026a 2023
Assignment 01 Project 01 - Part B
Zanan Virani
zvirani5
09/28/2023
'''

'''
This program will output all the prime numbers in a range determined by the user.
If the user messes up and inputs the first value greater than the second value, then the numbers 
will automatically be switched around and the program will carry on returning the prime numbers.
'''

# Opening, as in the assignment
print("Project One (01) - Part B : Prime Choice\n")

# This will is the intended lesser value in the range
first_value = int(input("Prime Numbers starting with: "))

# This is the intended greater value in the range
second_value = int(input("and ending with: "))

# Check if the first value is less than or equal to the second value.
if first_value <= second_value:
    print(f"\nPrime Numbers in the range from: {first_value} and {second_value} are: ")
    # Iterate through the numbers in the range, +1 to include the last value.
    for number in range(first_value, second_value + 1):
        # 'prime' variable is set to true, if composite, becomes false. Resets at every iteration.
        prime = True
        # 'number' is divided by every number from 2 to 'number' (exclusive). If there is no remainder in
        # any of the numbers, then this means that the number is not prime, and 'prime' will then be turned to False.
        for factor in range(2, number):
            if (number % factor) == 0:
                prime = False
            else:
                continue
        if not prime or number <= 1:
            continue
        else:
            print(number, "is prime")

# If the second value is greater than the first value, then the process is repeated with the two values in the range switched.
else:
    print(f"\nIncorrect Input: {first_value} is greater than {second_value}\nThe numbers have been automatically switched.\n")
    print(f"Prime Numbers in the range from: {second_value} and {first_value} are: ")
    for number in range(second_value, first_value + 1):
        prime = True
        for factor in range(2, number):
            if (number % factor) == 0:
                prime = False
            else:
                continue
        if not prime or number <= 1:
            continue
        else:
            print(number, "is prime")

print("\nEND: Project One (01) - Part B\nZanan Virani zvirani5 251346220")
# Closing, like in assignment
