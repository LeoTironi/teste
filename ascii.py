from PIL import ImageDraw,ImageFont,Image
import cv2
import numpy as np
import math

#Com algumas alterações pode funcionar com imagens

fileName="C:\\Users\\Usuario\\Desktop\\pendrive\\rodando.mp4"
chars = " .'`^,:;Il!i><~+_-?][}{1)(|\/tfjrxnuvczXYUJCLQ0OZmwqpdbkhao*#MW&8%B@$"
charlist=list(chars)
charlen=len(charlist)
interval=charlen/256
scale_factor=0.1
charwidth=10
charheight=10

def get_char(i):
    return charlist[math.floor(i*interval)]

cap = cv2.VideoCapture(fileName)

Font=ImageFont.truetype('C:\\Windows\\Fonts\\ARIAL.TTF',15)

while True:
    _, img = cap.read()

    img = Image.fromarray(img)

    width,height=img.size
    img=img.resize((int(scale_factor*width),int(scale_factor*height*(charwidth/charheight))),Image.NEAREST)
    width,height=img.size
    pixel=img.load()
    outputImage=Image.new("RGB",(charwidth*width,charheight*height),color=(0,0,0))
    dest=ImageDraw.Draw(outputImage)

    for i in range(height):
        for j in range(width):
            r,g,b=pixel[j,i]
            h=int((0.299*r+0.587*g+0.114*b))
            pixel[j,i]=(h,h,h)
            grayscale = math.floor((r+g+b)/3)
            dest.text((j*charwidth,i*charheight),get_char(h),font=Font,fill=(r,g,b))

    open_cv_image=np.array(outputImage)
    key=cv2.waitKey(1)
    if key == ord("q"):
        break
    cv2.imshow("AScii Art",open_cv_image)
cap.release()
cv2.destroyAllWindows()
