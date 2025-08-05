import cv2

cap = cv2.VideoCapture(0) # 0번 카메라
frame_size = (int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)),
              int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)))
print('frame_size =', frame_size)

#비디오 출력 위한 코덱 생성
#fourcc = cv2.VideoWriter_fourcc(*'DIVX')  # ('D', 'I', 'V', 'X')
fourcc = cv2.VideoWriter_fourcc(*'XVID')

out1 = cv2.VideoWriter('./Chapter2/resultData/record0.mp4',fourcc, 20.0, frame_size)                #컬러 비디오 생성
out2 = cv2.VideoWriter('./Chapter2/resultData/record1.mp4',fourcc, 20.0, frame_size,isColor=False)  #그레이스케일 비디오 생성

while True:
    retval, frame = cap.read()  #비디오 프레임 캡처
    if not retval:
        break   
    out1.write(frame)  #out1객체에 frame출력
    
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)  #그레이스케일 영상으로 변환
    out2.write(gray)        
    cv2.imshow('frame',frame)
    cv2.imshow('gray',gray)      
    
    key = cv2.waitKey(25)  #25/1000초 대기
    if key == 27:          #ESC
        break
#비디오 객체 해제 및 모든 윈도우 파괴
cap.release()
out1.release()
out2.release()
cv2.destroyAllWindows()