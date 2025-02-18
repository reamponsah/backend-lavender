def welcome_message():
    print("Welcome To The Student Database Management System")
welcome_message()

student_database = {}

def menu():    
        print("1. Add a student")
        print("2. Update student records")
        print("3. Calculate and display average grade of students")
        print("4. Display all student records")
        print("5. Exit")
    
# Add new students
def add_student():
            name = input("Enter student name: ")
            try:
                age = int(input("Enter student age: "))
                grade = int(input("enter student grade: "))
            except:
                print("Invalid input. Should be a number")     
            student = {name : {"age":age, "grade":grade}}
            student_database.update(student)
            print(f"{name} has successfully been added to the system")
            print(student_database)

# Update existing student records
def update_records():
    stu_update = input("Enter name of student to update: ")
    

    if stu_update in student_database:
        update_input = input("Which info would you like to update?: \n1. Age\n2. Grade\nEnter option here: ")
        
        if update_input == "1":
            upd_age = input("Enter new age: ")
            student_database[stu_update]['age'] = upd_age
            print("Age has been succesfully updated")
            print(student_database)
            
        elif update_input == "2":
            upd_grade = input("Enter new grade: ")  
            student_database[stu_update]['grade'] = upd_grade
            print("Grade has been successfully updated")
            print(student_database)
    
    else:
        print("Student not found!")  
        

        
#Calculate and display the average grade of all students
def average_grade():
    total_grade = sum(student['grade'] for student in student_database.values())
    avg_grade = total_grade / len(student_database)
    print("Average grade of students:", avg_grade)



#Display all student records        
def display_all_students():
    for name, data in student_database.items():
        print(f"Name: {name}, Age: {data['age']}, Grade: {data['grade']}")            






while True:
    menu()

    choice = input("Please choose an option(1-5): ")

    if choice == "1":
        add_student()
    elif choice == "2":
        update_records()
    elif choice == "3":
        average_grade()  
    elif choice == "4":
        display_all_students()  
    elif choice == "5":
        print("Exiting System...")
        break           


    else:
        print("Invalid Choice! Please try again")
