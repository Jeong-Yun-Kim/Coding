import cv2
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# 프로그램 시작    
cap = cv2.VideoCapture(0)
fig = plt.figure(figsize=(10, 6)) # fig.set_size_inches(10, 6)
fig.canvas.manager.set_window_title('Video Capture')
plt.axis('off')

#애니메이션 초기화 함수 정의
def init():   
    global im
    retval, frame = cap.read() # 첫 프레임 캡처
    im = plt.imshow(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
##    return im, #updateFrame()에서 영상 갱신하기 때문에 필요없음

#애니메이션 반복적으로 호출될 함수 정의
def updateFrame(k):   #k : 애니메이션 프레임 번호 전달됨
    retval, frame = cap.read()
    if retval:
        im.set_array(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))

ani = animation.FuncAnimation(fig, updateFrame, init_func=init, interval=50)
plt.show()
if cap.isOpened():
    cap.release() 