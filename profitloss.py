#take two imput costprice and market price, then find profit loss or no profit or no loss. if profit print by how much and if loss print by how much if not print 0 

cost = float(input(" Enter the cost price: "))
selling = float(input(" Enter the market price: "))

price = 0 
if selling > cost:
    print(f"Profit: ${selling - cost}")
elif selling < cost:
    print(f" Loss: ${ cost - selling }")
else:
    print("No proft, No loss")
