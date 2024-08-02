import numpy as np
import file

print("WELCOME TO THE IMAGE RECOGNIZER")

def train_ai(target):
    # reorders to begin training
    trainable_characters = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
    trainable_characters.remove(target)
    trainable_characters.insert(0, target)

    # resets heatmap
    file.reset_heatmap(32, str(target) + " heatmap")

    # training
    blank_heatmap = file.read_heatmap(str(target)).astype(np.float64)

    # initial training with no calculation
    for number in trainable_characters:
        for version in range(1, 21):
            image = file.get_image(f'{number}.{version}')
            grayscale_image = file.rgb_to_grayscale(image).astype(np.float64)
            if number == target:
                blank_heatmap += (len(trainable_characters) - 1) * grayscale_image
            else:
                blank_heatmap -= grayscale_image
    file.write_heatmap(blank_heatmap, str(target) + " heatmap")

    cont = True
    while cont:

        guess_and_correct = []
        guess_and_wrong = []
        not_and_correct = []
        not_and_wrong = []

        for number in trainable_characters:

            for version in range(1, 21):

                image = file.get_image(f'{number}.{version}')
                grayscale_image = file.rgb_to_grayscale(image).astype(np.float64)

                heatmap = file.read_heatmap(str(target)).astype(np.float64)

                # multiplies matrices to obtain a certainty value
                total = 0
                for i in range(32):
                    for j in range(32):
                        total += grayscale_image[i, j] * heatmap[i, j]

                # if guesses wrong character, character is removed from heatmap
                if total > 0 and number != target:
                    guess_and_wrong.append(f"{number}.{version}")
                    heatmap -= grayscale_image * np.ones((32, 32))
                    file.write_heatmap(heatmap, str(target) + " heatmap")

                # if guesses target, but the image is not the target, image is added to the heatmap
                elif total < 0 and number == target:
                    not_and_wrong.append(f"{number}.{version}")
                    heatmap += grayscale_image * np.ones((32, 32))
                    file.write_heatmap(heatmap, str(target) + " heatmap")

                # if the guess is correct, nothing changes

        if len(guess_and_correct) == 0 and len(guess_and_wrong) == 0 and len(not_and_correct) == 0 and len(
                not_and_wrong) == 0:
            cont = False


