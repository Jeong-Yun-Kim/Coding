import cv2
import numpy as np

#White 배경 생성
img=np.zeros(shape=(512,512,3), dtype=np.uint8)+255

'''
np.zeros() : 영상으로 사용할 0으로 초기화된 배열 생성
shape=(512,512,3) : 512X512 크기의 3채널 컬러영상
dtype=np.uint8 : 영상 화소가 부호 없는 8비트 정수
np.zeros()+255 : 영상 모든 채널 값이 255로 변경->흰색 배경
'''

#img=np.ones((512,512,3),np.uint8)*255  #np.ones() : 1로 초기화된 배열 생성
#img=np.full((512,512,3),(255,255,255),dtype=np.uint8)  #np.full() : 배경으로 사용할 컬러 지정해서 영상 생성 가능
#img=np.zeros(shape=(512,512,3), dtype=np.uint8)  #Black 배경
pt1=100,100
pt2=400,400
cv2.rectangle(img,pt1,pt2,(0,255,0),2)  #img 영상에 pt1, pt2에 의해 정의되는 사각형을 녹색, 두께 2로 그림

cv2.line(img,(0,0),(500,0),(255,0,0),5)  #img 영상에 원점에서 좌표(500,0)로 파란색, 두께 5로 그림
cv2.line(img,(0,0),(0,500),(0,0,255),5)  #img 영상에 원점에서 좌표(0,500)로 빨간색, 두께 5로 그림

cv2.imshow('img',img)
cv2.waitKey()
cv2.destroyAllWindows()