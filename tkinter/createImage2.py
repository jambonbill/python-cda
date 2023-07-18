from PIL import Image

import random


width=256
height=256

im = Image.new('RGB', (width, height))
#im = Image.open('test.png') # Can be many different formats.
pixels = im.load()

#floatcolor=random.random()
color=random.randint(0,256)

#print("Color is "+str(color))
#exit(0)

for i in range(im.size[0]):    # for every col:
    for j in range(im.size[1]):    # For every row
        r=random.randint(0,256)
        r=random.randint(0,1)*256 #black or white
        pixels[i,j] = (r, r, r) # set the colour accordingly




print("save img")
im.save('png/randint.png')  # Save the modified pixels as .png

#im.show() #`GLIBCXX_3.4.29' not found

exit(0)
