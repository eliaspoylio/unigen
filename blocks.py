import numpy as np
import urllib.request
import math
from PIL import Image

def getTileAverage(image):
    """
    Return average grayscale value for image
    """
    nImage = np.array(image)
    w, h = nImage.shape
    return np.average(nImage.reshape(w*h))


def converToUnicode(url):
    blockScale = '█▓▙▀▚▌▝▏▒░.'
    cols = 48
    scale = 0.43
    
    #open image from url and convert to grayscale
    image = Image.open(urllib.request.urlopen(url)).convert('L')

    origWidth, origHeigth = image.size[0], image.size[1]
    # tile sizes
    tileWidth = origWidth/cols
    tileHeight = tileWidth/scale

    rows = int(origHeigth/tileHeight)

    unicodeImage = []
    
    for j in range(rows):
        y1 = int(j*tileHeight)
        y2 = int((j+1)*tileHeight)

        # correct last tile
        if j == rows-1:
            y2 = origHeigth

        unicodeImage.append("")

        for i in range(cols):
            x1 = int(i*tileWidth)
            x2 = int((i+1)*tileWidth)

            # correct last tile
            if i == cols-1:
                x2 = origWidth

            img = image.crop((x1, y1, x2, y2))

            avg = int(getTileAverage(img))

            tileValue = blockScale[int((avg*9)/255)]

            unicodeImage[j] += tileValue
    
    return unicodeImage