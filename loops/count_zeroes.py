# Count zero digits in a non-negative integer

num = int(input("Enter a non-negative integer: "))

if num < 0:
    print("Please enter a non-negative integer.")
else:
    count = 0

    # The number 0 itself contains one zero digit.
    if num == 0:
        count = 1
    else:
        while num > 0:
            digit = num % 10
            if digit == 0:
                count += 1
            num //= 10

    print("Total number of zeroes:", count)
