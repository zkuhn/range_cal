import matplotlib.pyplot as plt
import numpy as np

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