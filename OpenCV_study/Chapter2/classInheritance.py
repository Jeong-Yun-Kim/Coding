import cv2
import matplotlib.pyplot as plt
import matplotlib.animation as animation
 
class Video(animation.FuncAnimation):
    def __init__(self, device=0, fig=None, frames=None,
                       interval=50, repeat_delay=5, blit=False, **kwargs):  #상위클래스 생성자 호출 및 함수 초기화

        if fig is None:
            self.fig = plt.figure()
            self.fig.canvas.manager.set_window_title('Video Capture')
            plt.axis("off")
            
        super(Video, self).__init__(self.fig, self.updateFrame, init_func=self.init,
                                    frames=frames, interval=interval, blit=blit,
                                    repeat_delay=repeat_delay, **kwargs)        
        self.cap = cv2.VideoCapture(device)
        print("start capture ...")
        
    #프레임 캡처 및 RGB로 변환하여 표시, 반환값 저장
    def init(self): 
        retval, self.frame = self.cap.read()
        if retval:
            self.im = plt.imshow(cv2.cvtColor(self.frame, cv2.COLOR_BGR2RGB))
                    
    #비디오 프레임 캡처 및 RGB로 변환, 영상 변경
    def updateFrame(self, k):
        retval, self.frame = self.cap.read()
        if retval:
            self.im.set_array(cv2.cvtColor(camera.frame, cv2.COLOR_BGR2RGB))
#       return self.im,

    #비디오 객체가 개방되어 있으면 해제
    def close(self):
        if self.cap.isOpened():
            self.cap.release()
        print("finish capture.")

# 프로그램 시작 
camera = Video()
##camera = Video('./data/vtest.avi')
plt.show()
camera.close()