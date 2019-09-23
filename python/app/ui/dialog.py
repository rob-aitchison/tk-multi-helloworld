# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'VREDWorkflow2.ui'
#
# Created: Mon Sep 16 14:34:21 2019
#      by: pyside-uic 0.2.15 running on PySide 1.2.4
#
# WARNING! All changes made in this file will be lost!

from sgtk.platform.qt import QtCore, QtGui

class Ui_VREDWorkflow(object):
    def setupUi(self, VREDWorkflow):
        VREDWorkflow.setObjectName("VREDWorkflow")
        VREDWorkflow.resize(800, 683)
        self.centralwidget = QtGui.QWidget(VREDWorkflow)
        self.centralwidget.setObjectName("centralwidget")
        self.publish_view = QtGui.QListView(self.centralwidget)
        self.publish_view.setGeometry(QtCore.QRect(10, 10, 771, 421))
        self.publish_view.setSelectionMode(QtGui.QAbstractItemView.ExtendedSelection)
        #self.publish_view.setViewMode(QtGui.QListView.ViewMode.IconMode)
        self.publish_view.setObjectName("publish_view")
        self.verticalLayoutWidget = QtGui.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 440, 771, 81))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.checkBox_layout = QtGui.QVBoxLayout(self.verticalLayoutWidget)
        self.checkBox_layout.setContentsMargins(0, 0, 0, 0)
        self.checkBox_layout.setObjectName("checkBox_layout")
        self.launch_presenter_tools = QtGui.QCheckBox(self.verticalLayoutWidget)
        self.launch_presenter_tools.setObjectName("launch_presenter_tools")
        self.checkBox_layout.addWidget(self.launch_presenter_tools)
        self.prepare_vr_setup = QtGui.QCheckBox(self.verticalLayoutWidget)
        self.prepare_vr_setup.setObjectName("prepare_vr_setup")
        self.checkBox_layout.addWidget(self.prepare_vr_setup)
        self.verticalLayoutWidget_2 = QtGui.QWidget(self.centralwidget)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(10, 530, 771, 37))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.go_layout = QtGui.QVBoxLayout(self.verticalLayoutWidget_2)
        self.go_layout.setContentsMargins(0, 0, 0, 0)
        self.go_layout.setObjectName("go_layout")
        self.go_button = QtGui.QPushButton(self.verticalLayoutWidget_2)
        self.go_button.setObjectName("go_button")
        self.go_layout.addWidget(self.go_button)
        self.verticalLayoutWidget_3 = QtGui.QWidget(self.centralwidget)
        self.verticalLayoutWidget_3.setGeometry(QtCore.QRect(10, 570, 771, 80))
        self.verticalLayoutWidget_3.setObjectName("verticalLayoutWidget_3")
        self.context_layout = QtGui.QVBoxLayout(self.verticalLayoutWidget_3)
        self.context_layout.setContentsMargins(0, 0, 0, 0)
        self.context_layout.setObjectName("context_layout")
        #VREDWorkflow.setCentralWidget(self.centralwidget)
        self.statusbar = QtGui.QStatusBar(VREDWorkflow)
        self.statusbar.setObjectName("statusbar")
        #VREDWorkflow.setStatusBar(self.statusbar)
        self.context = QtGui.QLabel(VREDWorkflow)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.context.sizePolicy().hasHeightForWidth())
        self.context.setSizePolicy(sizePolicy)
        self.context.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.context.setObjectName("context")
        self.context_layout.addWidget(self.context)

        self.retranslateUi(VREDWorkflow)
        QtCore.QMetaObject.connectSlotsByName(VREDWorkflow)

    def retranslateUi(self, VREDWorkflow):
        VREDWorkflow.setWindowTitle(QtGui.QApplication.translate("VREDWorkflow", "MainWindow", None, QtGui.QApplication.UnicodeUTF8))
        self.launch_presenter_tools.setText(QtGui.QApplication.translate("VREDWorkflow", "Launch Presenter Tools", None, QtGui.QApplication.UnicodeUTF8))
        self.prepare_vr_setup.setText(QtGui.QApplication.translate("VREDWorkflow", "Prepare VR Setup", None, QtGui.QApplication.UnicodeUTF8))
        self.go_button.setText(QtGui.QApplication.translate("VREDWorkflow", "Go!", None, QtGui.QApplication.UnicodeUTF8))

