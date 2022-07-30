def printArea(width = 1, height = 2):
    area = width * height
    print("width:", width, "\theight:", height, "\tarea:", area)

printArea()  # Default arguments width = 1 and height = 2
printArea(4, 2.5)  #  Default arguments width = 1 and height = 2
printArea(height = 5, width = 3)  # Keyword arguments width
printArea(width = 1.2)  # Default height = 2
printArea(height = 6.2) # Default width = 1