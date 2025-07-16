#.Create a function that takes a name parameter and returns the message "Hello, [name]".
# For example, use the argument "Anna". (Pronounced: "Hello, Anna")

Name = input(" Please Enter Your Name:")

def Say_Hello(Name):
    return "Hello," + Name

print(Say_Hello(Name))