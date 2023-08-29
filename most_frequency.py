#Write Python code to create a function called most_frequent that takes a string
#and prints the letters in decreasing order of frequency. Use dictionaries.
def most_frequent(string):
    d = dict()
    for key in string:
        if key not in d:
            d[key] = 1
        else:
            d[key] += 1
    return d

input_string = input("Please enter a string: ")
frequency_dict = most_frequent(input_string)

sorted_chars = sorted(frequency_dict.keys(), key=lambda x: frequency_dict[x], reverse=True)

for char in sorted_chars:
    print(f"{char} = {frequency_dict[char]:02d}")


