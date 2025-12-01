#TASK-1
studentData = {
    'Alice' : 85,
    'Andry' : 75,
    'Bob' : 64,
    'Charlie' : 88,
    'David' : 45
}

studentName = input("Enter the student's name: ")

if studentName in studentData:
    print(f"{studentName}'s marks: {studentData[studentName]}")
else:
    print('Student not found.')