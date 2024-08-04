import file
import image_locator
import image_recognizer
import numpy as np

#file.display_rbg_image(file.get_image("download test"))




def user_interface():

    testable_characters = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]


    full_greyscale_matrix = file.rgb_to_grayscale(file.get_image("big image"))

    characters_to_guess = image_locator.find_text(full_greyscale_matrix)
    # for i in range(len(characters_to_guess)):
    #     for j in range(len(characters_to_guess[i])):
    #         file.display_grayscale_image(characters_to_guess[i][j])



    final_text = []
    for count_i in range(len(characters_to_guess)):
        row = []
        for count_j in range(len(characters_to_guess[count_i])):
            guess = image_recognizer.image_recogniser(characters_to_guess[count_i][count_j])
            shrunk_greyscale_matrix = image_recognizer.shrink_image(characters_to_guess[count_i][count_j], 32)
            file.display_grayscale_image(shrunk_greyscale_matrix)
            print(f"The Image Recognizer thinks this is a {guess}")

            # corrects heatmap is guess is wrong
            correct = False
            while not correct:
                user_answer = input("Is this correct? (y/n): ")
                if user_answer != "y":
                    actual = input("What is it actually?: ")
                    actual_heatmap = file.read_heatmap(actual)
                    actual_heatmap += (len(testable_characters) - 1) * shrunk_greyscale_matrix * np.ones((32, 32))
                    file.write_heatmap(actual_heatmap, str(actual) + " heatmap")

                    new_guess = image_recognizer.image_recogniser(characters_to_guess[count_i][count_j])
                    file.display_grayscale_image(shrunk_greyscale_matrix)
                    print(f"The Image Recognizer thinks this is a {new_guess}")
                # returns guessed character if correct
                if user_answer == "y":
                    row.append(guess)
                    correct = True
        final_text.append(row)
    return final_text
written_text = user_interface()


# greyscale_matrix = file.rgb_to_grayscale(file.get_image("big image"))
# matricies = image_locator.find_text(greyscale_matrix)
# full_number_picture = []
#
# for count_i in range(len(matricies)):
#     row = []
#     #print("count_i", count_i)
#     for count_j in range(len(matricies[count_i])):
#         number_identified = image_recognizer.image_recogniser(matricies[count_i][count_j])
#         row.append(number_identified)
#     full_number_picture.append(row)
#
#
# for i in full_number_picture:
#     print(i)
