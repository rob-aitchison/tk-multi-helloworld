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
from .ui.dialog import Ui_VREDWorkflow

# Import the shotgun_model module from the shotgun utils framework.
shotgun_model = sgtk.platform.import_framework("tk-framework-shotgunutils",
                                               "shotgun_model")
# Set up alias
ShotgunModel = shotgun_model.ShotgunModel

#from .delegate_list_item import ListItemDelegate

# standard toolkit logger
logger = sgtk.platform.get_logger(__name__)


def show_dialog(app_instance):
    """
    Shows the main dialog window.
    """
    # in order to handle UIs seamlessly, each toolkit engine has methods for launching
    # different types of windows. By using these methods, your windows will be correctly
    # decorated and handled in a consistent fashion by the system. 
    
    # we pass the dialog class to this method and leave the actual construction
    # to be carried out by toolkit.
    app_instance.engine.show_dialog("VRED Prototype", app_instance, AppDialog)
    


class AppDialog(QtGui.QWidget):
    """
    Main application dialog window
    """
    
    def __init__(self):
        """
        Constructor
        """
        # first, call the base class and let it do its thing.
        QtGui.QWidget.__init__(self)
        
        # now load in the UI that was created in the UI designer
        self.ui = Ui_VREDWorkflow() 
        self.ui.setupUi(self)
        
        # most of the useful accessors are available through the Application class instance
        # it is often handy to keep a reference to this. You can get it via the following method:
        self._app = sgtk.platform.current_bundle()
        
        # logging happens via a standard toolkit logger
        logger.info("VRED Prototype")
        
        # via the self._app handle we can for example access:
        # - The engine, via self._app.engine
        # - A Shotgun API instance, via self._app.shotgun
        # - An Sgtk API instance, via self._app.sgtk 

        # setup our data backend
        self._model = shotgun_model.SimpleShotgunModel(self)

        # tell the view to pull data from the model
        #self.ui.publish_view.setModel(self._model)

        # load all assets from Shotgun
        self._model.load_data(entity_type="PublishedFile")
        
        self._proxy_model = QtGui.QSortFilterProxyModel(self)
        #self._proxy_model.setDynamicSortFilter(True)
        self._proxy_model.setSourceModel(self._model)

        self.ui.publish_view.setModel(self._proxy_model)

        # lastly, set up our very basic UI
        self.ui.context.setText("Current Context: %s" % self._app.context)
        
        # RA 
        self.ui.go_button.clicked.connect(self.PrintSelected)


    def PrintSelected(self):
        """
        do something here
        """
        selected_publishes = self.ui.publish_view.selectedIndexes()
        what_type = type(selected_publishes)
        logger.debug("selected publishes type is %s" % what_type)
        if not selected_publishes:
            return

        # for selected_publish in selected_publishes:
        #     # selected_publish_info = self._model.itemFromIndex(
        #     #     self._proxy_model.mapToSource(selected_publish)
        #     # )
        #     what_type = type(selected_publish)
        
        #     logger.debug("selected publish type is %s" % what_type)
        
        return selected_publishes
        