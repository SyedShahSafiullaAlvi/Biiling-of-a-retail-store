# Biiling-of-a-retail-store
'''A python program prompting the user to enter the price and ask for quantity. A revelant discount is applied based on some criterias. Atlast a structured bill is printed.'''

print("\t***ABC Retail Store***")
items=int(input("Enter the numner of items purchased: "))
price=float(input("Enter the total amount: "))

print("\n\nItems purchased: \t{}\nTotal amount:\t\t{}\n".format(items,price))

if price>100 and price<199.99:
    print("Yay! Discount of 10% is applied.")
    discount=10/100*price

elif price>200 and price<299.99:
    print("Yay! Discount of 15% is applied.")
    discount=15/100*price

elif price>300 and price<499.99:
    print("Yay! Discount of 20% is applied.")
    discount=20/100*price

elif price>500:
    print("Yay! Discount of 25% is applied.")
    discount=25/100*price
    
finalAmount=price-discount

print("Discount amount:\t{}\n----------------------------------\nFinal Amount:\t\t{}\n---------------------------------".format(discount,finalAmount))
print("---Thank you!! Visit again---")