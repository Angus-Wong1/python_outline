student1 = Student("Alice", "123456", "Computer Science")
student1.insert_student()
student2 = Student("Bob", "234567", "Mathematics")
student2.insert_student()

course1 = Course("Data Structures", "CS101", "Professor Smith")
course1.insert_course()
course2 = Course("Calculus", "MAT201", "Professor Johnson")
course2.insert_course()

print(Student.retrieve_all_students())
# [("Alice", "123456", "Computer Science"), ("Bob", "234567", "Mathematics")]
print(Course.retrieve_all_courses())
# [("Data Structures", "CS101", "Professor Smith"), ("Calculus", "MAT201", "Professor Johnson")]
