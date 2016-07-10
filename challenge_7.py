from PIL import Image
import re

image = Image.open('oxygen.png')    # Move from Resources folder to current folder

y = 48
last_x = 607
message = ''

for x in range(0, last_x, 7):
    message += chr((image.getpixel((x, 48))[0]))

print(message)

pattern1 = r"[0-9]+"
final_code = ''
string_final = ''

final_code = re.findall(pattern1, message)

for number in final_code:
    string_final += chr(int(number))

print(string_final)
