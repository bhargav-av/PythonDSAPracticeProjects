# Find the sum of the digits in a given integer.

# Accept the integer number from keyboard and convert that to int.
num = int(input("Enter the integer number you want to sum: "))

# Take the absolute value of the input to handle negative integers
num = abs(num)

result_Sum = 0
# Repeat the process until the last digit
while num > 0:
    # Get the left most digit
    digit = num % 10

    # Sum the digits
    result_Sum = result_Sum + digit

    # Separate the left most digit
    num = num // 10
    print(f"{num} -> {digit}")


# Display the result
print(result_Sum)
