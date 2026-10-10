# Search a tuple using a for loop and track the index

numbers = (1, 4, 9, 16, 25, 36, 49, 64, 81, 100)
target = int(input("Enter a number to search for: "))

index = 0
found = False

for value in numbers:
    if value == target:
        print("Number found at index:", index)
        found = True
        break
    index += 1

if not found:
    print("Number is not in the tuple")
