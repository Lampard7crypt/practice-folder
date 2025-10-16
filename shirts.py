from PIL import Image, ImageOps
import sys

input_file = sys.argv[1]
output_file = sys.argv[2]

with Image.open(input_file) as input_img, Image.open("shirt_blue.jpg") as shirt:
    resized_input = ImageOps.fit(input_img, shirt.size)
    shirt.paste(resized_input, (0, 0), resized_input)
    resized_input.save(output_file)
