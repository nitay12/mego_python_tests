# If a string contains at least two "A" characters but not contains the sequence "AA"
# it called a "Valid String"
# Write a program that gets 23 strings
# the program will calculate and print the number of "Valid Strings"

# Solution
valid_strings_count = 0
for i in range(2):
    user_input = input("Enter a string: ")
    last_letter = ""
    a_letter_count = 0
    for char in user_input:
        has_a_sequence = False
        if char == "A":
            if last_letter == "A":
                has_a_sequence = True
            else:
                a_letter_count += 1
        last_letter = char
    if a_letter_count >= 2 and has_a_sequence == False:
        valid_strings_count += 1
        
print(f"Number of Valid Strings: {valid_strings_count}")
