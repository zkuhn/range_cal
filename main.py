from linear_regression import linear_fit
import matplotlib.pyplot as plt
import numpy as np
import ui
import calib_workflow_ctrlr as cw
import test_calib_workflow_ctrlr as tcw

 

import mock_data as md

def simple_plot():
    """
    Do a plot of the simple point cloud
    """
    points = [
        (1,2),
        (2,1),
        (3,2),
        (4,1),
        (5,2),
    ]
    
    m, b = linear_fit(points)
    
    print(m)
    print (b)
    
    plot_fit(points, m, b)


def mock_data_plot():
    """
    Do a plot of the mock data supplied in the question
    """
    my_data = md.data()
    data_array = md.split_data(my_data)
    # print(data_array)
    m,b = linear_fit(data_array)
    plot_fit(data_array, m, b)


def main():
    """
    Run our two sample data sets to start
    """
    # simple_plot()
    # mock_data_plot()

    fc = tcw.MockFixtureController()
    tui = ui.TextUI()
    tc = cw.CalibrationWorkflowController(fc, tui)
    tc.run()
    

if __name__ == "__main__":
    main() 