def divide(dividend, divisor):
    if divisor == 0:
        raise ZeroDivisionError("Cannot divide by zero.")
    return dividend / divisor

grades = []
print("Calculating average grade...")
try:
    average_grade = divide(sum(grades), len(grades))
except ZeroDivisionError as e:
    print(e)
    print("There are no grades to calculate the average.")
else:
    print(f"The average grade is: {average_grade}")
finally:
    print("Grade calculation complete.")

