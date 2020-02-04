# -*- coding: utf-8 -*-
from typing import Tuple

from PyQt5 import QtCore
from PyQt5.QtGui import QKeySequence, QIcon
from PyQt5.QtWidgets import (
    QAction,
    QMenu,
    QDockWidget,
    QMessageBox,
    QDialog,
    QToolBar,
    QMainWindow,
    QListWidget,
    QAbstractItemView)

# noinspection PyUnresolvedReferences
import resources
import settings
import values
from ui_settingsdialog import Ui_SettingsDialog


# noinspection PyPep8Naming
class Ui_MainWindow:

    # noinspection PyTypeChecker
    def __init__(self):
        self.mainWindow: QMainWindow = None
        self.videoListDockWidget: QDockWidget = None
        self.videoListWidget: QListWidget = None

        self.newProjectAct: QAction = None
        self.addVideoDirAct: QAction = None
        self.delVideosAct: QAction = None
        self.openProjectAct: QAction = None
        self.openRecentAct: QAction = None
        self.saveProjectAct: QAction = None
        self.setSettingsAct: QAction = None
        self.exitAct: QAction = None
        self.aboutAct: QAction = None
        self.toggleVideoListViewAct: QAction = None
        self.exportAct: QAction = None

        self.fileMenu: QMenu = None
        self.projectMenu: QMenu = None
        self.helpMenu: QMenu = None
        self.fileToolBar: QToolBar = None
        self.projectToolBar: QToolBar = None
        self.settingsDialog: SettingsDialog = None

    def setupUi(self, mainWindow):
        
        self.mainWindow = mainWindow
        self.createDockWidgets()
        self.createActions()        
        self.createMenus()
        self.createToolBars()
        self.createStatusBar()
        self.createDialogs()

        self.mainWindow.setWindowIcon(QIcon(values.logoImage))

    @property
    def pos(self) -> Tuple[int, int]:
        pos = self.mainWindow.pos()
        return pos.x(), pos.y()

    @pos.setter
    def pos(self, pos: Tuple[int, int]):
        if pos[0] > 0 and pos[1] > 0:
            self.mainWindow.move(pos[0], pos[1])

    @property
    def size(self):
        size = self.mainWindow.size()
        return size.width(), size.height()

    @size.setter
    def size(self, size: Tuple[int, int]):
        self.mainWindow.resize(size[0], size[1])

    ######################################################################
    #  Initialization
    ######################################################################

    def createDockWidgets(self):

        self.videoListDockWidget = panel = QDockWidget(
            values.videoListPanelTitle,
            self.mainWindow
        )
        panel.setAllowedAreas(QtCore.Qt.LeftDockWidgetArea)
        self.mainWindow.addDockWidget(QtCore.Qt.LeftDockWidgetArea, panel)
        # panel.close()

        self.videoListWidget = QListWidget(panel)
        self.videoListWidget.setSelectionMode(
            QAbstractItemView.ExtendedSelection
        )
        panel.setWidget(self.videoListWidget)

    def createActions(self):

        self.newProjectAct = QAction(
            QIcon(values.newProjectImage),
            values.newProjectActText,
            self.mainWindow
        )
        self.newProjectAct.setShortcut(QKeySequence.New)
        self.newProjectAct.setStatusTip(values.newProjectActTip)

        self.addVideoDirAct = QAction(
            QIcon(values.addVideoDirImage),
            values.addVideoDirActText,
            self.mainWindow
        )
        self.addVideoDirAct.setStatusTip(values.addVideoDirActTip)

        self.delVideosAct = QAction(
            QIcon(values.delVideosImage),
            values.delVideosActText,
            self.mainWindow
        )
        self.delVideosAct.setShortcut(QKeySequence.Delete)
        self.delVideosAct.setStatusTip(values.delVideosActTip)

        self.openProjectAct = QAction(
            QIcon(values.openProjectImage),
            values.openProjectActText,
            self.mainWindow
        )
        self.openProjectAct.setShortcut(QKeySequence.Open)
        self.openProjectAct.setStatusTip(values.openProjectActTip)

        self.openRecentAct = QAction(
            values.openRecentActText,
            self.mainWindow
        )
        self.openRecentAct.setMenu(QMenu())
        
        self.saveProjectAct = QAction(
            QIcon(values.saveProjectImage),
            values.saveProjectActText,
            self.mainWindow
        )
        self.saveProjectAct.setShortcut(QKeySequence.Save)
        self.saveProjectAct.setStatusTip(values.saveProjectActTip)

        self.setSettingsAct = QAction(
            QIcon(values.settingsImage),
            values.settingsActText,
            self.mainWindow
        )
        self.setSettingsAct.setStatusTip(values.settingsActTip)
            
        self.exitAct = QAction(
            values.exitActText,
            self.mainWindow
        )
        self.exitAct.setShortcut("Ctrl+Q")

        self.aboutAct = QAction(
            values.aboutActText,
            self.mainWindow
        )

        action = self.videoListDockWidget.toggleViewAction()
        action.setIcon(QIcon(values.panelViewImage))
        action.setText(values.togglePanelViewActText)
        action.setStatusTip(values.togglePanelViewActTip)
        self.toggleVideoListViewAct = action

        self.exportAct = QAction(
            QIcon(values.exportImage),
            values.exportActText,
            self.mainWindow
        )
        self.saveProjectAct.setStatusTip(values.exportActTip)

    def createMenus(self):

        mainMenu = self.mainWindow.menuBar()

        self.fileMenu = mainMenu.addMenu(values.fileMenuText)
        self.fileMenu.addAction(self.newProjectAct)
        self.fileMenu.addAction(self.openProjectAct)
        self.fileMenu.addAction(self.openRecentAct)
        self.fileMenu.addAction(self.saveProjectAct)
        self.fileMenu.addSeparator()
        self.fileMenu.addAction(self.exitAct)

        self.projectMenu = mainMenu.addMenu(values.projectMenuText)
        self.projectMenu.addAction(self.toggleVideoListViewAct)
        self.projectMenu.addAction(self.addVideoDirAct)
        self.projectMenu.addAction(self.delVideosAct)
        self.projectMenu.addAction(self.exportAct)
        self.projectMenu.addAction(self.setSettingsAct)

        self.helpMenu = self.mainWindow.menuBar().addMenu(values.helpMenuText)
        self.helpMenu.addAction(self.aboutAct)

    def createToolBars(self):
        size = settings.TOOLBAR_ICON_SIZE
        iconSize = QtCore.QSize(size, size)

        self.fileToolBar = QToolBar(self.mainWindow)
        self.mainWindow.addToolBar(self.fileToolBar)
        self.fileToolBar.setIconSize(iconSize)
        self.fileToolBar.addAction(self.newProjectAct)
        self.fileToolBar.addAction(self.openProjectAct)
        self.fileToolBar.addAction(self.saveProjectAct)

        self.projectToolBar = QToolBar(self.mainWindow)
        self.mainWindow.addToolBar(self.projectToolBar)
        self.projectToolBar.setIconSize(iconSize)
        self.projectToolBar.addAction(self.toggleVideoListViewAct)
        self.projectToolBar.addAction(self.addVideoDirAct)
        self.projectToolBar.addAction(self.delVideosAct)
        self.projectToolBar.addAction(self.exportAct)
        self.projectToolBar.addAction(self.setSettingsAct)

    def createStatusBar(self):
        self.mainWindow.statusBar().showMessage("Ready")

    def createDialogs(self):
        self.settingsDialog = SettingsDialog(self.mainWindow)

    def errorMsg(self, msg):
        QMessageBox.critical(
            self.mainWindow,
            values.errorDialogTitle,
            msg
        )

    def warnMsg(self, msg: str, title: str = '', buttons=None):
        if not title:
            title = values.warnDialogTitle
        if buttons is None:
            ret = QMessageBox.warning(self.mainWindow, title, msg)
        else:
            ret = QMessageBox.warning(self.mainWindow, title, msg, buttons)
        return ret
    

class SettingsDialog(QDialog):
    def __init__(self, parent=None):
        super(SettingsDialog, self).__init__(parent)
        # Set up the user interface from Designer.
        self.ui = Ui_SettingsDialog()
        self.ui.setupUi(self)
        self.setWindowTitle(values.settingsDialogTitle)

        helpFlag = QtCore.Qt.WindowContextHelpButtonHint
        self.setWindowFlags(self.windowFlags() & ~helpFlag)
        self.setFixedSize(self.size())
