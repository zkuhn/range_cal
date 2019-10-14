import numpy as np

def linear_fit(points):
    """
    Given a set of points, return the slope and y-intercept of a least squares fit line
    See https://docs.scipy.org/doc/numpy/reference/generated/numpy.linalg.lstsq.html
    
    :param points: a list of points
    :return m, b: where m is the slope of the fit line, and b is the y-intercept i.e. y = mx + b 
    """
    
    x = [a[0] for a in points]
    y = [a[1] for a in points]
    A = np.vstack([x, np.ones(len(x))]).T
    m, b = np.linalg.lstsq(A, y, rcond=None)[0]
    
    return m, b
    
    
    
    


