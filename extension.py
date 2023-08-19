filename = input("Input the Filename: ")
parts = filename.split(".")

if len(parts) > 1:
    extension = parts[-1]
    print(f"The extension of the file is : '{extension}'")
else:
    print("No extension found.")
