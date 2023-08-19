#write a Python program to accept a filename from the user and print the extension of that.

file = input("Input the Filename: ")
parts = file.split(".")

if len(parts) > 1:
    extension = parts[-1]
    print(f"The extension of the file is : '{extension}'")
else:
    print("No extension found.")
