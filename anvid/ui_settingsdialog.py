# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'settingsdialog.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_SettingsDialog(object):
    def setupUi(self, SettingsDialog):
        SettingsDialog.setObjectName("SettingsDialog")
        SettingsDialog.resize(540, 207)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(SettingsDialog.sizePolicy().hasHeightForWidth())
        SettingsDialog.setSizePolicy(sizePolicy)
        SettingsDialog.setToolTip("")
        self.buttonBox = QtWidgets.QDialogButtonBox(SettingsDialog)
        self.buttonBox.setGeometry(QtCore.QRect(10, 170, 521, 31))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setCenterButtons(False)
        self.buttonBox.setObjectName("buttonBox")
        self.annFormatEdit = QtWidgets.QLineEdit(SettingsDialog)
        self.annFormatEdit.setGeometry(QtCore.QRect(10, 40, 521, 30))
        self.annFormatEdit.setObjectName("annFormatEdit")
        self.label = QtWidgets.QLabel(SettingsDialog)
        self.label.setGeometry(QtCore.QRect(10, 20, 211, 18))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(SettingsDialog)
        self.label_2.setGeometry(QtCore.QRect(10, 90, 171, 18))
        self.label_2.setObjectName("label_2")
        self.videoExtEdit = QtWidgets.QLineEdit(SettingsDialog)
        self.videoExtEdit.setGeometry(QtCore.QRect(10, 110, 521, 30))
        self.videoExtEdit.setObjectName("videoExtEdit")

        self.retranslateUi(SettingsDialog)
        self.buttonBox.accepted.connect(SettingsDialog.accept)
        self.buttonBox.rejected.connect(SettingsDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(SettingsDialog)

    def retranslateUi(self, SettingsDialog):
        _translate = QtCore.QCoreApplication.translate
        SettingsDialog.setWindowTitle(_translate("SettingsDialog", "Dialog"))
        self.annFormatEdit.setText(_translate("SettingsDialog", "%VIDEO_NAME% %LABEL% %SEGMENTS%"))
        self.label.setText(_translate("SettingsDialog", "Annotation Export Format"))
        self.label_2.setText(_translate("SettingsDialog", "List Video Extensions"))
        self.videoExtEdit.setText(_translate("SettingsDialog", ".mp4 .mkv .avi .mpeg .mov .wmv"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    SettingsDialog = QtWidgets.QDialog()
    ui = Ui_SettingsDialog()
    ui.setupUi(SettingsDialog)
    SettingsDialog.show()
    sys.exit(app.exec_())
