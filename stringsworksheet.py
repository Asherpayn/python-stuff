# vscode.dev works but when connecting to a github codespace the connection fails with network error
# from powerpoint
age = 14
print("Kumar " + "Ahmad are " + str(age) + " years old")

# from worksheet

# saving first and last names to variables
firstname = input("What is your first name?")
surname = input("What is your last name?")

# printing various stuff using the variables above
print ("Hello,", firstname)
print ("Your surname is,", surname)
print ("Hello,", firstname, surname)
print("Your initials are:", firstname[0], surname[0])
print(firstname.upper() + " " + surname.upper())
# saving fullname - the " " adds space between the variables
fullname = firstname + " " + surname
print(fullname)
print("There are " + str(len(firstname)) + " letters in your first name")

# username generation
# is there a faster way to do this?
print("Your username could be: " + surname[0] + surname[1] + surname[2] + str(len(surname)))
