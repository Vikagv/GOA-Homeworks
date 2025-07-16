#. Create a function that takes the parameters word1 and word2 and returns them concatenated together.
# For example, use the arguments "hello" and "friend". (Pronounced: "Hello friend")Create a function that takes the parameters 
# word1 and word2 and returns them concatenated together.
# For example, use the arguments "hello" and "friend". (Pronounced: "Hello friend")

Word1 = input("Please Enter your first word:")
Word2 = input("Please Enter your second word:")

def conect_words(Word1,Word2):
   return "Your Final Word is:" + Word1+ "" + Word2 

print(conect_words(Word1,Word2))