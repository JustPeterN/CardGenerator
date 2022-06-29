# Importing the PIL library
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont


def read_file():
    file_obj = open("words.txt", "r")  # opens the file in read mode
    words = file_obj.read().splitlines()  # puts the file into an array
    file_obj.close()
    return words

words = read_file()
myFont = ImageFont.truetype('arial.ttf', 29)

for index, i in enumerate(words):
    img = Image.open('card.PNG')
    I = ImageDraw.Draw(img)
    I.text((80, 80), words[0], font=myFont, fill=(255, 255, 255))
    I.text((80, 180), words[1], font=myFont, fill=(255, 255, 255))
    I.text((80, 280), words[2], font=myFont, fill=(255, 255, 255))
    I.text((80, 380), words[3], font=myFont, fill=(255, 255, 255))
    I.text((80, 480), words[4], font=myFont, fill=(255, 255, 255))
    print(words)
    #img.show()
    words = words[5:]
    img.save("cards/card " + str(index) + ".png")
