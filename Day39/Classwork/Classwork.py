print("Hello, welcome to my store, please make sure to awnser the following questions")

price = int(input("How much does the item cost?"))
discount = int(input("What discount does the product have?"))

print("Your final price will be:")
final_price = (price * discount) / 100
print(price - final_price)


