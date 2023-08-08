# Author : InferiorAK

import os
from PIL import Image

# Perform background removal for each image (assuming white background)
def remove_background(image):
    image = image.convert("RGBA")
    data = image.getdata()
    
    new_data = []
    for item in data:
        # Change all white (also shades of whites)
        # pixels to transparent
        if item[:3] == (255, 255, 255):
            new_data.append((255, 255, 255, 0))
        else:
            new_data.append(item)
    
    image.putdata(new_data)
    return image

# Open the images you want to merge
dir = os.listdir("extracted_qr")
img_list = []
for img in dir:
    img_list.append(f'remove_background(Image.open("extracted_qr/{img}"))')

merged_image = Image.new('RGBA', eval(img_list[0]).size, (255, 255, 255, 255))

# Paste images onto the blank image
for img in img_list:
    merged_image.paste(eval(img), (0,0), eval(img))

# Save or display the merged image
merged_image.save('merged_qr image.png')
merged_image.show()