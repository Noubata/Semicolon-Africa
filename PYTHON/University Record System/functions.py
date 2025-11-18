THE_COURSES = ( "math", "physics", "computer science", "biology", "chemistry", "statistics", "english", "economics", "history", "philosophy", "sociology", "political science", "geography", "psychology", "art", "music", "engineering", "law", "medicine", "business"
)

def infos_collection(name, age, my_courses, city, zip_code):
 
	my_updated_courses = [cleaned_course.strip() for cleaned_course in my_courses.split(',')]

	valid_courses = {course for course in my_updated_courses if course in THE_COURSES}
    
	a_student = {'name': name, 'age': age, 'courses': valid_courses, 'address': {'city': city, 'zip_code': zip_code}}
	
	return a_student

def student_record(all_students, username):
   
	return all_students.get(username)

def student_courses(all_students, username):
    
	student = all_students.get(username)
	if student:
		return student.get('courses', set())
	return None 

def student_zipcode(all_students, username):

	student = all_students.get(username)
	if student and 'address' in student:
		return student['address'].get('zip_code')
	return None 

def student_city(all_students, username):
   
	student = all_students.get(username)
	if student and 'address' in student:
		return student['address'].get('city')
	return None 

def add_course(all_students, username, new_course):
    
	student = all_students.get(username)
	if not student:
		return "Student not found."

	if new_course not in THE_COURSES:
		return f"Course '{new_course}' is not offered by the university."

	if new_course in student['courses']:
		return "Student is already enrolled in this course."

	student['courses'].add(new_course)
	return "Course added successfully."

def remove_course(all_students, username, course_to_remove):
   
	student = all_students.get(username)
	if not student:
		return "Student not found."

	if course_to_remove in student['courses']:
		student['courses'].remove(course_to_remove)
		return "Course removed successfully."
	else:
		return "Student is not enrolled in this course."

def total_student(all_students):
    
	return len(all_students)