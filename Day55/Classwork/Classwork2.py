#Ask the user for first name, last name, age, address, then create a function that will pass this data as an
# argument and this function will return one longsentence about the user eg. hello {first name} {surname} you
# live in {residence})
User_Name = input("Please Enter your Name:")
User_Last_Name = input("Please Enter your Last Name:")
User_Age = int(input("Please Enter your Age:"))
User_Address = input("Please Enter your Address:")

def Hello (Name , Lastname, Age, Address):
    return "Hello" + Name + "" + Lastname + "Your Age is" + Age + "You live at " + Address

print (Hello (User_Name , User_Last_Name , User_Age ,  User_Address))