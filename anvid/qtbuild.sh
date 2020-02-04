#!/usr/bin/env bash
python -m PyQt5.uic.pyuic -x videoannwidget.ui -o ui_videoannwidget.py
python -m PyQt5.uic.pyuic -x settingsdialog.ui -o ui_settingsdialog.py
pyrcc5 -o resources.py resources.qrc
