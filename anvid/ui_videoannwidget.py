# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'videoannwidget.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_VideoAnnoWidget(object):
    def setupUi(self, VideoAnnoWidget):
        VideoAnnoWidget.setObjectName("VideoAnnoWidget")
        VideoAnnoWidget.resize(1168, 750)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(VideoAnnoWidget)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setContentsMargins(4, 8, 8, 4)
        self.verticalLayout.setObjectName("verticalLayout")
        self.videoWidget = QVideoWidget(VideoAnnoWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.videoWidget.sizePolicy().hasHeightForWidth())
        self.videoWidget.setSizePolicy(sizePolicy)
        self.videoWidget.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.videoWidget.setObjectName("videoWidget")
        self.verticalLayout.addWidget(self.videoWidget)
        self.segmentColorBar = SegmentColorBar(VideoAnnoWidget)
        self.segmentColorBar.setMaximumSize(QtCore.QSize(16777215, 12))
        self.segmentColorBar.setText("")
        self.segmentColorBar.setObjectName("segmentColorBar")
        self.verticalLayout.addWidget(self.segmentColorBar)
        self.positionSlider = QtWidgets.QSlider(VideoAnnoWidget)
        self.positionSlider.setOrientation(QtCore.Qt.Horizontal)
        self.positionSlider.setObjectName("positionSlider")
        self.verticalLayout.addWidget(self.positionSlider)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setSizeConstraint(QtWidgets.QLayout.SetMinimumSize)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.playButton = QtWidgets.QPushButton(VideoAnnoWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.playButton.sizePolicy().hasHeightForWidth())
        self.playButton.setSizePolicy(sizePolicy)
        self.playButton.setMinimumSize(QtCore.QSize(30, 30))
        self.playButton.setMaximumSize(QtCore.QSize(30, 30))
        self.playButton.setBaseSize(QtCore.QSize(30, 30))
        self.playButton.setText("")
        self.playButton.setObjectName("playButton")
        self.horizontalLayout_2.addWidget(self.playButton)
        self.stepBackwardButton = QtWidgets.QPushButton(VideoAnnoWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.stepBackwardButton.sizePolicy().hasHeightForWidth())
        self.stepBackwardButton.setSizePolicy(sizePolicy)
        self.stepBackwardButton.setMinimumSize(QtCore.QSize(30, 30))
        self.stepBackwardButton.setMaximumSize(QtCore.QSize(30, 30))
        self.stepBackwardButton.setText("")
        self.stepBackwardButton.setObjectName("stepBackwardButton")
        self.horizontalLayout_2.addWidget(self.stepBackwardButton)
        self.stepForwardButton = QtWidgets.QPushButton(VideoAnnoWidget)
        self.stepForwardButton.setMinimumSize(QtCore.QSize(30, 30))
        self.stepForwardButton.setMaximumSize(QtCore.QSize(30, 30))
        self.stepForwardButton.setText("")
        self.stepForwardButton.setObjectName("stepForwardButton")
        self.horizontalLayout_2.addWidget(self.stepForwardButton)
        self.curTimeLabel = QtWidgets.QLabel(VideoAnnoWidget)
        self.curTimeLabel.setObjectName("curTimeLabel")
        self.horizontalLayout_2.addWidget(self.curTimeLabel)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.label = QtWidgets.QLabel(VideoAnnoWidget)
        self.label.setObjectName("label")
        self.horizontalLayout_2.addWidget(self.label)
        self.stepSpinBox = QtWidgets.QSpinBox(VideoAnnoWidget)
        self.stepSpinBox.setMinimumSize(QtCore.QSize(100, 30))
        self.stepSpinBox.setMaximumSize(QtCore.QSize(100, 30))
        self.stepSpinBox.setMinimum(50)
        self.stepSpinBox.setMaximum(999999999)
        self.stepSpinBox.setObjectName("stepSpinBox")
        self.horizontalLayout_2.addWidget(self.stepSpinBox)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.verticalLayout.setStretch(0, 1)
        self.horizontalLayout_3.addLayout(self.verticalLayout)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_3 = QtWidgets.QLabel(VideoAnnoWidget)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_4.addWidget(self.label_3)
        self.labelLineEdit = QtWidgets.QLineEdit(VideoAnnoWidget)
        self.labelLineEdit.setObjectName("labelLineEdit")
        self.horizontalLayout_4.addWidget(self.labelLineEdit)
        self.verticalLayout_4.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.label_5 = QtWidgets.QLabel(VideoAnnoWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy)
        self.label_5.setMaximumSize(QtCore.QSize(16777215, 20))
        self.label_5.setObjectName("label_5")
        self.verticalLayout_5.addWidget(self.label_5)
        self.startTimeLabel = QtWidgets.QLabel(VideoAnnoWidget)
        self.startTimeLabel.setStyleSheet("background-color: rgb(195, 195, 195);")
        self.startTimeLabel.setObjectName("startTimeLabel")
        self.verticalLayout_5.addWidget(self.startTimeLabel)
        self.getStartTimeButton = QtWidgets.QPushButton(VideoAnnoWidget)
        self.getStartTimeButton.setMinimumSize(QtCore.QSize(0, 30))
        self.getStartTimeButton.setMaximumSize(QtCore.QSize(16777215, 30))
        self.getStartTimeButton.setObjectName("getStartTimeButton")
        self.verticalLayout_5.addWidget(self.getStartTimeButton)
        self.horizontalLayout_6.addLayout(self.verticalLayout_5)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_2 = QtWidgets.QLabel(VideoAnnoWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setMaximumSize(QtCore.QSize(16777215, 20))
        self.label_2.setObjectName("label_2")
        self.verticalLayout_3.addWidget(self.label_2)
        self.endTimeLabel = QtWidgets.QLabel(VideoAnnoWidget)
        self.endTimeLabel.setStyleSheet("background-color: rgb(195, 195, 195);")
        self.endTimeLabel.setObjectName("endTimeLabel")
        self.verticalLayout_3.addWidget(self.endTimeLabel)
        self.getEndTimeButton = QtWidgets.QPushButton(VideoAnnoWidget)
        self.getEndTimeButton.setMinimumSize(QtCore.QSize(0, 30))
        self.getEndTimeButton.setMaximumSize(QtCore.QSize(16777215, 30))
        self.getEndTimeButton.setObjectName("getEndTimeButton")
        self.verticalLayout_3.addWidget(self.getEndTimeButton)
        self.horizontalLayout_6.addLayout(self.verticalLayout_3)
        self.verticalLayout_4.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_4 = QtWidgets.QLabel(VideoAnnoWidget)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_5.addWidget(self.label_4)
        self.addSegmentButton = QtWidgets.QPushButton(VideoAnnoWidget)
        self.addSegmentButton.setMinimumSize(QtCore.QSize(30, 30))
        self.addSegmentButton.setMaximumSize(QtCore.QSize(30, 30))
        self.addSegmentButton.setText("")
        self.addSegmentButton.setObjectName("addSegmentButton")
        self.horizontalLayout_5.addWidget(self.addSegmentButton)
        self.delSegmentButton = QtWidgets.QPushButton(VideoAnnoWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.delSegmentButton.sizePolicy().hasHeightForWidth())
        self.delSegmentButton.setSizePolicy(sizePolicy)
        self.delSegmentButton.setMinimumSize(QtCore.QSize(30, 30))
        self.delSegmentButton.setMaximumSize(QtCore.QSize(30, 30))
        self.delSegmentButton.setText("")
        self.delSegmentButton.setObjectName("delSegmentButton")
        self.horizontalLayout_5.addWidget(self.delSegmentButton)
        self.verticalLayout_4.addLayout(self.horizontalLayout_5)
        self.segmentListWidget = QtWidgets.QListWidget(VideoAnnoWidget)
        self.segmentListWidget.setObjectName("segmentListWidget")
        self.verticalLayout_4.addWidget(self.segmentListWidget)
        self.verticalLayout_4.setStretch(3, 1)
        self.horizontalLayout_3.addLayout(self.verticalLayout_4)
        self.horizontalLayout_3.setStretch(0, 1)

        self.retranslateUi(VideoAnnoWidget)
        QtCore.QMetaObject.connectSlotsByName(VideoAnnoWidget)

    def retranslateUi(self, VideoAnnoWidget):
        _translate = QtCore.QCoreApplication.translate
        VideoAnnoWidget.setWindowTitle(_translate("VideoAnnoWidget", "Form"))
        self.playButton.setToolTip(_translate("VideoAnnoWidget", "Play / Pause Video"))
        self.stepBackwardButton.setToolTip(_translate("VideoAnnoWidget", "Video Step Backward"))
        self.stepForwardButton.setToolTip(_translate("VideoAnnoWidget", "Video Step Forward"))
        self.curTimeLabel.setText(_translate("VideoAnnoWidget", "00:00:00"))
        self.label.setText(_translate("VideoAnnoWidget", "Step Size"))
        self.stepSpinBox.setSuffix(_translate("VideoAnnoWidget", " ms"))
        self.label_3.setText(_translate("VideoAnnoWidget", "Label"))
        self.label_5.setText(_translate("VideoAnnoWidget", "Segment Start"))
        self.startTimeLabel.setText(_translate("VideoAnnoWidget", "00:00:00"))
        self.getStartTimeButton.setToolTip(_translate("VideoAnnoWidget", "Grab Segment Start Time"))
        self.getStartTimeButton.setText(_translate("VideoAnnoWidget", "Grab Time"))
        self.label_2.setText(_translate("VideoAnnoWidget", "Segment End"))
        self.endTimeLabel.setText(_translate("VideoAnnoWidget", "00:00:00"))
        self.getEndTimeButton.setToolTip(_translate("VideoAnnoWidget", "Grab Segment End Time"))
        self.getEndTimeButton.setText(_translate("VideoAnnoWidget", "Grab Time"))
        self.label_4.setText(_translate("VideoAnnoWidget", "Segments"))
        self.addSegmentButton.setToolTip(_translate("VideoAnnoWidget", "Add New Segment"))
        self.delSegmentButton.setToolTip(_translate("VideoAnnoWidget", "Delete Selected Segment"))
from PyQt5.QtMultimediaWidgets import QVideoWidget
from widgets import SegmentColorBar


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    VideoAnnoWidget = QtWidgets.QWidget()
    ui = Ui_VideoAnnoWidget()
    ui.setupUi(VideoAnnoWidget)
    VideoAnnoWidget.show()
    sys.exit(app.exec_())
