import cv2
from matplotlib import pyplot as plt

imageFile='./Chapter2/data/Lena.jpg'
imgGray=cv2.imread(imageFile,cv2.IMREAD_GRAYSCALE)
plt.axis('off')

plt.imshow(imgGray,cmap="gray",interpolation='bicubic')  #imgGray 영상을 'gray'컬러맵, 'bicubic'으로 보간
plt.show()