# Accept three numbers from user and print the largest number using ternary operators

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
num3 = int(input("Enter the third number: "))
largestNumber = (
    "num1 is largest" if num1 > num2 and num1 > num3 else
    "num2 is largest" if num2 > num1 and num2 > num3 else
    "num3 is largest"
)
print("The largest number is: ", largestNumber)
