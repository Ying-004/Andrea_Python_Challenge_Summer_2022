# Receive the amount
amount = eval(input("Enter an amount, for example. 11.56: "))

#Convert the amount to cents
remainingAmount = int(amount * 100)

# Find the number of one dollars
numberOfOneDollars = remainingAmount // 100
remainingAmount= remainingAmount % 100

# Find the number of quarters
numberOf