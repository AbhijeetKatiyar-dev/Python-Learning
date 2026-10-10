# Practicing dictionaries in Python

student = {
    "name": "Abhijeet",
    "subjects": {
        "physics": 97,
        "chemistry": 98,
        "maths": 99,
    },
}

student.update({"city": "Delhi"})
print("Student:", student)

word_meanings = {
    "table": ["a piece of furniture", "a list of facts and figures"],
    "cat": "a small animal",
}
print("Word meanings:", word_meanings)
