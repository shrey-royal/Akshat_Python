class Student:
    roll_no = None
    name = None
    age = None
    marks = None
    standard = None
    section = None
    gender = None
    fees = None

# create a list to store the student objects
students = []

# scan the details of two students
for i in range(2):
    s = Student()
    s.roll_no = input(f"Enter roll number of student {i+1}: ")
    s.name = input(f"Enter name of student {i+1}: ")
    s.age = input(f"Enter age of student {i+1}: ")
    s.marks = input(f"Enter marks of student {i+1}: ")
    s.standard = input(f"Enter standard of student {i+1}: ")
    s.section = input(f"Enter section of student {i+1}: ")
    s.gender = input(f"Enter gender of student {i+1}: ")
    s.fees = input(f"Enter fees of student {i+1}: ")
    students.append(s)  # add the student object to the list
    # clear screen
    print("\033c")  # (clears the screen)

# print the details of all students in tabular format
print("Roll No.\tName\tAge\tMarks\tStandard\tSection\tGender\tFees")
for s in students:
    print("{}\t\t{}\t{}\t{}\t\t{}\t{}\t{}\t{}".format(s.roll_no, s.name, s.age, s.marks, s.standard, s.section, s.gender, s.fees))
