from PIL import Image

image = Image.open("cave.jpg")      # Move from Resources folder to current folder
pixel1 = image.getpixel((0, 0))
(x, y) = image.size

final_image = Image.new('RGB', (x//2, y//2))

for width in range(x):
    for height in range(y):
        color = image.getpixel((width, height))
        if (width + height) % 2 == 0:
            final_image.putpixel((width // 2, height // 2), color)

final_image.save('final_image.jpg')     # Contained in the Resources folder
