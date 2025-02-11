print("Welcome To The Student Management System!")
student_database = []

while True:
    print("\nPlease choose an option:")
    print("1. Add Student")
    print("2. Remove Student")
    print("3. View Student")
    print("4. View All Students")
    print("5. Exit")
    choice = input("Enter an option(1-5): ")

    if choice == "1":
        name = input("Enter student name: ")
        try:
          age = int(input("Enter student age: "))
        except:
          print("Your age should be a number")    
        course = input("enter student course: ")
        grade = input("enter student grade: ")


        student = {"name":name, "age":age, "course":course, "grade":grade}
        student_database.append(student)
        print(f"{name} has been successfully added to the system!")
        print(student_database)
    

    elif choice == "2":
        rem_student = input("Enter name of student to remove: ")
        for student in student_database:
            if rem_student == student['name']:
              student_database.remove(student)     
              print(f"{rem_student} has been successfully removed")
              break
            else:
               print("Error. Name cannot be found in database")    
            
                  
            
    elif choice == "3":
        view_name = input("Enter name: ")
        for student in student_database:
            if student['name'] == view_name:
                print(f"Name:{student['name']}, Age:{student['age']}, Course:{student['course']}, Grade:{student['grade']}")
                break
            else:
                print("Error. Name cannot be found in database")
    

    elif choice == "4":
        print(student_database)
         

    elif choice == "5":
        print("Exiting Student Management System...")    
        break
    else:
        print("Invalid Input")