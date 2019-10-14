from linear_regression import linear_fit
import matplotlib.pyplot as plt
import numpy as np

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


def main():
    """
    Run our two sample data sets to start
    """
    simple_plot()
    mock_data_plot()
    
def mock_data_plot():
    """
    Do a plot of the mock data supplied in the question
    """
    my_data = md.data()
    data_array = md.split_data(my_data)
    # print(data_array)
    m,b = linear_fit(data_array)
    plot_fit(data_array, m, b)
        

def plot_fit(points, slope, y_intercept):
    """
    Plot the points and the linear fit line.
    Label the plot so it's easy to see what data is plotted
    """

    fig, ax = plt.subplots()
    
    for x,y in points:
    
        ax.scatter(x,y)
    
    x_range = [a[0] for a in points]
    x_range.sort()
    
    t = np.arange(x_range[0], x_range[-1])    
    plt.plot(t, slope * t + y_intercept)
    
    ax.set_title("Slope = {:4.4f}".format(slope) + "  :  Y_intercept = {:4.2f}".format(y_intercept), fontsize=15)
    ax.set_xlabel("Temperature" , fontsize=15)
    ax.set_ylabel("Range", fontsize=15)
       
    plt.show( )
    

if __name__ == "__main__":
    main() 