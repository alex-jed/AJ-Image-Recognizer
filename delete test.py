checks_for_blank_spaces = [33, 170, 216, 320, 368, 479, 1251, 1336, 1384, 1510]

row_of_single_characters = [5,4,2,0,1]
avg_letter_size = 100


# adds blank spaces
row_of_single_characters_with_spaces = []
adder = 0

# checks for blanks spaces at the start of the row of written characters
if checks_for_blank_spaces[0] > avg_letter_size:
    for count in range(checks_for_blank_spaces[0]//avg_letter_size):
        row_of_single_characters_with_spaces.append("")
row_of_single_characters_with_spaces.append(row_of_single_characters[adder])
adder+=1

# checks for blank spaces between the rest of the characters
for side in range(1, len(checks_for_blank_spaces)-1, 2):
    if checks_for_blank_spaces[side + 1] - checks_for_blank_spaces[side] > avg_letter_size:
        for count in range((checks_for_blank_spaces[side + 1] - checks_for_blank_spaces[side])//avg_letter_size):
            row_of_single_characters_with_spaces.append("")
    row_of_single_characters_with_spaces.append(row_of_single_characters[adder])
    adder += 1

# checks for blank spaces at the end of the row of written characters
if 2214 - checks_for_blank_spaces[-1] > avg_letter_size:
    print(f"{(2214 - checks_for_blank_spaces[-1])//avg_letter_size} SPACES AT THE END")
    for count in range((2214 - checks_for_blank_spaces[-1])//avg_letter_size):
        row_of_single_characters_with_spaces.append("")

print(row_of_single_characters_with_spaces)
