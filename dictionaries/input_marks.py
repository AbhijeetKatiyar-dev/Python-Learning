# Store subject marks entered by the user in a dictionary

subjects = {}

physics = int(input("Enter your physics marks: "))
subjects.update({"physics": physics})

chemistry = int(input("Enter your chemistry marks: "))
subjects.update({"chemistry": chemistry})

maths = int(input("Enter your maths marks: "))
subjects.update({"maths": maths})

print("Subject marks:", subjects)
