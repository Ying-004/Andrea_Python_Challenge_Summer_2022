# Print grade for the score
def getGrade(score):
    if score >= 90.0:
        return'A'
    elif score >= 80.0:
        return'B'
    elif score >= 70.0:
        return'C'
    else:
        return'F'

def main():
    score = eval (input("Enter a score: "))
    print("The grade is ", getGrade(score))

main()  # Call the main function)