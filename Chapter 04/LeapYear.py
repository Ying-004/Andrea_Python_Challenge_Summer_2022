year = eval(input("Enter a year: "))

# Check if the year is a leap year
isLeapYear = (year % 4 == 0 and year % 100 !=0) or \
             (year % 400 == 0)  # 可以被4 整除而不能被100整除

# Display the result
print(year, "is a leap year?", isLeapYear)