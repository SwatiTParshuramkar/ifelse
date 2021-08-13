quantity=int(input("Enter the amount"))
discount=0
if quantity>1000:
    discount=discount+(10/100*quantity)
    print("Your amount is to pay",quantity - discount)
else:
    print(quantity)