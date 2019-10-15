import os
import yaml
from data_types import Calibration
from test.test_email import test_message

class CalibrationMapper(object):
    def __init__(self):
        """
        """
        self._sensor_data_path = "./sensor_data"
        self._calib_filename = "sensorParameter.yaml"
        self._data_filename  = "sensorData.yaml"
    
    def persist_calibration(self, calibration: Calibration):
        """
        api to use formal Calibration type
        """
        self.persist(str(calibration.sensor_id), calibration.slope, calibration.y_intercept, calibration.points)
    
    def persist(self, sensor_id, slope, y_intercept, data):
        """
        Simple data api for ease of testing
        """
        path = self.make_sensor_dir(sensor_id)
        self.save_calibration(path, slope, y_intercept)
        self.save_sensor_data(path, data)
            
    def path_for_sensor_id(self, sensor_id):
        """
        Used for both reading and writing
        """
        return os.path.join(self._sensor_data_path, sensor_id)
        
    def make_sensor_dir(self, sensor_id):
        """
        If it already exists just return the path. In the future, may want to back up 
        a dir we would be overwriting
        
        """
        path = self.path_for_sensor_id(sensor_id)
        try:
            os.mkdir(path)
        except FileExistsError:
            pass
        
        return path
    
    def save_calibration(self, path, slope, y_intercept):
        """
        From the spec: \
        Record the coefficients that define the line into ~/sensorParameter.yaml:
        
        # calib_meas = A * measurement + B
        A: 0.25
        B: 5.1
        """
        with open(os.path.join(path , self._calib_filename ), "w") as w_file:
            w_file.write("# calib_meas = A * measurement + B \n")
            w_file.write("A: {} \n".format(slope))
            w_file.write("B: {} \n".format(y_intercept))
            
    def save_sensor_data(self, path, data):
        """
        Save the raw data for a calibration
        """ 
        with open(os.path.join(path , self._data_filename), "w") as d_file:
            self.log("saving data")
            for data_elem in data:
                self.log(data_elem)
                d_file.write(str(data_elem[0]) + ", " + str(data_elem[1]) + "\n" )

                
    def load_calibration(self, sensor_id):
        """
        Load a calibration file. Throw exception if there is a problem parsing
        """
        path = path = self.path_for_sensor_id(sensor_id)
        
        with open(os.path.join(path , self._calib_filename), 'r') as stream:
            # This can throw.. let it bubble out so the app can deal with file load failure
            data = yaml.safe_load(stream)
            
        return data
    
    def log(self, message):
        # print(message)
        pass
            
        
