from PIL import Image

img = Image.open("beach.jpg")
img.show() #original image

pixmap = img.load()

def filter_chooser():
    choice = input("enter the exact name of the image with quotes--")
    img = Image.open(choice)
    choice2 = input("what filter do you want? /n1.rusted /n2.bright_blue /n3.old timey /n4.purple")
    if choice2 == 1:
        for i in range(img.size[0]):  
            for j in range(img.size[1]):
                r, g, b = pixmap[i,j]
                r += 0
                g -= 100
                b -= 100
                pixmap[i,j] = (r, g, b)
        img.show()
    if choice2 == 2:
        for i in range(img.size[0]):
            for j in range(img.size[1]):
                r, g, b = pixmap[i,j]
                r += 0
                g += 55
                b += 255
                pixmap[i,j] = (r, g, b)
        img.show()
#    if choice2 == 3:
#        for i in range(img.size[0]):
#            for j in range(img.size[1]):
#                r, g, b = pixmap[i,j]
#                r += 0
#                g += 55
#                b += 255
#                pixmap[i,j] = (r, g, b)
        img.show()
    if choice2 == 3:
        for i in range(img.size[0]):  
            for j in range(img.size[1]):
                r, g, b = pixmap[i,j]
                r = b
                g = r
                b = g
                pixmap[i,j] = (r, g, b)
        img.show()
    if choice2 == 4:
        for i in range(img.size[0]):  
            for j in range(img.size[1]):
                r, g, b = pixmap[i,j]
                r = (r + g + b) // 4
                g = (r + g + b) // 9
                b = (r + g + b) // 2
                pixmap[i,j] = (r, g, b)
        img.show()
def negative():
    img = Image.open("beach.jpg")
    pixmap = img.load()
    for i in range(img.size[0]):  
        for j in range(img.size[1]):
            r, g, b = pixmap[i,j]
            r = 255 - r 
            g = 255 - g
            b = 255 - b
            pixmap[i,j] = (r, g, b)
            img.save("negative_filter.jpg")
 
    img.show()


#    filter_chooser()



    