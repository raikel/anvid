from datetime import timedelta

from PyQt5.QtCore import QUrl
from PyQt5.QtGui import QIcon
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent
from PyQt5.QtWidgets import QWidget, QListWidgetItem

import values
from applog import logger
from projects import VideoAnn
from ui_videoannwidget import Ui_VideoAnnoWidget


# https://stackoverflow.com/questions/45537627/qwidgetpaintengine-should-no-longer-be-called-appears-when-using-qmediaplay


class VideoAnnoWidget(QWidget):
    def __init__(self, parent=None):
        super(VideoAnnoWidget, self).__init__(parent)
        # Set up the user interface from Designer.
        self.ui = Ui_VideoAnnoWidget()
        self.ui.setupUi(self)
        ui = self.ui

        self._videoPath: str = ''

        self.player = QMediaPlayer(None, QMediaPlayer.VideoSurface)

        self.player.setVideoOutput(ui.videoWidget)
        # noinspection PyUnresolvedReferences
        self.player.stateChanged.connect(self.onPlayerStateChanged)
        # noinspection PyUnresolvedReferences
        self.player.positionChanged.connect(self.onPlayerPositionChanged)
        # noinspection PyUnresolvedReferences
        self.player.durationChanged.connect(self.onPlayerDurationChanged)
        # noinspection PyUnresolvedReferences
        self.player.error.connect(self.handlePlayerError)

        self.iconPlay = QIcon(values.playImage)
        self.iconPause = QIcon(values.pauseImage)

        ui.playButton.setIcon(self.iconPlay)
        ui.playButton.clicked.connect(self.videoPlayPause)

        ui.positionSlider.setRange(0, 0)
        ui.positionSlider.sliderMoved.connect(self.onSliderMoved)

        ui.addSegmentButton.clicked.connect(self.onAddSegment)
        ui.delSegmentButton.clicked.connect(self.onDelSegment)
        ui.getStartTimeButton.clicked.connect(self.onGrabStartTime)
        ui.getEndTimeButton.clicked.connect(self.onGrabEndTime)
        ui.segmentListWidget.itemSelectionChanged.connect(
            self.onItemSelectionChanged
        )
        ui.stepForwardButton.clicked.connect(self.onStepForward)
        ui.stepBackwardButton.clicked.connect(self.onStepBackward)
        ui.labelLineEdit.textChanged.connect(self.onLabelChanged)
        ui.stepSpinBox.valueChanged.connect(self.onStepChanged)

        ui.playButton.setEnabled(False)
        ui.stepForwardButton.setEnabled(False)
        ui.stepBackwardButton.setEnabled(False)
        ui.getStartTimeButton.setEnabled(False)
        ui.getEndTimeButton.setEnabled(False)
        ui.delSegmentButton.setEnabled(False)

        self._videoAnn: VideoAnn = VideoAnn()

        self.setIcons()

    def setIcons(self):
        ui = self.ui
        ui.addSegmentButton.setIcon(QIcon(values.addImage))
        ui.delSegmentButton.setIcon(QIcon(values.delImage))
        ui.stepForwardButton.setIcon(QIcon(values.stepForwardImage))
        ui.stepBackwardButton.setIcon(QIcon(values.stepBackwardImage))

    def onStepForward(self):
        if self.player.state() == QMediaPlayer.PlayingState:
            self.player.pause()
        curPosition = self.player.position()
        duration = self.player.duration()
        step = self.ui.stepSpinBox.value()
        position = min(curPosition + step, duration)
        self.player.setPosition(position)

    def onStepBackward(self):
        if self.player.state() == QMediaPlayer.PlayingState:
            self.player.pause()
        curPosition = self.player.position()
        step = self.ui.stepSpinBox.value()
        position = max(curPosition - step, 0)
        self.player.setPosition(position)

    def onLabelChanged(self, text):
        self._videoAnn.label = text

    def onStepChanged(self, value):
        self._videoAnn.step = value

    @property
    def videoAnn(self):
        return self._videoAnn

    @videoAnn.setter
    def videoAnn(self, videoAnn: VideoAnn):

        self._videoAnn = VideoAnn()

        if videoAnn is None:
            self.player.stop()
            self.ui.playButton.setEnabled(False)
            self.ui.stepForwardButton.setEnabled(False)
            self.ui.stepBackwardButton.setEnabled(False)
            self.ui.labelLineEdit.setText(self._videoAnn.label)
            self.ui.stepSpinBox.setValue(self._videoAnn.step)
            self.updateSegmentList()
            return

        state = self.player.state()
        if state in (QMediaPlayer.PlayingState, QMediaPlayer.PausedState):
            self.player.stop()

        qUrl = QUrl.fromLocalFile(videoAnn.videoPath)
        self.player.setMedia(QMediaContent(qUrl))
        self.ui.playButton.setEnabled(True)
        self.ui.stepForwardButton.setEnabled(True)
        self.ui.stepBackwardButton.setEnabled(True)

        if videoAnn.paused:
            self.player.pause()
        else:
            self.player.play()

        self.player.setPosition(int(videoAnn.videoPosition))

        self.ui.labelLineEdit.setText(videoAnn.label)
        self.ui.stepSpinBox.setValue(videoAnn.step)

        videoAnn.duration = self.player.duration()

        self._videoAnn = videoAnn

        self.updateSegmentList()

    def videoPlayPause(self):
        if self.player.state() == QMediaPlayer.PlayingState:
            self.player.pause()
        else:
            self.player.play()

    def onPlayerStateChanged(self, state):
        if state == QMediaPlayer.PlayingState:
            self.ui.playButton.setIcon(self.iconPause)
            self.videoAnn.paused = False
        elif state == QMediaPlayer.PausedState:
            self.ui.playButton.setIcon(self.iconPlay)
            self.videoAnn.paused = True

    def onPlayerPositionChanged(self, position):
        self.ui.positionSlider.setValue(position)
        curTime = int(position/1000)
        remTime = int((self.player.duration() - position) / 1000)
        curTime = str(timedelta(seconds=curTime))
        remTime = str(timedelta(seconds=remTime))
        self.ui.curTimeLabel.setText(curTime)
        self.ui.remTimeLabel.setText(remTime)
        self._videoAnn.videoPosition = position

    def onPlayerDurationChanged(self, duration):
        self.ui.positionSlider.setRange(0, duration)
        self._videoAnn.duration = duration

    def onSliderMoved(self, position):
        self.player.setPosition(position)

    def handlePlayerError(self):
        self.ui.playButton.setEnabled(False)
        error = self.player.errorString()
        logger.error(error)
        # self.ui.errorMsg(f'Media player error: {error}')

    def onAddSegment(self):
        self._videoAnn.segments.append([-1, -1])
        self._videoAnn.selSegmentInd = len(self._videoAnn.segments) - 1
        self.updateSegmentList()

    def onDelSegment(self):
        selSegmentInd = self._videoAnn.selSegmentInd
        del self._videoAnn.segments[selSegmentInd]
        if selSegmentInd > len(self._videoAnn.segments) - 1:
            self._videoAnn.selSegmentInd = len(self._videoAnn.segments) - 1
        self.updateSegmentList()

    def onGrabStartTime(self):
        selSegmentInd = self._videoAnn.selSegmentInd
        selSegment = self._videoAnn.segments[selSegmentInd]
        selSegment[0] = self.player.position()
        if selSegment[1] < selSegment[0]:
            selSegment[1] = selSegment[0]
        self.updateSegmentList()

    def onGrabEndTime(self):
        selSegmentInd = self._videoAnn.selSegmentInd
        selSegment = self._videoAnn.segments[selSegmentInd]
        selSegment[1] = self.player.position()
        if selSegment[1] < selSegment[0]:
            selSegment[0] = selSegment[1]
        self.updateSegmentList()

    def onItemSelectionChanged(self):
        selSegmentInd = self.ui.segmentListWidget.currentRow()
        if selSegmentInd < len(self._videoAnn.segments):
            self._videoAnn.selSegmentInd = selSegmentInd
            self.updateTimeLabels()

    def updateTimeLabels(self):
        selSegmentInd = self._videoAnn.selSegmentInd

        if selSegmentInd < 0:
            start, end = self.formatSegment([-1, -1])
            self.ui.startTimeLabel.setText(start)
            self.ui.endTimeLabel.setText(end)
        else:
            selSegment = self._videoAnn.segments[selSegmentInd]
            start, end = self.formatSegment(selSegment)
            self.ui.startTimeLabel.setText(start)
            self.ui.endTimeLabel.setText(end)
            if selSegment[0] >= 0 and selSegment[1] >= 0:
                self.player.setPosition(int(selSegment[0]))

    def updateSegmentList(self):
        segmentListWidget = self.ui.segmentListWidget
        selSegmentInd = self._videoAnn.selSegmentInd

        segmentListWidget.clear()
        for segment in self._videoAnn.segments:
            start, end = self.formatSegment(segment)
            item = QListWidgetItem(f'{start} -> {end}')
            segmentListWidget.addItem(item)

        if selSegmentInd < 0:
            self.ui.delSegmentButton.setDisabled(True)
            self.ui.getStartTimeButton.setDisabled(True)
            self.ui.getEndTimeButton.setDisabled(True)
        else:
            self.ui.delSegmentButton.setDisabled(False)
            self.ui.getStartTimeButton.setDisabled(False)
            self.ui.getEndTimeButton.setDisabled(False)
            item = segmentListWidget.item(selSegmentInd)
            segmentListWidget.setCurrentItem(item)

        self.updateTimeLabels()

    @staticmethod
    def formatSegment(segment):
        start, end = segment
        start = max(0, start)
        end = max(0, end)
        return _formatTimeDelta(start), _formatTimeDelta(end)


def _formatTimeDelta(ms):
    s = int(ms / 1000)
    ms = ms - 1000 * s
    return f'{timedelta(seconds=s)}.{ms:03d}'
