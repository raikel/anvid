from typing import List

from PyQt5 import QtCore
from PyQt5.QtGui import QColor
from PyQt5.QtGui import QImage, QPainter
from PyQt5.QtWidgets import QLabel

from projects import Segment


class SegmentColorBar(QLabel):

    def __init__(self, parent=None):
        super(SegmentColorBar, self).__init__(parent)

        self.markColor: QColor = QColor('#f0134d')
        self.barColor: QColor = QColor('#35495e')
        self._segments: List[Segment] = []
        self._length: float = 1
        self._nColors = 300
        self._image: QImage = QImage(self._nColors, 1, QImage.Format_RGB32)

        self._image.fill(self.barColor)

    @property
    def segments(self):
        return self._segments

    @property
    def length(self):
        return self._length

    @length.setter
    def length(self, length):
        self._length = length
        self.updateImage()

    @segments.setter
    def segments(self, segments: List[Segment]):
        self._segments = segments
        self.updateImage()

    def updateImage(self):
        self._image.fill(self.barColor)

        if len(self._segments) and self._length:
            w = self._nColors
            length = self._length
            segments = [
                (
                    int(min(1, max(0, s[0]/length)) * w),
                    int(min(1, max(0, s[1]/length)) * w)
                ) for s in self._segments
            ]

            for s in segments:
                for p in range(s[0], s[1]):
                    self._image.setPixelColor(p, 0, self.markColor)

        self.update()

    def paintEvent(self, event):

        painter = QPainter(self)
        painter.setPen(QtCore.Qt.NoPen)
        painter.drawImage(self.contentsRect(), self._image)