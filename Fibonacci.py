#Write a Python Program for Fibonacci numbers.

n = int(input("Enter the number of terms: "))

a=0
b=1
print("Fibonacci sequence:")
for i in range(n):
    print(a, end=" ")
    temp = a
    a = b
    b = temp + b

