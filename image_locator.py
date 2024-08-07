import numpy as np
import matplotlib.pyplot as plt

def find_text(whole_matrix, tolerance):
    # once image has been located, is stored here
    stored_character_matrices = []

    # stores the sum of greyscale values of each row to
    # where the rows of written text
    whole_matrix_row_sums = []
    for row in whole_matrix:
        whole_matrix_row_sums.append(np.sum(row))

    # calculates how far from each the max value each other value is
    max_row_value = np.max(whole_matrix_row_sums)
    distance_from_max_whole_row_sums = []
    for count in range(len(whole_matrix_row_sums)):
        distance_from_max_whole_row_sums.append((max_row_value - whole_matrix_row_sums[count]) / max_row_value)



    # checks where new row of written text starts
    nr_of_edges_of_row_of_written_text = 0
    for i in range(len(distance_from_max_whole_row_sums)):

        row_of_single_characters = []  # stores final matrix once image has been found

        if distance_from_max_whole_row_sums[i] >= tolerance and nr_of_edges_of_row_of_written_text == 0:
            top_edge_of_row_of_written_text = i
            nr_of_edges_of_row_of_written_text += 1

        if distance_from_max_whole_row_sums[i] < tolerance and nr_of_edges_of_row_of_written_text == 1:
            bottom_edge_of_row_of_written_text = i
            nr_of_edges_of_row_of_written_text += 1

        # scans for individual numbers in that row once row of written text has been found
        if nr_of_edges_of_row_of_written_text == 2:
            checks_for_blank_spaces = []
            print("ROW STARTS AT", top_edge_of_row_of_written_text, "AND ENDS AT", bottom_edge_of_row_of_written_text)
            print()

            # resets number of edges to begin looking for new row of written text
            nr_of_edges_of_row_of_written_text = 0

            # returns isolated row to begin looking for numbers in that row
            matrix_row = whole_matrix[top_edge_of_row_of_written_text:bottom_edge_of_row_of_written_text]

            ##### the above isolates the row #####
            #####below isolates each number #####

            nr_of_sides_of_characters = 0

            # same as above function but for columns of isolated row
            col_sums = []
            for count in range(np.shape(matrix_row)[1]):
                col_sums.append(np.sum(matrix_row[:, count]))

            max_col_value = np.max(col_sums)
            new_col_sums = []
            for count in range(len(col_sums)):
                new_col_sums.append((max_col_value - col_sums[count]) / max_col_value)

            # plt.plot(new_col_sums, label="column sum")
            # plt.legend()
            # plt.show()

            # scans for individual character in the isolated row

            for j in range(len(new_col_sums)):

                if new_col_sums[j] >= tolerance and nr_of_sides_of_characters == 0:
                    character_left_edge = j
                    checks_for_blank_spaces.append(character_left_edge)
                    nr_of_sides_of_characters += 1

                if new_col_sums[j] < tolerance and nr_of_sides_of_characters == 1:
                    character_right_edge = j
                    checks_for_blank_spaces.append(character_right_edge)
                    nr_of_sides_of_characters += 1

                # trims the blank spaces of the isolated characters
                if nr_of_sides_of_characters == 2:

                    print("CHARACTER STARTS AT", character_left_edge, "AND ENDS AT", character_right_edge)

                    # resets nr_of_sides_of_characters to begin looking for new character
                    nr_of_sides_of_characters = 0

                    # returns a matrix of the single character with potentially some blank rows
                    single_number_matrix = whole_matrix[
                                           top_edge_of_row_of_written_text:bottom_edge_of_row_of_written_text,
                                           character_left_edge:character_right_edge]

                    ##### the above finds the individual numbers in the row #####
                    ##### below we trim any blank spaces #####

                    # same as above but for the individual character
                    single_number_matrix_row_sums = []
                    for row in single_number_matrix:
                        single_number_matrix_row_sums.append(np.sum(row))

                    max_row_value_single_number = np.max(single_number_matrix_row_sums)
                    normalized_single_number_row_sums = []
                    for count in range(len(single_number_matrix_row_sums)):
                        normalized_single_number_row_sums.append((max_row_value_single_number - single_number_matrix_row_sums[count]) / max_row_value_single_number)

                    # plt.plot(normalized_single_number_row_sums, label="column sum")
                    # plt.legend()
                    # plt.show()

                    # checks exactly where the character is
                    nr_of_single_character_sides = 0
                    for k in range(len(normalized_single_number_row_sums)):

                        if normalized_single_number_row_sums[k] >= tolerance and nr_of_single_character_sides == 0:
                            single_number_top = k
                            nr_of_single_character_sides += 1

                        if (normalized_single_number_row_sums[k] < tolerance and nr_of_single_character_sides == 1) or (k == (np.shape(single_number_matrix)[0] - 1)):
                            single_number_bottom = k
                            nr_of_single_character_sides += 1

                        # trims the fat blank lines of the single numbers
                        if nr_of_single_character_sides == 2:
                            print("BLANKS STARTS AT", single_number_top, "AND ENDS AT", single_number_bottom)


                            # resets number of edges to begin looking again
                            nr_of_single_character_sides = 0

                            # returns trimmed matrix
                            trimmed_single_number_matrix = single_number_matrix[single_number_top:single_number_bottom]

                            print(checks_for_blank_spaces)
                            print()
                            # saves the new character to the row matrix
                            row_of_single_characters.append(trimmed_single_number_matrix)

            # finds average size of the letters to use for spacings
            letter_sizes = []
            for side in range(1,len(checks_for_blank_spaces),2):
                letter_sizes.append(checks_for_blank_spaces[side] - checks_for_blank_spaces[side-1])
            avg_letter_size = sum(letter_sizes)/len(letter_sizes)

            # adds blank spaces to the rows
            row_of_single_characters_with_spaces = []
            adder = 0
            print(checks_for_blank_spaces[0] // avg_letter_size)
            # checks for blanks spaces at the start of the row of written characters
            if checks_for_blank_spaces[0] > avg_letter_size:
                for count in range(int(checks_for_blank_spaces[0] // avg_letter_size)):
                    row_of_single_characters_with_spaces.append("")
            row_of_single_characters_with_spaces.append(row_of_single_characters[adder])
            adder += 1

            # checks for blank spaces between the rest of the characters
            for side in range(1, len(checks_for_blank_spaces) - 1, 2):
                if checks_for_blank_spaces[side + 1] - checks_for_blank_spaces[side] > avg_letter_size:
                    for count in range(int(
                            (checks_for_blank_spaces[side + 1] - checks_for_blank_spaces[side]) // avg_letter_size)):
                        row_of_single_characters_with_spaces.append("")
                row_of_single_characters_with_spaces.append(row_of_single_characters[adder])
                adder += 1

            # checks for blank spaces at the end of the row of written characters
            if 2214 - checks_for_blank_spaces[-1] > avg_letter_size:
                for count in range(int((2214 - checks_for_blank_spaces[-1]) // avg_letter_size)):
                    row_of_single_characters_with_spaces.append("")

            stored_character_matrices.append(row_of_single_characters_with_spaces)
            print()
            print()
            print()
    return stored_character_matrices



