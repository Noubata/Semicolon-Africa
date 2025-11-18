from functions import *

all_students = {}

while True:

	print("""
	----------------------------------------------
	Bright Future University Record System

	1.  Add student
	2.  Student record
	3.  Student courses
	4.  Student city
	5.  Student zip code
	6.  Add course to student's record
	7.  Remove course from student's record
	8.  Display total number of students
	0. Exit
	----------------------------------------------
	""")
	try:
		choice = int(input("choose from above: "))
		if choice < 0:
			print("Only positive integer is accepted!!")
			continue
	except ValueError:
		print("The input must be an integer")
		continue

	match choice:
		case 1:
			try:
				name = input("Enter student name (this will be an username too): ").lower()
				age = int(input("Enter student age: "))
			except ValueError:
				print("Age must be an integer. Student not added.")
				continue
            
			my_courses= input("Enter student courses, separated by commas: ").lower()
			city = input("Enter student city: ").lower()
			zip_code = input("Enter student zip code: ").lower()

			if name in all_students:
				print(f"{name} already exists. Please choose a unique name.")
				continue
			all_students[name] = infos_collection(name, age, my_courses, city, zip_code)
			print(f"{name} successfully added")

		case 2:
			username = input("Enter student name to retrieve record: ")
			record = student_record(all_students, username)
			if record:
				print(f"Record for {username}:\n{record}")
			else:
				print(f"Student {username} not found.")

		case 3:
			username = input("Enter student name to view courses: ")
			courses = student_courses(all_students, username)
			if courses is not None:
				print(f"{username}'s Courses are:\n{courses}")
			else:
				print(f"Student {username} not found.")

		case 4:
			username = input("Enter student name to view city: ")
			city = student_city(all_students, username)
			if city:
				print(f"{username}'s City is: {city}")
			else:
				print(f"Student {username} not found")

		case 5:
			username = input("Enter student name to view zip code: ")
			zipcode = student_zipcode(all_students, username)
			if zipcode:
				print(f"{username}'s Zip Code is: {zipcode}")
			else:
				print(f"Student {username} not found")

		case 6:
			username = input("Enter student name to add a course: ")
			new_course = input("Enter the course to add: ")
			result = add_course(all_students, username, new_course)
			print(result)

		case 7:
			username = input("Enter student name to remove a course: ")
			course_to_remove = input("Enter the course to remove: ")
			result = remove_course(all_students, username, course_to_remove)
			print(result)

		case 8:
			total = total_student(all_students)
			print(f"Total number of students recorded: {total} ")

		case 0:
			print("Bright Future University Record System. Goodbye!")
			break

        