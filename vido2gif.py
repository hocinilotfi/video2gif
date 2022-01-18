
from fileinput import filename
from math import pi
import sys
from UI_video2gif import Ui_MainWindow
from PyQt5 import QtCore, QtGui, QtWidgets
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
       


    def init_connections(self):
        self.browse_source_btn.clicked.connect(self.browse_source_file)
        self.browse_destination_btn.clicked.connect(self.browse_destination_file)
        self.start_slider.sliderMoved.connect(self.start_slider_value_changed)
        self.stop_slider.sliderMoved.connect(self.stop_slider_value_changed)


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
            frame = get_frame_from_video(self.cap, actual_value)
            pixmap = opencv_frame_to_pixmap(frame)
            self.img_label.setPixmap(pixmap)
            if (self.stop_slider.sliderPosition()- actual_value)<3:
                self.stop_slider.setSliderPosition(actual_value+3)
    
    def stop_slider_value_changed(self):
        if self.stop_slider.hasFocus():
            actual_value = self.stop_slider.sliderPosition()
            print('slide actual value', actual_value)
            frame = get_frame_from_video(self.cap, actual_value)
            pixmap = opencv_frame_to_pixmap(frame)
            self.img_label.setPixmap(pixmap)
            if (actual_value - self.start_slider.sliderPosition())<3:
                self.start_slider.setSliderPosition(actual_value-3)
        
    def load_video(self):
        self.cap = cv2.VideoCapture(self.source_file_name)
        
        # Display the first image
        ret, frame = self.cap.read()
        if ret:
            pixmap = opencv_frame_to_pixmap(frame)
            self.img_label.setPixmap(pixmap)
        
        # get the video properties and set theme to the GUI
        if self.cap.isOpened(): 
            
            self.video_intitial_width  = int(self.cap.get(cv2.CAP_PROP_FRAME_WIDTH))  # float `width`
            self.video_intitial_height = int(self.cap.get(cv2.CAP_PROP_FRAME_HEIGHT))  # float `height`
            self.video_intitial_fps = int(self.cap.get(cv2.CAP_PROP_FPS))# float `fps`
            self.video_intitial_total_frames = int(self.cap.get(cv2.CAP_PROP_FRAME_COUNT)) # float `total_frame_in_the_vi
            print('total frame = ', self.video_intitial_total_frames)
            self.fps_spin.setValue(self.video_intitial_fps)
            self.fps_spin.setMaximum(self.video_intitial_fps)
            self.width_txt.setText(str(self.video_intitial_width))
            self.height_txt.setText(str(self.video_intitial_height))
            self.start_slider.setMaximum(self.video_intitial_total_frames-3)
            self.stop_slider.setMaximum(self.video_intitial_total_frames-1)
            self.stop_slider.setMinimum(3)
            self.stop_slider.setValue(self.video_intitial_total_frames-1)


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