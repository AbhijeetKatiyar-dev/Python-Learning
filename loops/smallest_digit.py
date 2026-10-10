# Find the smallest digit in a non-negative integer

num = int(input("Enter a non-negative integer: "))

if num < 0:
    print("Please enter a non-negative integer.")
else:
    smallest = 9

    if num == 0:
        smallest = 0
    else:
        while num > 0:
            digit = num % 10
            if digit < smallest:
                smallest = digit
            num //= 10

    print("Smallest digit is:", smallest)
