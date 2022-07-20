Import turtle

# Prompt the user for inputting two points
x1, y1 = eval(input("Enter x1 and y1 for point 1:"))
x2, y2 = eval(input("Enter x2 and y2 for point 2:"))

#Compute the distance
distance = ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5
v