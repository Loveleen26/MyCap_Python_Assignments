#Write a Python program to print all positive numbers in a range.

input_str = input("Input List: ")
num_list = [int(x) for x in input_str.split()]
positive = []

for i in num_list:
    if i > 0:
        positive.append(i)

print("Output List:", positive)
