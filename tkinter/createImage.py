from PIL import Image

width=320
height=200

im = Image.new('RGB', (width, height))
#im = Image.open('test.png') # Can be many different formats.
pixels = im.load()

for i in range(im.size[0]):    # for every col:
    for j in range(im.size[1]):    # For every row
        pixels[i,j] = (i, j, 100) # set the colour accordingly


print("save img")
im.save('png/test.png')  # Save the modified pixels as .png


#im.show() #`GLIBCXX_3.4.29' not found


exit(0)
