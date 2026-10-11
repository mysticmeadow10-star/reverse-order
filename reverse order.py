#Write a program to print the numbers in reverse order beginning from the number entered by the user.

n = int(input("Enter a number:"))

for i in range(n, -1, -1):
    print(i)