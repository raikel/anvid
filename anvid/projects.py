import pickle
from os import path
from typing import List, Dict

Segment = List[float]

ANN_TEMPLATE = '%VIDEO_NAME% %LABEL% %SEGMENTS%'


class VideoAnn:
    def __init__(
        self,
        videoPath: str = '',
        segments: List[Segment] = None,
        videoPosition: float = 0,
        selSegmentInd: int = -1,
    ):
        self.videoPath: str = videoPath
        self.segments: List[Segment] = segments
        self.videoPosition: float = videoPosition
        self.selSegmentInd: int = selSegmentInd
        self.paused = False
        self.label: str = ''
        self.step: int = 50
        self.duration: float = 1

        if self.segments is None:
            self.segments = []

    def toText(self, template: str):

        video_name = path.basename(self.videoPath)
        template = template.replace('%VIDEO_NAME%', video_name)
        template = template.replace('%VIDEO_PATH%', self.videoPath)
        template = template.replace('%LABEL%', self.label)

        segments = []
        ds = self.duration

        if ds > 0:
            for s in self.segments:
                if (s[1] > s[0]) and (0 < s[1] < ds) and (0 < s[0] < ds):
                    ss = f'{s[0] / self.duration} {s[1] / self.duration}'
                else:
                    ss = '-1 -1'
                segments.append(ss)
            segments = ' '.join(segments)
        else:
            segments = ' '

        template = template.replace('%SEGMENTS%', segments)

        return template


class Project:
    # noinspection PyTypeChecker
    def __init__(self):
        self.projectPath: str = ''
        self.selectVideoInd: int = 0
        self.videosAnn: Dict[str, VideoAnn] = {}
        self.annTemplate: str = ANN_TEMPLATE
        self.empty = True

    def save(self):
        with open(self.projectPath, 'wb') as projectFile:
            pickle.dump(self, projectFile)

    @property
    def projectName(self):
        if self.projectPath:
            name, _ = path.splitext(path.basename(self.projectPath))
            return name
        return ''

    @staticmethod
    def load(projectPath) -> 'Project':
        with open(projectPath, 'rb') as projectFile:
            return pickle.load(projectFile)

    def toText(self):
        return '\n'.join([
            va.toText(template=self.annTemplate)
            for va in self.videosAnn.values()
        ])
