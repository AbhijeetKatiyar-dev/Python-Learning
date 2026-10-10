# Calculate the sum of the digits of an integer

num = int(input("Enter an integer: "))
num = abs(num)
digit_sum = 0

while num != 0:
    digit = num % 10
    digit_sum += digit
    num //= 10

print("The sum of digits is:", digit_sum)
