import cv2

imageFile='./Chapter2/data/Lena.jpg'
img=cv2.imread(imageFile)     #cv2.IMREAD_COLOR
img2=cv2.imread(imageFile,0)  #cv2.IMREAD_GRAYSCALE
cv2.imshow('Lena color',img)
cv2.imshow('Lena grayscale',img2)

cv2.waitKey()
cv2.destroyAllWindows()   #임의의 키 터치시 윈도우 파괴