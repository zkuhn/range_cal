
from collections import namedtuple
import time

from calib_workflow_ctrlr import CalibrationWorkflowController
import fixture_controller
from data_types import SensorReading
  
def test_run():
    fc = MockFixtureController()
    ui = MockUI()
    tc = CalibrationWorkflowController(fc, ui)
    tc.run()
    
    assert ui.asfa_called()

def test_full_data_run():
    
    fc = fixture_controller.FixtureController()
    ui = MockUI()
    tc = CalibrationWorkflowController(fc, ui)
    tc.run()
    
def test_calib_data():
    
    data = fixture_data()
    fc = MockFixtureController()
    ui = MockUI()
    tc = CalibrationWorkflowController(fc, ui)
    sensor_mappings = [(555, 1)]
    tc.get_calibration_data(fixture_data() , sensor_mappings)
    
    
def fixture_data():
    return [
            (
                time.ctime(), #time of reading
                26, # temperature recorded at that time
                    #list of sensor/fixture ranges
                 [
                     SensorReading(555, 1,  46.0),
                 ]
            ),
            (
                time.ctime(), #time of reading
                27, # temperature recorded at that time
                    #list of sensor/fixture ranges
                 [
                     SensorReading(555, 1,  48.0),
                 ]
            ),
            (
                time.ctime(), #time of reading
                28, # temperature recorded at that time
                    #list of sensor/fixture ranges
                 [
                     SensorReading(555, 1,  49.0),
                 ]
            ),
            
        ]
    
    
class MockUI(object):
    
    def __init__(self):
        self._asfa_called = False
    
    def ask_sensor_fixture_assignment(self):
        self._asfa_called = True
        return (11234, 1)
        
    def ask_done(self):
        return True
    
    def asfa_called(self):
        return self._asfa_called  


class MockFixtureController(object):
    def run(self, sensor_mappings):
        
        print("Running mock sensor controller")
        print(sensor_mappings)
        return  [
            (
                time.ctime(), #time of reading
                26, # temperature recorded at that time
                    #list of sensor/fixture ranges
                 [
                     SensorReading(sensor_mappings[0][0], sensor_mappings[0][1],  46.0),
                 ]
            ),
            (
                time.ctime(), #time of reading
                27, # temperature recorded at that time
                    #list of sensor/fixture ranges
                 [
                     SensorReading(sensor_mappings[0][0], sensor_mappings[0][1],  48.0),
                 ]
            ),
            (
                time.ctime(), #time of reading
                28, # temperature recorded at that time
                    #list of sensor/fixture ranges
                 [
                     SensorReading(sensor_mappings[0][0], sensor_mappings[0][1],  49.0),
                 ]
            ),
            
        ]