# Practicing sets in Python

numbers = {1, 2, 3, 4, 5}
print("Type:", type(numbers))

numbers.add(7)
print("After adding 7:", numbers)

numbers.remove(2)
print("After removing 2:", numbers)

# pop() removes an arbitrary element from a set.
numbers.pop()
print("After pop():", numbers)

numbers.clear()
print("After clear():", numbers)
print("Number of elements:", len(numbers))

# Sets keep only unique values.
languages = {
    "python", "java", "C++", "python", "javascript",
    "java", "python", "java", "C++", "C"
}
print("Unique languages:", languages)
print("Number of unique languages:", len(languages))

values = {("float", 9.0), ("int", 9)}
print("Tuple values:", values)
print("Type:", type(values))
