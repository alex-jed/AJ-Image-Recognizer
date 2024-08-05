import file
import image_locator
import image_recognizer

def user_interface():
    testable_characters = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

    full_greyscale_matrix = file.rgb_to_grayscale(file.get_image("big image"))

    characters_to_guess = image_locator.find_text(full_greyscale_matrix, 0.01)

    final_text = []
    for count_i in range(len(characters_to_guess)):
        row = []
        for count_j in range(len(characters_to_guess[count_i])):
            correct = False
            while not correct:

                # generates guess and shows you what character is currently being guessed
                guess = image_recognizer.image_recogniser(characters_to_guess[count_i][count_j])
                shrunk_greyscale_matrix = image_recognizer.shrink_image(characters_to_guess[count_i][count_j], 32)
                file.display_grayscale_image(shrunk_greyscale_matrix)
                print(f"The Image Recognizer thinks this is a {guess}")
                actual = int(input("What is it actually?: "))

                if actual != guess:
                    # removed number matrix to the wrong heatmaps
                    wrong_heatmap = file.read_heatmap(guess)
                    wrong_heatmap -= shrunk_greyscale_matrix
                    file.write_heatmap(wrong_heatmap, str(guess) + " heatmap")

                    # adds number matrix to the correct heatmap
                    correct_heatmap = file.read_heatmap(actual)
                    correct_heatmap += shrunk_greyscale_matrix
                    file.write_heatmap(correct_heatmap, str(actual) + " heatmap")

                # returns guessed character if correct
                if actual == guess:
                    row.append(guess)
                    correct = True

        final_text.append(row)

    return final_text


written_text = user_interface()
for i in written_text:
    print(i)


