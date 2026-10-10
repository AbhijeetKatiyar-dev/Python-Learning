# Check whether an integer is a palindrome

num = int(input("Enter an integer: "))

if num < 0:
    print("Your number is not a palindrome")
else:
    original = num
    reversed_num = 0

    while num > 0:
        digit = num % 10
        reversed_num = reversed_num * 10 + digit
        num //= 10

    if original == reversed_num:
        print("Your number is a palindrome")
    else:
        print("Your number is not a palindrome")
