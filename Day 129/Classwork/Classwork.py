#Write a function that takes a number as an argument and returns the square of that number.

def square(sq):
    return sq * sq 

#2) Write a function that takes a number as an argument. If the number is even --> returns "odd", if it is odd --> "even".

def oddoreven(oe):
    if oe / 2:
        return "even"
    else:
        return "odd"
    
#3) In the form of a comment, indicate how the .split() method works and give 2 examples of its use.
# it splits a string into lists

Hi = "Hello World"

X = Hi.split()
print(X)

#In the comment, indicate how the .join() method works and give 2 examples of its use
#the join method joins all the items in the list using a seperator, for an example a !

mylist = ("Vika","Taso","kato")

X = "!".join(mylist)
print(X)