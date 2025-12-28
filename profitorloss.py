print("PROFIT OR LOSS CALCULATION")
cost_price=int(input("Enter the Cost Price: "))
selling_price=int(input("Enter the Selling Price: "))

if selling_price > cost_price:
    profit = selling_price - cost_price
    print("You made a profit of:", profit)

elif selling_price < cost_price:
    loss = cost_price - selling_price
    print("You incurred a loss of:", loss)

else:
    print("There is no profit or loss.")
print("**************")



