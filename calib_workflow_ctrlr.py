
from typing import List
from calib_plot import plot_fit 
from linear_regression import linear_fit
from persist import CalibrationMapper

from data_types import Calibration, SensorMapping, SensorReading

class CalibrationWorkflowController(object):
    """
    """

    def __init__(self, fixture_controller, ui):
        """
        """
        self._fixture_controller = fixture_controller
        self._ui = ui
        self._mapper = CalibrationMapper()
    
    def run(self):
        
        # Identify operator
        operator_id = self.get_operator()
        
        # Load sensors into fixtures
        sensor_mappings = self.get_sensor_mappings()
        
        # save fixture assignments
        self.save_sensor_mappings(operator_id, sensor_mappings)
        
        # ask user to proceed
        
        # run calibration cycle
        sensor_data = self._fixture_controller.run(sensor_mappings)
        
        
        calib_data = self.get_calibration_data(sensor_data, sensor_mappings)
        
        # calculate calibration
        sensor_calibrations = self.calc_calibrations(calib_data)
        
        # save data
        self.save_calibration_data(sensor_calibrations)
        
        # verify tolerance
        sensor_tolerances = self.check_tolerances(sensor_calibrations)
        
        # notify operator pass/fail 
        self.notify_operator_tolerances(sensor_tolerances)
        
        
    def get_operator(self) -> int:
        return 1
    
    def get_sensor_mappings(self)-> List[SensorMapping]:
        """
        Prompt the operator for a sensor id/serial number and the fixture id it is placed in
        This way when a fixture is giving back data, we know which sensor it is for
        """    
        done = False
        sensor_mappings = []
        while not done:
        
            #ask for sensor id
            sensor_id, fixture_id = self._ui.ask_sensor_fixture_assignment()
            
            if not self.check_data_input(sensor_id, fixture_id, sensor_mappings):
                self._ui.fail_input_message()
                continue
            
            sensor_mappings.append((sensor_id, fixture_id))
            #ask done /more
            done = self._ui.ask_done()
        
        return sensor_mappings
    
    def check_data_input(self, sensor_id, fixture_id, sensor_mappings):
        """
        User input checks. confirm unique fixture and sensor id /serial num
        """
        for mapping in sensor_mappings:
            if mapping[0] == sensor_id or mapping[1] == fixture_id:
                return False
        return True
            
    def save_sensor_mappings(self, operator_id, sensor_mappings):
        return True
    
    def save_calibration_data(self, calib_data):
        self.log("saving sensor data")
        self.log(calib_data)
        for sensor_calib in calib_data:
            self._mapper.persist_calibration(sensor_calib)
            
    
    def get_calibration_data(self, sensor_data, sensor_mappings):
        """
        need to convert from time, temperature, list of sensor readings
        to sensorID, list of (temperature, range) pairs
        """
        sensor_dict = {}
        for mapping in sensor_mappings:
            sensor_dict[mapping[0]] = []    
        
        for time, temperature, sensor_readings in sensor_data:
            
            for reading in sensor_readings:
            # a reading is a time, temperature, list
                sensor_dict[reading.sensor_id].append((temperature, reading.range))
        
        # turn the map into alist of tuples
        return_data = []
        for k, v in sensor_dict.items():
            return_data.append((k, v))
            
        return return_data
        
    
    def calc_calibrations(self, sensor_data):
        self.log("calculating sensor calibrations")
        self.log(sensor_data)
        calibrations = []
        for sensor_id, readings in sensor_data:
            m, b = linear_fit(readings)
            calibrations.append(Calibration(sensor_id, 1, readings, m, b))

        self.log(calibrations)
                    
        return calibrations
    
    def check_tolerances(self, sensor_calibrations):
        self.log("checking tolerances")
        for calib in sensor_calibrations:
            self.log(calib)
            plot_fit(calib.points, calib.slope, calib.y_intercept)
        return []
    
    def notify_operator_tolerances(self, sensor_tolerances):        
        return True

    def log(self, message):
        # print(message)
        pass
