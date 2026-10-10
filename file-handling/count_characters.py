# Count non-whitespace characters in each line of sample.txt.
# Run this script from the file-handling directory.

count = 0

with open("sample.txt", "r", encoding="utf-8") as file:
    lines = file.readlines()
    for line in lines:
        count += len(line.strip())

print("Character count (excluding surrounding whitespace):", count)
