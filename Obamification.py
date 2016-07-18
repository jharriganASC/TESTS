from Myro import *

ObamaDarkBlue = makeColor(0, 51, 76)
ObamaRed = makeColor(217, 26, 33)
ObamaBlue = makeColor(112, 150, 158)
ObamaYellow = makeColor(252, 227, 166)

pic = makePicture(pickAFile())

pixels = getPixels(pic)

for pixels in pixels:
    
    gray = getGray(pixels)
    
    if gray > 180:
        setColor(pixels, ObamaYellow)
        
        show(pic)