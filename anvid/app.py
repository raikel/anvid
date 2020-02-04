import glob
import os
from typing import Tuple

from PyQt5 import QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QFileDialog, QListWidgetItem, QAbstractItemView

import values
from applog import logger
from projects import Project, VideoAnn
from settings import (
    AppSettings,
    MAX_RECENT_FILES,
    PROJECT_FILE_EXT,
    VIDEO_EXTENSIONS
)
from ui_mainwindow import Ui_MainWindow
from video import VideoAnnoWidget


class MainWindow(QtWidgets.QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()
        
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.connectActions()

        self.videoAnnoWidget = VideoAnnoWidget(self)
        self.setCentralWidget(self.videoAnnoWidget)

        self.project: Project = Project()
        self.appSettings: AppSettings = AppSettings()
        self.loadAppSettings()

    def closeEvent(self, event):
        self.saveProject()
        self.saveAppSettings()
        event.accept()

    def loadAppSettings(self):

        try:
            self.appSettings = AppSettings.load()
        except Exception as err:
            logger.error(err)

        self.ui.pos = self.appSettings.mainWindowPos
        self.ui.size = self.appSettings.mainWindowSize

        lastProjectPath = self.appSettings.lastProjectPath
        if lastProjectPath and os.path.exists(lastProjectPath):
            self.loadProjectFile(lastProjectPath)
        self.updateRecentProjectsActions()

    def saveAppSettings(self):
        self.appSettings.mainWindowPos = self.ui.pos
        self.appSettings.mainWindowSize = self.ui.size

        try:
            self.appSettings.save()
        except Exception as err:
            logger.error(err)
            self.ui.errorMsg('Error saving application settings')

    def setCurrentProject(self):

        projectName = self.project.projectName
        self.setWindowTitle(f'{projectName} - {values.appName}')

        recentPaths = self.appSettings.recentFiles
        currentPath = self.project.projectPath

        if currentPath in recentPaths:
            recentPaths.remove(currentPath)
        else:
            pass

        recentPaths.insert(0, currentPath)
        del recentPaths[MAX_RECENT_FILES:]

        self.appSettings.recentFiles = recentPaths
        self.appSettings.lastProjectPath = currentPath
        self.updateRecentProjectsActions()
        self.saveAppSettings()

    def updateRecentProjectsActions(self):

        menu = self.ui.openRecentAct.menu()
        if menu.isEmpty():
            for i in range(MAX_RECENT_FILES):
                action = QtWidgets.QAction(self)
                action.visible = False
                action.triggered.connect(self.openRecentProject)
                menu.addAction(action)

        recentPaths = self.appSettings.recentFiles
        recentPaths[:] = [
            file for file in recentPaths
            if os.path.exists(file)
        ]
        self.appSettings.recentFiles = recentPaths

        if len(recentPaths) == 0:
            self.ui.openRecentAct.setDisabled(True)
            return
        self.ui.openRecentAct.setDisabled(False)

        numRecentFiles = min(len(recentPaths), MAX_RECENT_FILES)
        actions = menu.actions()
        for i in range(numRecentFiles):
            fileName = os.path.basename(recentPaths[i])
            text = f'&{i + 1} {fileName}'
            actions[i].setText(text)
            actions[i].setData(recentPaths[i])
            actions[i].setVisible(True)

        for j in range(numRecentFiles, MAX_RECENT_FILES):
            actions[j].setVisible(False)

    def initVideoList(self):
        listWidget = self.ui.videoListWidget
        listWidget.clear()
        for videoPath in self.project.videosAnn.keys():
            name = os.path.basename(videoPath)
            item = QListWidgetItem(name)
            item.setData(Qt.UserRole, videoPath)
            listWidget.addItem(item)

        if listWidget.count() == 0:
            self.videoAnnoWidget.videoAnn = None
        else:
            if self.project.selectVideoInd > listWidget.count() - 1:
                self.project.selectVideoInd = 0

            item = listWidget.item(self.project.selectVideoInd)
            listWidget.setCurrentItem(item)
            self.onVideoSelectionChanged()

    ######################################################################
    #  Actions
    ######################################################################

    def newProject(self):
        self.saveProject()
        se = Project()
        self.loadProject(se)

    def addVideoDir(self):
        project = self.project
        dirPath = QFileDialog.getExistingDirectory(
            self,
            values.selectDirDialogTitle,
            self.appSettings.lastAddVideoDir,
            options=QFileDialog.DontUseNativeDialog | QFileDialog.ShowDirsOnly
        )
        if dirPath:
            self.appSettings.lastAddVideoDir = dirPath
            videoPaths = list_files(
                dirPath, self.appSettings.videoExt, recursive=True
            )
            if len(videoPaths):
                for videoPath in videoPaths:
                    videoAnn = VideoAnn(videoPath=videoPath)
                    project.videosAnn[videoPath] = videoAnn
                self.initVideoList()
                self.project.empty = False
            else:
                self.ui.warnMsg(
                    f'Could not find any video file on directory {dirPath}.'
                )

    def delVideos(self):
        items = self.ui.videoListWidget.selectedItems()
        if len(items):
            for item in items:
                videoPath = item.data(Qt.UserRole)
                del self.project.videosAnn[videoPath]
            self.initVideoList()
        else:
            self.ui.warnMsg('Please select the videos you want to remove.')

    def openProject(self):
        filePath, _ = QFileDialog.getOpenFileName(
            self,
            values.openProjectDialogTitle,
            self.appSettings.lastProjectPath,
            f'{values.appName} files (*{PROJECT_FILE_EXT})',
            options=QFileDialog.DontUseNativeDialog
        )
        if filePath:
            self.appSettings.lastProjectPath = filePath
            self.loadProjectFile(filePath)

    def openRecentProject(self):
        action = self.sender()
        if action:
            self.loadProjectFile(action.data())

    def loadProjectFile(self, filePath):
        try:
            projectSettings = Project.load(filePath)
        except Exception as err:
            logger.error(err)
            self.ui.errorMsg(f'Error loading project {filePath}.')
            self.updateRecentProjectsActions()
        else:
            self.loadProject(projectSettings)

    def loadProject(self, project: Project):
        self.project = project
        self.setCurrentProject()
        self.initVideoList()

    def saveProject(self):
        if self.project.empty:
            return

        savePath = self.project.projectPath
        if not savePath:
            savePath, _ = QFileDialog.getSaveFileName(
                self,
                values.saveProjectDialogTitle,
                self.appSettings.lastProjectPath,
                f'{values.appName} files (*{PROJECT_FILE_EXT})',
                options=QFileDialog.DontUseNativeDialog
            )
            if savePath:
                _, ext = os.path.splitext(savePath)
                if ext != PROJECT_FILE_EXT:
                    savePath += PROJECT_FILE_EXT
                self.project.projectPath = savePath

        if savePath:
            try:
                self.project.save()
                self.appSettings.lastProjectPath = savePath
            except Exception as err:
                logger.error(err)
                self.ui.errorMsg(values.saveProjectErrorMessage)

    def setSettings(self):
        self.setSettingsWidgetsValues()
        dialog = self.ui.settingsDialog
        if dialog.exec_():
            self.getSettingsWidgetsValues()

    def getSettingsWidgetsValues(self):
        ui = self.ui.settingsDialog.ui
        pr = self.project
        se = self.appSettings

        pr.annTemplate = ui.annFormatEdit.text()
        se.videoExt = ui.videoExtEdit.text().split()

    def setSettingsWidgetsValues(self):
        ui = self.ui.settingsDialog.ui
        pr = self.project
        se = self.appSettings

        ui.annFormatEdit.setText(pr.annTemplate)
        ui.videoExtEdit.setText(' '.join(se.videoExt))

    def onVideoSelectionChanged(self):
        ind = self.ui.videoListWidget.currentRow()
        videoPath = list(self.project.videosAnn.keys())[ind]
        self.videoAnnoWidget.videoAnn = self.project.videosAnn[videoPath]
        self.project.selectVideoInd = ind

    def export(self):
        savePath, _ = QFileDialog.getSaveFileName(
            self,
            values.exportDialogTitle,
            self.appSettings.lastExportPath,
            options=QFileDialog.DontUseNativeDialog
        )
        if savePath:
            with open(savePath, 'wt') as fi:
                fi.write(self.project.toText())
                self.appSettings.lastExportPath = savePath

    def aboutAction(self):
        QtWidgets.QMessageBox.about(
            self,
            values.aboutDialogTitle,
            values.aboutDialogMessage
        )

    def connectActions(self):

        self.ui.newProjectAct.triggered.connect(self.newProject)
        self.ui.addVideoDirAct.triggered.connect(self.addVideoDir)
        self.ui.delVideosAct.triggered.connect(self.delVideos)
        self.ui.openProjectAct.triggered.connect(self.openProject)
        self.ui.saveProjectAct.triggered.connect(self.saveProject)
        self.ui.setSettingsAct.triggered.connect(self.setSettings)
        self.ui.exportAct.triggered.connect(self.export)
        # noinspection PyTypeChecker
        self.ui.exitAct.triggered.connect(self.close)
        self.ui.aboutAct.triggered.connect(self.aboutAction)

        # noinspection PyUnresolvedReferences
        self.ui.videoListWidget.itemDoubleClicked.connect(
            self.onVideoSelectionChanged
        )


def list_files(
    root_path: str,
    extensions: Tuple[str, ...],
    recursive: bool = True
):
    file_paths = []
    for ext in extensions:
        if recursive:
            root_path_ext = os.path.join(root_path, f'**/*{ext}')
            file_paths.extend(glob.iglob(root_path_ext, recursive=True))
        else:
            root_path_ext = os.path.join(root_path, f'*{ext}')
            file_paths.extend(glob.iglob(root_path_ext, recursive=False))

    return file_paths


if __name__ == '__main__':

    import sys

    app = QtWidgets.QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.show()
    sys.exit(app.exec_())
