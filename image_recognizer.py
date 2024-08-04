import numpy as np
import file

def shrink_image(image, a):

    #file.display_grayscale_image(image)
    n, m = image.shape

    # Calculate the step size for downsampling
    row_step = n / a
    col_step = m / a

    # Generate the indices to keep
    row_indices = [int(i * row_step) for i in range(a)]
    col_indices = [int(j * col_step) for j in range(a)]

    # Use the indices to downsample the image
    shrunk_image = image[np.ix_(row_indices, col_indices)]

    return shrunk_image

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

def image_recogniser(image):
    testable_characters = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

    # shrinks the matrix to match the 32x32 format
    greyscale_matrix = shrink_image(image, 32)

    # generates the certainties for each character
    scores = []
    for number in testable_characters:
        heatmap = file.read_heatmap(number)
        total = 0
        for i in range(32):
            for j in range(32):
                total += greyscale_matrix[i, j] * heatmap[i, j]
        scores.append(total)

    # for count in range(10):
    #     print(f"{testable_numbers[count]}: ", scores[count])

    #file.display_grayscale_image(greyscale_matrix)
    return testable_characters[np.argmax(scores)]



