# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/lotfi/Documents/vs-code-projects/video2gif/video2gif.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1031, 590)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("#middle_frame{\n"
"background-color: rgb(66, 86, 120);\n"
"}\n"
"\n"
"#top_bar{\n"
"    background-color: rgb(26, 26, 80);\n"
"}\n"
"#left_side_frame{\n"
"background-color: rgb(46, 66, 100);\n"
"}\n"
"#right_side_frame_2{\n"
"background-color: rgb(46, 66, 100);\n"
"}\n"
"#buttom_bar{\n"
"    background-color: rgb(26, 26, 80);\n"
"}\n"
"*{\n"
"background-color: transparent;\n"
"color: #fff;\n"
"}\n"
"QFrame{\n"
" border: none;\n"
"}\n"
"\n"
"\n"
"QPushButton{\n"
"border-radius: 5px;\n"
"background-color: #040f13;\n"
"color: white;\n"
"padding: 5px;\n"
"\n"
"}\n"
"QPushButton:hover{\n"
"padding: 5px;\n"
"background-color: rgb(59, 103, 128);\n"
"border-left: 1px solid red;\n"
"\n"
"}\n"
"QProgressBar{\n"
"border-radius: 5px;\n"
"}\n"
"QTextEdit{\n"
"background-color: rgb(255,255,255);\n"
"border: 1px solid blue;\n"
"color: black;\n"
"}\n"
"\n"
"QCheckBox{\n"
"color: white;\n"
"}\n"
"QCheckBox::indicator:checked{\n"
"background-color: red;\n"
"}\n"
"QCheckBox::indicator:unchecked{\n"
"background-color: white;\n"
"}\n"
"QSpinBox{\n"
"\n"
"}")
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.top_bar = QtWidgets.QFrame(self.centralwidget)
        self.top_bar.setMinimumSize(QtCore.QSize(0, 70))
        self.top_bar.setMaximumSize(QtCore.QSize(16777215, 70))
        self.top_bar.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.top_bar.setFrameShadow(QtWidgets.QFrame.Raised)
        self.top_bar.setObjectName("top_bar")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout(self.top_bar)
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_8.setSpacing(6)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.frame_14 = QtWidgets.QFrame(self.top_bar)
        self.frame_14.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_14.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_14.setObjectName("frame_14")
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout(self.frame_14)
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.label = QtWidgets.QLabel(self.frame_14)
        font = QtGui.QFont()
        font.setPointSize(28)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.horizontalLayout_9.addWidget(self.label)
        self.horizontalLayout_8.addWidget(self.frame_14, 0, QtCore.Qt.AlignHCenter)
        self.verticalLayout.addWidget(self.top_bar)
        self.middle_frame = QtWidgets.QFrame(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.middle_frame.sizePolicy().hasHeightForWidth())
        self.middle_frame.setSizePolicy(sizePolicy)
        self.middle_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.middle_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.middle_frame.setObjectName("middle_frame")
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout(self.middle_frame)
        self.horizontalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.left_side_frame = QtWidgets.QFrame(self.middle_frame)
        self.left_side_frame.setMinimumSize(QtCore.QSize(400, 0))
        self.left_side_frame.setMaximumSize(QtCore.QSize(400, 16777215))
        self.left_side_frame.setStyleSheet("")
        self.left_side_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.left_side_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.left_side_frame.setObjectName("left_side_frame")
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout(self.left_side_frame)
        self.horizontalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_11.setSpacing(6)
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.frame_15 = QtWidgets.QFrame(self.left_side_frame)
        self.frame_15.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_15.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_15.setObjectName("frame_15")
        self.verticalLayout_14 = QtWidgets.QVBoxLayout(self.frame_15)
        self.verticalLayout_14.setObjectName("verticalLayout_14")
        self.groupBox_3 = QtWidgets.QGroupBox(self.frame_15)
        self.groupBox_3.setMaximumSize(QtCore.QSize(16777215, 70))
        self.groupBox_3.setObjectName("groupBox_3")
        self.horizontalLayout_17 = QtWidgets.QHBoxLayout(self.groupBox_3)
        self.horizontalLayout_17.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_17.setObjectName("horizontalLayout_17")
        self.frame_30 = QtWidgets.QFrame(self.groupBox_3)
        self.frame_30.setStyleSheet("\n"
"QFrame{\n"
"    border:none;\n"
"}\n"
"#buttom_bar{\n"
"border: 1px solid gray;\n"
"}\n"
"QPushButton{\n"
"padding: 5px;\n"
"border-radius: 5px;\n"
"background-color: rgb(192, 191, 188)\n"
"}\n"
"QPushButton:hover{\n"
"padding: 5px;\n"
"border-radius: 5px;\n"
"background-color: rgb(154, 153, 150);\n"
"}")
        self.frame_30.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_30.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_30.setObjectName("frame_30")
        self.horizontalLayout_20 = QtWidgets.QHBoxLayout(self.frame_30)
        self.horizontalLayout_20.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_20.setObjectName("horizontalLayout_20")
        self.frame_27 = QtWidgets.QFrame(self.frame_30)
        self.frame_27.setMinimumSize(QtCore.QSize(0, 45))
        self.frame_27.setMaximumSize(QtCore.QSize(16777215, 45))
        self.frame_27.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_27.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_27.setObjectName("frame_27")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.frame_27)
        self.verticalLayout_7.setContentsMargins(9, 0, 0, 0)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.label_4 = QtWidgets.QLabel(self.frame_27)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_7.addWidget(self.label_4)
        self.horizontalLayout_20.addWidget(self.frame_27)
        self.frame_28 = QtWidgets.QFrame(self.frame_30)
        self.frame_28.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_28.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_28.setObjectName("frame_28")
        self.horizontalLayout_18 = QtWidgets.QHBoxLayout(self.frame_28)
        self.horizontalLayout_18.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_18.setObjectName("horizontalLayout_18")
        self.fps_spin = QtWidgets.QSpinBox(self.frame_28)
        self.fps_spin.setMinimumSize(QtCore.QSize(60, 0))
        self.fps_spin.setMaximumSize(QtCore.QSize(60, 30))
        self.fps_spin.setAutoFillBackground(False)
        self.fps_spin.setObjectName("fps_spin")
        self.horizontalLayout_18.addWidget(self.fps_spin)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_18.addItem(spacerItem)
        self.horizontalLayout_20.addWidget(self.frame_28)
        self.horizontalLayout_17.addWidget(self.frame_30)
        self.verticalLayout_14.addWidget(self.groupBox_3)
        self.groupBox_2 = QtWidgets.QGroupBox(self.frame_15)
        self.groupBox_2.setObjectName("groupBox_2")
        self.verticalLayout_13 = QtWidgets.QVBoxLayout(self.groupBox_2)
        self.verticalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_13.setObjectName("verticalLayout_13")
        self.frame_18 = QtWidgets.QFrame(self.groupBox_2)
        self.frame_18.setStyleSheet("")
        self.frame_18.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_18.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_18.setObjectName("frame_18")
        self.verticalLayout_11 = QtWidgets.QVBoxLayout(self.frame_18)
        self.verticalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.frame_19 = QtWidgets.QFrame(self.frame_18)
        self.frame_19.setMaximumSize(QtCore.QSize(16777215, 50))
        self.frame_19.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_19.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_19.setObjectName("frame_19")
        self.verticalLayout_12 = QtWidgets.QVBoxLayout(self.frame_19)
        self.verticalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_12.setObjectName("verticalLayout_12")
        self.frame_26 = QtWidgets.QFrame(self.frame_19)
        self.frame_26.setMaximumSize(QtCore.QSize(16777215, 50))
        self.frame_26.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_26.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_26.setObjectName("frame_26")
        self.verticalLayout_15 = QtWidgets.QVBoxLayout(self.frame_26)
        self.verticalLayout_15.setContentsMargins(9, 0, 0, 0)
        self.verticalLayout_15.setObjectName("verticalLayout_15")
        self.keep_ratio_btn = QtWidgets.QCheckBox(self.frame_26)
        self.keep_ratio_btn.setChecked(False)
        self.keep_ratio_btn.setObjectName("keep_ratio_btn")
        self.verticalLayout_15.addWidget(self.keep_ratio_btn)
        self.verticalLayout_12.addWidget(self.frame_26)
        self.verticalLayout_11.addWidget(self.frame_19)
        self.frame_20 = QtWidgets.QFrame(self.frame_18)
        self.frame_20.setMaximumSize(QtCore.QSize(16777215, 45))
        self.frame_20.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_20.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_20.setObjectName("frame_20")
        self.horizontalLayout_14 = QtWidgets.QHBoxLayout(self.frame_20)
        self.horizontalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_14.setObjectName("horizontalLayout_14")
        self.frame_22 = QtWidgets.QFrame(self.frame_20)
        self.frame_22.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_22.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_22.setObjectName("frame_22")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.frame_22)
        self.verticalLayout_9.setContentsMargins(12, -1, 0, -1)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.label_2 = QtWidgets.QLabel(self.frame_22)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_9.addWidget(self.label_2)
        self.horizontalLayout_14.addWidget(self.frame_22)
        self.frame_23 = QtWidgets.QFrame(self.frame_20)
        self.frame_23.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_23.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_23.setObjectName("frame_23")
        self.horizontalLayout_15 = QtWidgets.QHBoxLayout(self.frame_23)
        self.horizontalLayout_15.setContentsMargins(0, -1, 0, -1)
        self.horizontalLayout_15.setObjectName("horizontalLayout_15")
        self.width_txt = QtWidgets.QTextEdit(self.frame_23)
        self.width_txt.setMaximumSize(QtCore.QSize(60, 30))
        self.width_txt.setObjectName("width_txt")
        self.horizontalLayout_15.addWidget(self.width_txt)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_15.addItem(spacerItem1)
        self.horizontalLayout_14.addWidget(self.frame_23)
        self.verticalLayout_11.addWidget(self.frame_20)
        self.frame_21 = QtWidgets.QFrame(self.frame_18)
        self.frame_21.setMaximumSize(QtCore.QSize(16777215, 45))
        self.frame_21.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_21.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_21.setObjectName("frame_21")
        self.horizontalLayout_13 = QtWidgets.QHBoxLayout(self.frame_21)
        self.horizontalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_13.setObjectName("horizontalLayout_13")
        self.frame_24 = QtWidgets.QFrame(self.frame_21)
        self.frame_24.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_24.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_24.setObjectName("frame_24")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.frame_24)
        self.verticalLayout_8.setContentsMargins(-1, -1, 0, -1)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.label_3 = QtWidgets.QLabel(self.frame_24)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_8.addWidget(self.label_3)
        self.horizontalLayout_13.addWidget(self.frame_24)
        self.frame_25 = QtWidgets.QFrame(self.frame_21)
        self.frame_25.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_25.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_25.setObjectName("frame_25")
        self.horizontalLayout_16 = QtWidgets.QHBoxLayout(self.frame_25)
        self.horizontalLayout_16.setContentsMargins(0, -1, 0, -1)
        self.horizontalLayout_16.setObjectName("horizontalLayout_16")
        self.height_txt = QtWidgets.QTextEdit(self.frame_25)
        self.height_txt.setMaximumSize(QtCore.QSize(60, 30))
        self.height_txt.setObjectName("height_txt")
        self.horizontalLayout_16.addWidget(self.height_txt)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_16.addItem(spacerItem2)
        self.horizontalLayout_13.addWidget(self.frame_25)
        self.verticalLayout_11.addWidget(self.frame_21)
        self.verticalLayout_13.addWidget(self.frame_18)
        self.verticalLayout_14.addWidget(self.groupBox_2)
        self.groupBox = QtWidgets.QGroupBox(self.frame_15)
        self.groupBox.setObjectName("groupBox")
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout(self.groupBox)
        self.horizontalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.frame_29 = QtWidgets.QFrame(self.groupBox)
        self.frame_29.setStyleSheet("")
        self.frame_29.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_29.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_29.setObjectName("frame_29")
        self.horizontalLayout_19 = QtWidgets.QHBoxLayout(self.frame_29)
        self.horizontalLayout_19.setObjectName("horizontalLayout_19")
        self.frame_16 = QtWidgets.QFrame(self.frame_29)
        self.frame_16.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_16.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_16.setObjectName("frame_16")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.frame_16)
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.start_slider = QtWidgets.QSlider(self.frame_16)
        self.start_slider.setPageStep(1)
        self.start_slider.setOrientation(QtCore.Qt.Horizontal)
        self.start_slider.setObjectName("start_slider")
        self.verticalLayout_5.addWidget(self.start_slider)
        self.stop_slider = QtWidgets.QSlider(self.frame_16)
        self.stop_slider.setPageStep(1)
        self.stop_slider.setOrientation(QtCore.Qt.Horizontal)
        self.stop_slider.setInvertedAppearance(False)
        self.stop_slider.setInvertedControls(False)
        self.stop_slider.setObjectName("stop_slider")
        self.verticalLayout_5.addWidget(self.stop_slider)
        self.horizontalLayout_19.addWidget(self.frame_16)
        self.frame_17 = QtWidgets.QFrame(self.frame_29)
        self.frame_17.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_17.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_17.setObjectName("frame_17")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.frame_17)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.play_btn = QtWidgets.QPushButton(self.frame_17)
        self.play_btn.setObjectName("play_btn")
        self.verticalLayout_6.addWidget(self.play_btn)
        self.horizontalLayout_19.addWidget(self.frame_17)
        self.horizontalLayout_12.addWidget(self.frame_29)
        self.verticalLayout_14.addWidget(self.groupBox)
        self.horizontalLayout_11.addWidget(self.frame_15, 0, QtCore.Qt.AlignTop)
        self.horizontalLayout_10.addWidget(self.left_side_frame)
        self.right_side_frame_1 = QtWidgets.QFrame(self.middle_frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.right_side_frame_1.sizePolicy().hasHeightForWidth())
        self.right_side_frame_1.setSizePolicy(sizePolicy)
        self.right_side_frame_1.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.right_side_frame_1.setFrameShadow(QtWidgets.QFrame.Raised)
        self.right_side_frame_1.setObjectName("right_side_frame_1")
        self.horizontalLayout_22 = QtWidgets.QHBoxLayout(self.right_side_frame_1)
        self.horizontalLayout_22.setObjectName("horizontalLayout_22")
        self.frame = QtWidgets.QFrame(self.right_side_frame_1)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayout_21 = QtWidgets.QHBoxLayout(self.frame)
        self.horizontalLayout_21.setObjectName("horizontalLayout_21")
        self.img_label = QtWidgets.QLabel(self.frame)
        self.img_label.setText("")
        self.img_label.setObjectName("img_label")
        self.horizontalLayout_21.addWidget(self.img_label, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.horizontalLayout_22.addWidget(self.frame)
        self.horizontalLayout_10.addWidget(self.right_side_frame_1)
        self.right_side_frame_2 = QtWidgets.QFrame(self.middle_frame)
        self.right_side_frame_2.setMinimumSize(QtCore.QSize(40, 0))
        self.right_side_frame_2.setMaximumSize(QtCore.QSize(35, 16777215))
        self.right_side_frame_2.setStyleSheet("#frame_13{\n"
"border: 1px solid gray;\n"
"}")
        self.right_side_frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.right_side_frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.right_side_frame_2.setObjectName("right_side_frame_2")
        self.verticalLayout_10 = QtWidgets.QVBoxLayout(self.right_side_frame_2)
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.progressBar = QtWidgets.QProgressBar(self.right_side_frame_2)
        self.progressBar.setEnabled(True)
        self.progressBar.setProperty("value", 20)
        self.progressBar.setAlignment(QtCore.Qt.AlignCenter)
        self.progressBar.setTextVisible(True)
        self.progressBar.setOrientation(QtCore.Qt.Vertical)
        self.progressBar.setTextDirection(QtWidgets.QProgressBar.TopToBottom)
        self.progressBar.setObjectName("progressBar")
        self.verticalLayout_10.addWidget(self.progressBar)
        self.horizontalLayout_10.addWidget(self.right_side_frame_2)
        self.verticalLayout.addWidget(self.middle_frame)
        self.buttom_bar = QtWidgets.QFrame(self.centralwidget)
        self.buttom_bar.setMaximumSize(QtCore.QSize(16777215, 75))
        self.buttom_bar.setStyleSheet("")
        self.buttom_bar.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.buttom_bar.setFrameShadow(QtWidgets.QFrame.Raised)
        self.buttom_bar.setObjectName("buttom_bar")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.buttom_bar)
        self.horizontalLayout.setContentsMargins(9, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.frame_4 = QtWidgets.QFrame(self.buttom_bar)
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame_4)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.frame_6 = QtWidgets.QFrame(self.frame_4)
        self.frame_6.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_6.setObjectName("frame_6")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame_6)
        self.verticalLayout_2.setContentsMargins(314, 0, 0, 0)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.frame_7 = QtWidgets.QFrame(self.frame_6)
        self.frame_7.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_7.setObjectName("frame_7")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.frame_7)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.frame_9 = QtWidgets.QFrame(self.frame_7)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_9.sizePolicy().hasHeightForWidth())
        self.frame_9.setSizePolicy(sizePolicy)
        self.frame_9.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_9.setObjectName("frame_9")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.frame_9)
        self.horizontalLayout_6.setContentsMargins(0, 5, 0, 5)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_5 = QtWidgets.QLabel(self.frame_9)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_6.addWidget(self.label_5)
        self.source_txt = QtWidgets.QTextEdit(self.frame_9)
        self.source_txt.setReadOnly(True)
        self.source_txt.setObjectName("source_txt")
        self.horizontalLayout_6.addWidget(self.source_txt)
        self.horizontalLayout_3.addWidget(self.frame_9)
        self.frame_10 = QtWidgets.QFrame(self.frame_7)
        self.frame_10.setMinimumSize(QtCore.QSize(30, 0))
        self.frame_10.setMaximumSize(QtCore.QSize(30, 16777215))
        self.frame_10.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_10.setObjectName("frame_10")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.frame_10)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.browse_source_btn = QtWidgets.QPushButton(self.frame_10)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.browse_source_btn.setFont(font)
        self.browse_source_btn.setObjectName("browse_source_btn")
        self.verticalLayout_3.addWidget(self.browse_source_btn)
        self.horizontalLayout_3.addWidget(self.frame_10)
        self.verticalLayout_2.addWidget(self.frame_7)
        self.frame_8 = QtWidgets.QFrame(self.frame_6)
        self.frame_8.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_8.setObjectName("frame_8")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.frame_8)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.frame_11 = QtWidgets.QFrame(self.frame_8)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_11.sizePolicy().hasHeightForWidth())
        self.frame_11.setSizePolicy(sizePolicy)
        self.frame_11.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_11.setObjectName("frame_11")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.frame_11)
        self.horizontalLayout_5.setContentsMargins(0, 5, 0, 5)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_6 = QtWidgets.QLabel(self.frame_11)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_5.addWidget(self.label_6)
        self.destination_txt = QtWidgets.QTextEdit(self.frame_11)
        self.destination_txt.setReadOnly(True)
        self.destination_txt.setObjectName("destination_txt")
        self.horizontalLayout_5.addWidget(self.destination_txt)
        self.horizontalLayout_4.addWidget(self.frame_11)
        self.frame_12 = QtWidgets.QFrame(self.frame_8)
        self.frame_12.setMinimumSize(QtCore.QSize(30, 0))
        self.frame_12.setMaximumSize(QtCore.QSize(30, 16777215))
        self.frame_12.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_12.setObjectName("frame_12")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.frame_12)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.browse_destination_btn = QtWidgets.QPushButton(self.frame_12)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.browse_destination_btn.setFont(font)
        self.browse_destination_btn.setObjectName("browse_destination_btn")
        self.verticalLayout_4.addWidget(self.browse_destination_btn)
        self.horizontalLayout_4.addWidget(self.frame_12)
        self.verticalLayout_2.addWidget(self.frame_8)
        self.horizontalLayout_2.addWidget(self.frame_6)
        self.horizontalLayout.addWidget(self.frame_4)
        self.frame_5 = QtWidgets.QFrame(self.buttom_bar)
        self.frame_5.setMinimumSize(QtCore.QSize(150, 0))
        self.frame_5.setMaximumSize(QtCore.QSize(100, 16777215))
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.frame_5)
        self.horizontalLayout_7.setContentsMargins(-1, -1, 45, -1)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.convert_btn = QtWidgets.QPushButton(self.frame_5)
        self.convert_btn.setObjectName("convert_btn")
        self.horizontalLayout_7.addWidget(self.convert_btn)
        self.horizontalLayout.addWidget(self.frame_5)
        self.verticalLayout.addWidget(self.buttom_bar)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Video2GIF"))
        self.label.setText(_translate("MainWindow", "Easy Video to Gif Converter"))
        self.groupBox_3.setTitle(_translate("MainWindow", "Frames Per Second"))
        self.label_4.setText(_translate("MainWindow", "      FPS:"))
        self.groupBox_2.setTitle(_translate("MainWindow", "Image Size"))
        self.keep_ratio_btn.setText(_translate("MainWindow", "Keep Ratio"))
        self.label_2.setText(_translate("MainWindow", "Width:"))
        self.label_3.setText(_translate("MainWindow", "Height:"))
        self.groupBox.setTitle(_translate("MainWindow", "Trimming"))
        self.play_btn.setText(_translate("MainWindow", "Play"))
        self.progressBar.setFormat(_translate("MainWindow", "%p"))
        self.label_5.setText(_translate("MainWindow", "         Source:"))
        self.browse_source_btn.setText(_translate("MainWindow", "..."))
        self.label_6.setText(_translate("MainWindow", "Destination:"))
        self.browse_destination_btn.setText(_translate("MainWindow", "..."))
        self.convert_btn.setText(_translate("MainWindow", "Convert"))
