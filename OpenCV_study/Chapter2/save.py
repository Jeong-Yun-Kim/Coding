import cv2

imageFile='./Chapter2/data/Lena.jpg'
img=cv2.imread(imageFile)
cv2.imwrite('./Chapter2/resultData/Lena.bmp', img)
cv2.imwrite('./Chapter2/resultData/Lena.png', img)
cv2.imwrite('./Chapter2/resultData/Lena2.png', img, [cv2.IMWRITE_PNG_COMPRESSION, 9]) #압축률 9의 PNG 영상으로 저장. 압축률 범위는 [0,9]로, 높을수록 시간 오래 걸림. 디폴트는 3.
cv2.imwrite('./Chapter2/resultData/Lena2.jpg', img, [cv2.IMWRITE_JPEG_QUALITY, 90])   #90%의 품질을 갖는 JPEG영상으로 저장. 품질 범위는 [0,100]으로, 높을수록 영상 품질 좋음. 디폴트는 95.