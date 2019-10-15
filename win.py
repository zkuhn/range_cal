import sys

from PySide2 import QtCore, QtGui, QtQml

from PySide2.QtCore import (
    Qt, 
    QObject, 
    Signal, 
    Slot, 
    QCoreApplication,
    Property
)

import calib_workflow_ctrlr as cwc
import fixture_controller as fixt

class WindowUI(QObject):
    
    def __init__(self, parent = None):
        QObject.__init__(self, parent)
        engine = QtQml.QQmlApplicationEngine()
        engine.rootContext().setContextProperty("ui_control", self)
        url = QtCore.QUrl.fromLocalFile('./qml/main.qml')
        engine.load(url)
        self._engine = engine
        fc = fixt.FixtureController()
        self._calib_workflow = cwc.CalibrationWorkflowController(fc, self)
        
        self._sensor_mappings = []
    
    
    @Slot(str, str, str)
    def set_fixture_mapping(self, a, b, c):
        self.log("fixture mappings set")
        
        self._sensor_mappings = []
        
        if a:
            self._sensor_mappings.append((a, 1))
            self.log("a")
        if b:
            self._sensor_mappings.append((b, 2))
            self.log("b")
        if c:
            self._sensor_mappings.append((c, 3))
            self.log("c")
        
        pass
    
    @Slot(str)
    def loader_changed(self, page):
        print(page)
        pass
    
    @Slot()
    def start_cycle(self):
        self.log("cycle start requested")
        self._calib_workflow.calibrate(self._sensor_mappings)
        self.log("cycle finished")
        
    def ask_sensor_fixture_assignment(self):
        pass
    
    def log(self, message):
        print(message)
    

if __name__ == '__main__':

    app = QtGui.QGuiApplication()
    uic = WindowUI()
    
    sys.exit(app.exec_())