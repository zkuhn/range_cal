from linear_regression import linear_fit
import matplotlib.pyplot as plt
import numpy as np

def test_unit_line():
    points = [
        (1,1),
        (2,2),
        (3,3),
        (4,4),
    ]
    
    m, b = linear_fit(points)
    
    assert np.isclose(m, 1)
    assert np.isclose(b, 0)
    
    
    
    
def test_flat_line():
    points = [
        (1,2),
        (2,1),
        (3,2),
        (4,1),
        (5,2),
    ]
    
    m, b = linear_fit(points)
    
    assert np.isclose(m, 0)
    assert np.isclose(b, 1.6)
    