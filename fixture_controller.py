from collections import namedtuple
import time

import mock_data

from data_types import Calibration, SensorMapping, SensorReading

class FixtureController(object):
    
    def __init__(self, final_temp=89):
        self._final_temp = final_temp
        self._sleep_interval = .01
        self._temp_step = .499
    
    def run(self, sensor_mappings):
        
        fixture = MockFixture() # This would be replaced with the real fixture
        
        if not len(sensor_mappings):
            raise RuntimeError("sensor mappings needed to gather calibration data")
        
        done = False
        
        last_temperature = 0
        readings = []
        
                
        #control algorithm to gather sensor data
        while not done:
            # get the temp
            # if the temp is at a measure target, save a measurement for all targets
            # if we've completed all measurements, finish
            recording_time, temperature,  sensor_ranges = fixture.read(sensor_mappings)
            data = (recording_time, temperature, sensor_ranges)
            # self.log(data)
            
            if temperature - last_temperature > self._temp_step:
                readings.append(data)
                last_temperature = temperature
            
            if last_temperature > self._final_temp :
                done = True
            
            # Appendix B says we get data every 100 ms.
            time.sleep(self._sleep_interval )    
        
        return readings
    
    def log(self, message):
        # print(message)
        pass

    
    
class MockFixture(object):
    
    def __init__(self):
        data = mock_data.data()
        self._data_array = mock_data.split_data(data)
        self._generator = (row for row in self._data_array )
        self._index = 0
        
    def read(self, sensor_mappings):
        data = next(self._generator)
        data_points = []
        # return temperature + fixture 1 range reading
        for sensor in sensor_mappings:
            data_points.append(SensorReading(sensor[0], sensor[1], data[1]))
         
        return  time.ctime(), data[0], data_points 
        
        