#Q4. Write a Python program that takes an integer input from the user and prints whether the number is
#positive, negative, or zero.

number= int(input("Enter an number : "))

if number==0:
    print("Number is zero")

elif number>=0:
    print("Number is positive")

elif number<0:
    print("Number is negative")