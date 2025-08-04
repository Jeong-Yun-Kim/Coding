import cv2
from matplotlib import pyplot as plt

imageFile='./Chapter2/data/Lena.jpg'
imgGray=cv2.imread(imageFile,cv2.IMREAD_GRAYSCALE)

plt.figure(figsize=(6,6))  #크기 설정
plt.subplots_adjust(left=0,right=1,bottom=0,top=1)  #영상 출력 범위 좌우 [0,1], 위아래 [0,1]로 조정
plt.imshow(imgGray,cmap='gray')
##plt.axis('tight')
plt.axis('off')
plt.savefig('./Chapter2/resultData/LenaBrankAdjust.png')
plt.show()