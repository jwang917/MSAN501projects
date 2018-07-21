import sys
import time
from PIL import Image

# define your flip function here
...
if len(sys.argv)<=1:
	print ("missing image filename")
	sys.exit(1)
filename = sys.argv[1]
img = Image.open(filename)
img = img.convert("L")

def blur(img):
    width, height = img.size
    # copy the original picture
    imgdup = img.copy()
    # get the matrix representation of original image.
    pixels = imgdup.load()
    for x in range(width):
        for y in range(height):
            # store the output of function region3 into r.
            r = region3(imgdup,x,y)
           
            # set the pixels[x,y] to be the averaged result of avg(r)
            pixels[x,y] = avg(r)
    return imgdup

def avg(data):
    # data is the return of region3, and it is a list.
    return int(sum(data)/len(data))

def region3(img,x,y):
    me = getpixel(img,x,y)
    N = getpixel(img,x,y-1)
    E = getpixel(img,x+1,y)
    S = getpixel(img,x,y+1)
    W = getpixel(img,x-1,y)
    NW = getpixel(img,x-1,y-1)
    NE = getpixel(img,x+1,y-1)
    SE = getpixel(img,x+1,y+1)
    SW = getpixel(img,x-1,y+1)
    #use a list to store all the 9 pixels around (x,y)
    pxls = [me,N,E,S,W,NW,NE,SE,SW]
    
    return pxls

def getpixel(img,x,y):
    #get the boundary of img, store it into width and height.
    width, height = img.size
    if x < 0: 
        x = 0
    elif x >= width:
        x = width-1
    if y < 0: 
        y = 0
    elif y >= height:
        y = height-1
    m = img.load()
    return m[x,y]
    
#Time the blur processing.
st = time.time()    
blurred = blur(img)
blurred.show()
img.show()
end = time.time()
lapse = end - st
print(lapse)