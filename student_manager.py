students = []
students_last_added = []
adding = True


def get_last_id():
	try:
		f = open("students_record.txt", "r")
		line_count = len(f.readlines())
		f.close()
		return line_count
	except Exception:
		print("Empty file")
		f = open("students_record.txt", "a")
		f.close()
		return 0


id_count = get_last_id()

def menu():
	global id_count
	global adding

	def display_menu():
		x = "\n---menu---"
		print(x.upper())
		print("Select letter to get started: \n")
		print("A. Add New Student\t\tB. Print List From Array")
		print("C. Save to/Update File\t\tD. Print List From File\n")
		print("Press any key to exit.\n")
		return input("Enter Letter:\t")


	def add_student(student_name, student_id):
		student = {"student_id": student_id, "student_name": student_name}
		students.append(student)
		students_last_added.append(student)


	def print_array():
		print(students)


	def print_file_content():
		f = open("students_record.txt", "r")
		print("-------------------------")
		print("|ID|NAME\t\t|")
		print("-------------------------")
		for line in f.readlines():
			l = line.split(",")
			print("| " + str(l[0]) + "|" + l[1].replace("\n", ""))
		f.close()


	def save_to_file():
		global students_last_added
		f = open("students_record.txt", "a")
		for student in students_last_added:
			f.write(str(student["student_id"]) + "," + student["student_name"] + "\n")
		f.close()
		students_last_added = []


	ask = display_menu()
	letter = ask.lower()
	if letter == "a":
		id_count += 1
		new_student = input("Enter student name:\t")
		add_student(new_student, id_count)
	elif letter == "b":
		print_array()
	elif letter == "c":
		save_to_file()
	elif letter == "d":
		print_file_content()
	else:
		adding = False
	print("\n-------------------------\n\n\n\n\n")


while(adding == True):
	menu()


print("Program terminated...")