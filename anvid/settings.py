import pickle
from os import path, mkdir
from typing import List, Tuple

DATA_DIR_NAME = '.data'

APP_SETTINGS_FILE_NAME: str = 'settings'

MAX_RECENT_FILES: int = 10

TOOLBAR_ICON_SIZE = 32

VIDEO_EXTENSIONS: Tuple[str, ...] = (
    '.mp4',
    '.mpeg',
    '.avi',
    '.mkv',
    '.wmv',
    '.mov'
)

PROJECT_FILE_EXT = '.anv'

currDir = path.dirname(path.abspath(__file__))
rootPath = path.join(currDir, DATA_DIR_NAME)

if not path.exists(rootPath) or not path.isdir(rootPath):
    mkdir(rootPath)

APP_SETTINGS_PATH = path.join(rootPath, APP_SETTINGS_FILE_NAME)


class AppSettings:
    def __init__(self):
        self.recentFiles: List[str] = []
        self.mainWindowPos: Tuple[int, int] = (-1, -1)
        self.mainWindowSize: Tuple[int, int] = (1280, 720)
        self.lastProjectPath: str = ''
        self.lastExportPath: str = ''
        self.lastAddVideoDir: str = ''
        self.videoExt = VIDEO_EXTENSIONS

    def save(self):
        with open(APP_SETTINGS_PATH, 'wb') as appFile:
            pickle.dump(self, appFile)

    @staticmethod
    def load() -> 'AppSettings':
        with open(APP_SETTINGS_PATH, 'rb') as appFile:
            return pickle.load(appFile)


if not path.exists(APP_SETTINGS_PATH) or not path.isfile(APP_SETTINGS_PATH):
    AppSettings().save()


# class VideoAnn:
#     def __init__(
#         self,
#         videoPath: str = '',
#         segments: List[Segment] = None,
#         videoPosition: float = 0,
#         selSegmentInd: int = -1,
#     ):
#         self.videoPath: str = videoPath
#         self.segments: List[Segment] = segments
#         self.videoPosition: float = videoPosition
#         self.selSegmentInd: int = selSegmentInd
#         self.paused = False
#         self.label: str = ''
#         self.step: int = 50
#         self.duration: float = 1
#
#         if self.segments is None:
#             self.segments = []
#
#     def toText(self, template: str = ANN_TEMPLATE):
#
#         video_name = path.basename(self.videoPath)
#         template = template.replace('%VIDEO_NAME%', video_name)
#         template = template.replace('%VIDEO_PATH%', self.videoPath)
#         template = template.replace('%LABEL%', self.label)
#
#         segments = []
#         ds = self.duration
#
#         if ds > 0:
#             for s in self.segments:
#                 if (s[1] > s[0]) and (0 < s[1] < ds) and (0 < s[0] < ds):
#                     ss = f'{s[0] / self.duration} {s[1] / self.duration}'
#                 else:
#                     ss = '-1 -1'
#                 segments.append(ss)
#             segments = ' '.join(segments)
#         else:
#             segments = ' '
#
#         template = template.replace('%SEGMENTS%', segments)
#
#         return template
#
#
# class Project:
#     # noinspection PyTypeChecker
#     def __init__(self):
#         self.projectPath: str = ''
#         self.videoPaths: List[str] = []
#         self.selectVideoInd: int = 0
#         self.videosAnn: Dict[str, VideoAnn] = {}
#
#     def save(self):
#         with open(self.projectPath, 'wb') as projectFile:
#             pickle.dump(self, projectFile)
#
#     @property
#     def projectName(self):
#         if self.projectPath:
#             name, _ = path.splitext(path.basename(self.projectPath))
#             return name
#         return ''
#
#     @staticmethod
#     def load(projectPath) -> 'Project':
#         with open(projectPath, 'rb') as projectFile:
#             return pickle.load(projectFile)
#
#     def toText(self, template: str = ANN_TEMPLATE):
#         return '\n'.join([
#             va.toText(template=template)
#             for va in self.videosAnn.values()
#         ])
