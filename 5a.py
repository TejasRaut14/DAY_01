#Q5. Create a program that checks if a given year is a leap year.

Year=int(input("Enter the year: "))

if (Year % 400==0) and (Year%100==0):
    print("IS A LEAP YEAR")

elif (Year%4==0) and (Year%100!=0):
    print(" Is a leap year")

else:
    print(" Is not leap year")
