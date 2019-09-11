# Copyright (c) 2013 Shotgun Software Inc.
# 
# CONFIDENTIAL AND PROPRIETARY
# 
# This work is provided "AS IS" and subject to the Shotgun Pipeline Toolkit 
# Source Code License included in this distribution package. See LICENSE.
# By accessing, using, copying or modifying this work you indicate your 
# agreement to the Shotgun Pipeline Toolkit Source Code License. All rights 
# not expressly granted therein are reserved by Shotgun Software Inc.

import sgtk
import os
import sys
import threading

# by importing QT from sgtk rather than directly, we ensure that
# the code will be compatible with both PySide and PyQt.
from sgtk.platform.qt import QtCore, QtGui
# from .ui.dialog import Ui_Dialog

# Import the shotgun_model module from the shotgun utils framework.
shotgun_model = sgtk.platform.import_framework("tk-framework-shotgunutils",
                                               "shotgun_model")
# Set up alias
ShotgunModel = shotgun_model.ShotgunModel

from .delegate_list_item import ListItemDelegate

import logging

logger = sgtk.platform.get_logger(__name__)

# import the spinner_widget module from the qtwidgets framework
spinner_widget = sgtk.platform.import_framework("tk-framework-qtwidgets", "spinner_widget")

def show_dialog(app_instance):
    """
    Shows the main dialog window.
    """
    # in order to handle UIs seamlessly, each toolkit engine has methods for launching
    # different types of windows. By using these methods, your windows will be correctly
    # decorated and handled in a consistent fashion by the system.

    # we pass the dialog class to this method and leave the actual construction
    # to be carried out by toolkit.
    app_instance.engine.show_dialog("VRED Workflow Prototypes", app_instance, VREDWorkflowPrototypes)

class VREDWorkflowPrototypes(QtGui.QWidget):
    """
    Main application dialog window
    """
    @property
    def hide_tk_title_bar(self):
        return True

    selected_publish_request_list = dict()
    
    def __init__(self, parent=None):
        """
        Constructor
        """
        super(VREDWorkflowPrototypes, self).__init__(parent)

        # see if we can determine the current project. if we can, only show the
        # episodes for this project.
        self._app = sgtk.platform.current_bundle()
        if self._app.context.project:
            filters = ["project", "is", self._app.context.project]
        else:
            filters = []

        # construct the view and set the model
        self._entity_view = QtGui.QTreeView()
        self._entity_view.setIndentation(16)
        self._entity_view.setUniformRowHeights(True)
        self._entity_view.setSortingEnabled(True)
        self._entity_view.sortByColumn(0, QtCore.Qt.AscendingOrder)

        # construct an entity model then load some data.
        self._entity_model = shotgun_model.ShotgunEntityModel(
            "PublishedFile",  # entity type
            [["project", "is", self._app.context.project], ["sg_status_list", "is", "wtg"]],  # filters
            ["project.Project.name", "code"],  # hierarchy
            ["description", "id", "project", "thumbnail"],  # fields
            self,
        )

        # UI nicety
        self._entity_model.setHeaderData(0, QtCore.Qt.Horizontal, 'Published Files')

        # refresh the data to ensure it is up-to-date
        self._entity_model.async_refresh()

        # create a proxy model to sort the model
        self._entity_proxy_model = QtGui.QSortFilterProxyModel(self)
        self._entity_proxy_model.setDynamicSortFilter(True)

        # set the proxy model's source to the entity model
        self._entity_proxy_model.setSourceModel(self._entity_model)

        # set the proxy model as the data source for the view
        self._entity_view.setModel(self._entity_proxy_model)

        # set the clicked.connected slot
        QtCore.QObject.connect(self._entity_view.selectionModel(),
                               QtCore.SIGNAL('selectionChanged(QItemSelection, QItemSelection)'), self.update_prl)

        info_lbl = QtGui.QLabel(
            "VRED Workflow Prototypes"
        )

        refresh_button = QtGui.QPushButton('Refresh List(s)')
        refresh_button.clicked.connect(self.refresh_prl)

        action_button = QtGui.QPushButton('Run Prototype - Go!')
        action_button.clicked.connect(self.RunPrototypes)

        layout = QtGui.QVBoxLayout(self)
        layout.addWidget(info_lbl)
        layout.addWidget(self._entity_view)
        layout.addWidget(refresh_button)
        layout.addWidget(action_button)

        # RA additions 20170808
        self.spinner = spinner_widget.SpinnerWidget()
        self.spinner.hide()
        self.spinner.setFixedSize(QtCore.QSize(100, 100))
        spinner_layout = QtGui.QHBoxLayout()
        spinner_layout.addStretch()
        spinner_layout.addWidget(self.spinner)
        spinner_layout.addStretch()
        layout.addLayout(spinner_layout)

        # RA addition 20170807
        logging_widget = QtGui.QSplitter()
        log_handler = QPlainTextEditLogger(logging_widget)
        logger.addHandler(log_handler)
        layout.addWidget(logging_widget)

        logger.info('tk-multi-helloworld running')

    def update_prl(self, selected, deselected):

        indexes = selected.indexes()
        if not indexes:
            return

        self.selected_publish_request_list = self._entity_model.itemFromIndex(
            self._entity_proxy_model.mapToSource(indexes[0]))

        return self.selected_publish_request_list

    def refresh_prl(self):

        self._entity_model.async_refresh()
        logger.info('Refreshed Publish Request List(s)')

    def destroy(self):
        """
        Destroy the model as required by the API.
        """
        try:
            self._entity_model.destroy()
        except Exception, e:
            # log exception
            pass
    
    def RunPrototypes(self):
        pass

class QPlainTextEditLogger(logging.Handler):
    def __init__(self, parent):
        super(QPlainTextEditLogger, self).__init__()

        self.widget = QtGui.QPlainTextEdit(parent)
        self.widget.setReadOnly(True)

    def emit(self, record):
        msg = self.format(record)
        self.widget.appendPlainText(msg)

    def write(self, m):
        pass