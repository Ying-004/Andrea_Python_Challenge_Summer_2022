#Prompt the user for input
seconds = eval(input("enter an integer for seconds： "))

#Get minutes and remaining second
minutes = seconds//60    # Find minutes in seconds
remainingSeconds = seconds % 60 # Seconds remaining
print(seconds, "Seconds is", minutes,
      "minutes and", remainingSeconds, "seconds")
