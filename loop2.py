"""
while True:
    age = int(input("How old are you? "))

    if age < 18:
        print("Invalid age, please try again")
        continue
    else:
        break

---------------

while True:
    n = int(input("What's n? "))
    if n > 0:
        break

for i in range(n):
    print(f"Travazap {i}")

for student in students:
    print(student)
"""

#data type called strings
students = ["Hermione", "Harry", "Ron", "Draco Malfoy"]
#print(students[3])

for i in range(len(students)):
    print(i + 1, students[i])