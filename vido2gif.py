
from fileinput import filename
from math import pi
import sys
from UI_video2gif import Ui_MainWindow
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt, QPoint, QRect
from PyQt5.QtGui import QPixmap, QPainter, QPen
import cv2
import imageio
import os

class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent=parent)

        self.setupUi(self)
        self.init_properties()
        self.init_connections()


    def init_properties(self):
        #self.side_menu.setMaximumWidth(0)
        self.source_file_name= ""
        self.destination_file_name= ""
        
        self.drawing = False
       


    def init_connections(self):
        self.browse_source_btn.clicked.connect(self.browse_source_file)
        self.browse_destination_btn.clicked.connect(self.browse_destination_file)
        self.start_slider.sliderMoved.connect(self.start_slider_value_changed)
        self.stop_slider.sliderMoved.connect(self.stop_slider_value_changed)
        self.start_slider.sliderPressed.connect(self.start_slider_value_changed)
        self.stop_slider.sliderPressed.connect(self.stop_slider_value_changed)
        
        self.img_label.mousePressEvent = self.mouse_pressed
        self.img_label.mouseMoveEvent = self.mouse_moving
        self.img_label.mouseReleaseEvent = self.mouse_released   
        
        self.ctr_is_pressed = False 
        


    @QtCore.pyqtSlot(bool)
    
    def browse_source_file(self):
        self.source_file_name, file_selected= QtWidgets.QFileDialog.getOpenFileName(self, 'Open video file', filter= "Video Files(*.mp4  *.avi *.mkv)")
        if file_selected:
            self.source_txt.setText(self.source_file_name)
            pathname, extension = os.path.splitext(self.source_file_name)
            self.destination_file_name= pathname+ ".gif"
            self.destination_txt.setText(self.destination_file_name)
            self.load_video()
            
        
    def browse_destination_file(self):
        self.destination_file_name, flag = QtWidgets.QFileDialog.getSaveFileName(self,'Save File',directory=self.destination_file_name)
        pathname, extension = os.path.splitext(self.destination_file_name)
        if extension != '.gif':
            self.destination_file_name= self.destination_file_name+ ".gif"
        self.destination_txt.setText(self.destination_file_name)
        
    def start_slider_value_changed(self):
        if self.start_slider.hasFocus():
            actual_value = self.start_slider.sliderPosition()
            print('slide actual value', actual_value)
            self.frame = get_frame_from_video(self.cap, actual_value)
            pixmap = opencv_frame_to_pixmap(self.frame)
            self.img_label.setPixmap(pixmap)
            if (self.stop_slider.sliderPosition()- actual_value)<3:
                self.stop_slider.setSliderPosition(actual_value+3)
    
    def stop_slider_value_changed(self):
        if self.stop_slider.hasFocus():
            actual_value = self.stop_slider.sliderPosition()
            print('slide actual value', actual_value)
            self.frame = get_frame_from_video(self.cap, actual_value)
            pixmap = opencv_frame_to_pixmap(self.frame)
            self.img_label.setPixmap(pixmap)
            if (actual_value - self.start_slider.sliderPosition())<3:
                self.start_slider.setSliderPosition(actual_value-3)
        
    def load_video(self):
        self.cap = cv2.VideoCapture(self.source_file_name)
        
        # Display the first image
        ret, self.frame = self.cap.read()
        if ret:
            pixmap = opencv_frame_to_pixmap(self.frame)
            self.img_label.setPixmap(pixmap)
            
        
        # get the video properties and set theme to the GUI
        if self.cap.isOpened(): 
            
            self.video_intitial_width  = int(self.cap.get(cv2.CAP_PROP_FRAME_WIDTH))  # float `width`
            self.video_intitial_height = int(self.cap.get(cv2.CAP_PROP_FRAME_HEIGHT))  # float `height`
            self.video_intitial_fps = int(self.cap.get(cv2.CAP_PROP_FPS))# float `fps`
            self.video_intitial_total_frames = int(self.cap.get(cv2.CAP_PROP_FRAME_COUNT)) # float `total_frame_in_the_vi
            
            self.width_scale = int ( float(self.video_intitial_width)/float(self.img_label.pixmap().width()))
            self.height_scale = int ( float(self.video_intitial_height)/float(self.img_label.pixmap().height()))
            
            print('total frame = ', self.video_intitial_total_frames)
            self.fps_spin.setValue(self.video_intitial_fps)
            self.fps_spin.setMaximum(self.video_intitial_fps)
            self.width_txt.setText(str(self.video_intitial_width))
            self.height_txt.setText(str(self.video_intitial_height))
            self.start_slider.setMaximum(self.video_intitial_total_frames-3)
            self.stop_slider.setMaximum(self.video_intitial_total_frames-1)
            self.stop_slider.setMinimum(3)
            self.stop_slider.setValue(self.video_intitial_total_frames-1)
            
    # Region Of Interrest using mouse 
  
    #Mouse click event
    def mouse_pressed(self,event):
        if self.ctr_is_pressed:
            print('str is pressed')
        if event.button() == Qt.LeftButton:
        
            self.flag = True
            self.x0 = event.x()
            self.y0 = event.y()
            print('mouse preseed:', self.x0, self.y0)
        if event.button() == Qt.RightButton:
            self.x0_cv_image = 0
            self.y0_cv_image = 0
            self.x1_cv_image = self.video_intitial_width
            self.y1_cv_image = self.video_intitial_height
            self.flag = False
            f= self.frame.copy()
            #f = cv2.rectangle(f, (self.x0_cv_image,self.y0_cv_image), (self.x1_cv_image,self.y1_cv_image), color = (0, 0, 255), thickness=2)
            pixmap = opencv_frame_to_pixmap(f)
            self.img_label.setPixmap(pixmap)
            self.update()

            
    
    #Mouse release event
    def mouse_released(self,event):
        self.flag = False
        print('mouse released')
        

    
    #Mouse movement events
    def mouse_moving(self,event):
        if self.flag:
            self.x1 = event.x()
            self.y1 = event.y()
            # Scale x y to openCV image
            self.x0_cv_image = self.x0 * self.width_scale
            self.y0_cv_image = self.y0 * self.height_scale
            self.x1_cv_image = self.x1 * self.width_scale
            self.y1_cv_image = self.y1 * self.height_scale
            f= self.frame.copy()
            f = cv2.rectangle(f, (self.x0_cv_image,self.y0_cv_image), (self.x1_cv_image,self.y1_cv_image), color = (0, 0, 255), thickness=2)
            pixmap = opencv_frame_to_pixmap(f)
            self.img_label.setPixmap(pixmap)
            self.update()
            print("mouving: ", self.x1, self.y1 )
            print("mouving 2 : ", self.x1_cv_image, self.y1_cv_image )
            
    def keyPressEvent(self, event):

        if event.key() == 16777249: #if control key pressed
            #print('CTR key pressed')
            self.ctr_is_pressed = True
        #print('pressed from MainWindow: ', event.key())

    def keyReleaseEvent(self, event):
        if event.key() == 16777249:
            self.ctr_is_pressed = False
            print('ctr key released')



      


def opencv_frame_to_pixmap(frame):
    image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    qt_image = QtGui.QImage(image.data, image.shape[1], image.shape[0], QtGui.QImage.Format_RGB888)
    pic = qt_image.scaled(640, 480, QtCore.Qt.KeepAspectRatio)
   
    pixmap = QtGui.QPixmap.fromImage(pic)
    return pixmap
    
def get_frame_from_video(video_capture, image_number):
    ret=True
    video_capture.set(cv2.CAP_PROP_POS_FRAMES, image_number)
    ret, frame = video_capture.read()
    return frame

                

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    w = MainWindow()
    w.show()
    sys.exit(app.exec_())