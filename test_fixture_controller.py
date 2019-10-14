import fixture_controller as fc
import pytest 
from attr.validators import instance_of

def test_run():
    ctrl = fc.FixtureController()
    mappings = [
        (555, 1),
        (1234, 2),
    ]
    data = ctrl.run(mappings)
    
    assert data is not None


def test_run():
    ctrl = fc.FixtureController()
    mappings = [
        (555, 1),
        (1234, 2),
    ]
    data = ctrl.run(mappings)
    
    assert data is not None
    assert len(data) == 168
    

def test_run_temp():
    ctrl = fc.FixtureController(85)
    mappings = [
        (555, 1),
        (1234, 2),
    ]
    data = ctrl.run(mappings)
    
    assert data is not None
    assert len(data) == 160
    
def test_run_data():
    ctrl = fc.FixtureController(85)
    mappings = [
        (555, 1),
    ]
    data = ctrl.run(mappings)
    
    assert data is not None
    assert len(data) == 160
    time, temperature, readings= data[0]
    assert isinstance(time , str)
    assert isinstance(temperature , float)
    assert isinstance(readings, list)
    

def test_multi_fixtures():
    ctrl = fc.FixtureController(85)
    mappings = [
        (555, 1),
        (1234, 2),
        (1735, 3),
    ]
    data = ctrl.run(mappings)
    
    assert data is not None
    assert len(data) == 160
    
    
def test_mappings_needed():
    ctrl = fc.FixtureController(85)
    mappings = []
    with pytest.raises(RuntimeError) as excinfo:
        data = ctrl.run(mappings)
    
    assert "sensor mappings needed to gather calibration data" in str(excinfo.value)
    
    

