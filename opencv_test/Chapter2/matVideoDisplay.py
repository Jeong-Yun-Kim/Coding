import cv2 
import matplotlib.pyplot as plt

#종료
def handle_key_press(event):
    if event.key == 'escape':
        cap.release()
        plt.close()       
def handle_close(evt):
    print('Close figure!')
    cap.release()

#프로그램 시작    
cap = cv2.VideoCapture(0) # 0번 카메라

plt.ion() # 대화모드 설정
fig = plt.figure(figsize=(10, 6))  #크기 10X6인치로 설정
plt.axis('off')  #좌표축 제거
#ax = fig.gca()
#ax.set_axis_off()
fig.canvas.manager.set_window_title('Video Capture')  #윈도우 타이틀
fig.canvas.mpl_connect('key_press_event', handle_key_press)
fig.canvas.mpl_connect('close_event', handle_close)

retval, frame = cap.read() 
im = plt.imshow(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))

while True:
    retval, frame = cap.read()  #비디오 프레임 캡처
    if not retval:  #비디오 캡처 실패시 나가기
        break       
#    plt.imshow(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
    im.set_array(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
    fig.canvas.draw()  #캔버스 갱신
#   fig.canvas.draw_idle()
    fig.canvas.flush_events()  # plt.pause(0.001)
if cap.isOpened():
    cap.release() 