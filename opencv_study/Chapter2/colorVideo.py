import cv2
from matplotlib import pyplot as plt

imageFile='./Chapter2/data/Lena.jpg'
imgBGR=cv2.imread(imageFile)
plt.axis('off')  #X,Y축 표시X
#plt.imshow(imgBGR)  
#plt.show()

imgRGB=cv2.cvtColor(imgBGR,cv2.COLOR_BGR2RGB)  #imgBGR의 채널 순서 BGR을 RGB 채널 순서로 변경.
plt.imshow(imgRGB)                         #컬러영상 처리 채널 순서 : OpenCV->BGR, Matplotlib->RGB
plt.show()