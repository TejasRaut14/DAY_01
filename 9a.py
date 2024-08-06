#Create a program that stops printing numbers when it encounters a number greater than 5 using the
#break statement.
num=int(input("Enter the number :"))

for num in range(1,11):
    if num>5:
        break
    print(num)