# define ng empty list na students at students_last_added.
# Ia-append lahat ng record sa variable students.
# Ilalagay temporarily sa variable students_last_added yung bagong nadagdag
# add = True, gagamitin para sa while loop
students = []
students_last_added = []
adding = True

#~~~~~ START NG GET_LAST_ID FUNCTION DECLARATION ~~~~
# definition ng get_last_id function
# kapag nage-exist yung students_record.txt, kuhain yung last number mula sa file
# pero kung hindi naman, gagawa ng students_record.txt tapos magsisimula yung id number sa 0
def get_last_id():
	try:
		f = open("students_record.txt", "r")
		line_count = len(f.readlines())
		f.close()
		return line_count # return yung last id na galing sa file
	except Exception:
		print("Empty file")
		f = open("students_record.txt", "a")
		f.close()
		return 0 # return integer 0 kung walang file na nage-exist

#~~~~~ END NG GET_LAST_ID FUNCTION DECLARATION ~~~~

# i-assign sa id_count variable yung nakuhang number mula sa
# get_last_id function.
id_count = get_last_id()

#~~~~~ START NG MENU FUNCTION DECLARATION ~~~~
# define ng menu function
def menu():
	# kuhain yung values ng id_count, at adding variables
	# kailangan gumamit ng global keyword dahil sa labas sila ng
	# menu function naka-declare
	global id_count
	global adding

	#~~~~~ START NG DISPLAY_MENU, ADD_STUDENT, PRINT_ARRAY, SAT_TO_FILE FUNCTION DECLARTIONS ~~~~
	# function para mag-display ng menu
	def display_menu():
		x = "\n---menu---"
		print(x.upper())
		print("Select letter to get started: \n")
		print("A. Add New Student\t\tB. Print List From Array")
		print("C. Save to/Update File\t\tD. Print List From File\n")
		print("Press any key to exit.\n")
		return input("Enter Letter:\t") # kuhain yung letter na ilalagay ng user


	# function para sa pag-add ng student sa students at students_last_added list or array.
	# tatanggap ng dalawang arguments, yung pangalan ng student at yung magiging id niya
	def add_student(student_name, student_id):
		student = {"student_id": student_id, "student_name": student_name} # gawa ng dictionary (key:value)
		students.append(student) # append sa dulo ng students
		students_last_added.append(student)


	# function para i-print yung students list.
	def print_array():
		print(students)


	# function para i-print yung laman ng students_record.txt
	def print_file_content():
		f = open("students_record.txt", "r")
		print("-------------------------")
		print("|ID|NAME\t\t|")
		print("-------------------------")
		for line in f.readlines():
			l = line.split(",") # i-convert yung 1,myName into [1, "myName"] na list at i-assign sa l variable
			# sa ngayon, ang value ng l[0] ay 1 tapos ang l[1] ay myName
			print("| " + str(l[0]) + "|" + l[1].replace("\n", ""))
			# sa .replace() function, binura lang natin yung \n na characters
		f.close()


	# function para i-save (append) sa file yung naidagdag na names
	def save_to_file():
		global students_last_added # kailangan kuhain yung students_last_added para
		# mabura nating yung laman niya at mapalitan ng bago
		# example na laman ng students_last_added array [{"student_id": 10, "student_name": "John"},{"student_id:", 11, "student_name": "Cristi"}]
		f = open("students_record.txt", "a")
		for student in students_last_added:
			f.write(str(student["student_id"]) + "," + student["student_name"] + "\n")
			# sa unang loop, ang output ay 10,John: 
			# sa pangalawang loop, ang output ay 11,Cristi: 
		f.close()
		students_last_added = [] # tapos burahin yung laman niya para mapalitan ng bago
		# kailangan burahin para hindi ma-doble yung record sa text file kapag
		# tinawag ulit yung function na 'to.

	#~~~~~ END NG DISPLAY_MENU, ADD_STUDENT, PRINT_ARRAY, SAVE_TO_FILE FUNCTION DECLARTIONS ~~~~
	
	# DITO TATAWAGIN AT GAGAMITIN YUNG APAT FUNCTIONS:

	ask = display_menu() # tawagin yung display_menu function tapos ilagay sa ask variable
	# yung ire-return na inputted string ng user which is yung letter.

	letter = ask.lower() # i-convert sa lowercase character yung nakuhang letter.
	# i-check kung anong letter yung ininput:
	if letter == "a":
		id_count += 1 # increment natin ng isa yung id para walang kapareho
		new_student = input("Enter student name:\t")
		# ipasa natin sa function yung laman ng new_student para mai-append
		# na siya sa students at students_last_added na list.
		add_student(new_student, id_count)
	elif letter == "b":
		# kung b, i-print lang yung lamang ng students list.
		print_array()
	elif letter == "c":
		# kung c, i-save sa text file yung laman ng students_last_added
		save_to_file()
	elif letter == "d":
		# kung d, i-print yung laman ng text file
		print_file_content()
	else:
		# pero kung wala sa option yung letter na binigay ng user,
		# palitan yung value ng adding na variable,
		adding = False
	print("\n-------------------------\n\n\n\n\n")

#~~~~~ END NG MENU FUNCTION DECLARATION ~~~~

# nasa labas na tayo ng menu function
# hangga't ang value ng adding variable ay True,
# i-run lang nang i-run yung menu function
# kapag nag-input ng ibang letter yung user,
# i-reassign ang value ng adding variable, at gawing False,
# saka lang mabe-break yung while loop
while(adding == True):
	menu()

# kapag na-break yung while loop, diretso siya dito at magpi-print 'to:
print("Program terminated...")