from collections import namedtuple

SensorMapping = namedtuple('SensorMapping', 'sensor_id fixture_id')
Calibration = namedtuple('Calibration', 'sensor_id fixture_id points slope y_intercept')
SensorReading = namedtuple('SensorReading', 'sensor_id fixture_id range')