import file
import image_locator
import image_recognizer

file.display_rbg_image(file.get_image("big image"))

greyscale_matrix = file.rgb_to_grayscale(file.get_image("big image"))
matricies = image_locator.find_text(greyscale_matrix)
full_number_picture = []

for count_i in range(len(matricies)):
    row = []
    #print("count_i", count_i)
    for count_j in range(len(matricies[count_i])):
        number_identified = image_recognizer.image_recogniser(matricies[count_i][count_j])
        row.append(number_identified)
    full_number_picture.append(row)


for i in full_number_picture:
    print(i)
