# Search for a number in a tuple using a while loop

numbers = (1, 4, 9, 16, 25, 36, 49, 64, 81, 100)
target = int(input("Enter a number to search for: "))

i = 0
while i < len(numbers):
    if numbers[i] == target:
        print("Number found at index:", i)
        break
    i += 1

if i == len(numbers):
    print("Number is not in the tuple")
