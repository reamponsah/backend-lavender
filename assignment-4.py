# store personal details (like name, age and favorite colors) in variables and dictionaries

name = input("what is your name?: ")
try: 
     age = int(input("how old are you?: "))
except ValueError:
     print("Your age should be a number")
except Exception as e:
     print("Error: ", e)    
fav_color = input("what is your favorite color?: ")

personal_details = {"name": name,
 "age" : age, 
 "favorite_color" : fav_color}

print(personal_details)

# Store a list of friends' names
friends_input = input("what are your friends names: ")
friends_names = friends_input.split()
print(friends_names)

# allow a user to update their personal information, like age and favorite color
update_info = input("would you like to update your details? 'Yes'/'No': ").capitalize()
if update_info == "Yes": 
     name_update = input("what is your name?: ")
     age_update = input("how old are you?: ")
     fav_color_update = input("what is your favorite color?: ")
     updated_personal_dictionary = {"name": name_update, "age": age_update, "favorite_color": fav_color_update} 
     personal_details.update(updated_personal_dictionary)
     print(personal_details)
else:
     print("Okay!") 

  