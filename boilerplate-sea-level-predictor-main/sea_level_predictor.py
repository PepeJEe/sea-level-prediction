import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.ticker import FormatStrFormatter
import numpy as np
from scipy.stats import linregress

def draw_plot():
    # Read data from file

    # Create scatter plot


    # Create first line of best fit


    # Create second line of best fit


    # Add labels and title

    data = pd.read_csv("./boilerplate-sea-level-predictor-main/epa-sea-level.csv")

    x = data["Year"].to_numpy()
    y = data["CSIRO Adjusted Sea Level"].to_numpy()


    mask = (x >= 2000) & (x <= x.max())
    x_1 = x[mask]
    y_1 = y[mask]

        #print(data[x_1])

    years_extended = np.arange(x[0], 2051, 1)
    years_extended_2 = np.arange(x_1[0], 2051, 1)

    slope, intercept, r_value, p_value, std_err = linregress(x, y)
    line = [slope*xi + intercept for xi in years_extended]

    slope, intercept, r_value, p_value, std_err = linregress(x_1, y_1)
    line_1 = [slope*xj + intercept for xj in years_extended_2]

    plt.scatter(x, y, color = "blue", label = "Data")
    plt.plot(years_extended, line, color = "red", label = "Regression Line")
    plt.plot(years_extended_2, line_1, color = "red", label = "Regression Line 2")

    ax = plt.gca()
    ax.set_title('Rise in Sea Level')
    ax.set_xlabel('Year')
    ax.set_ylabel('Sea Level (inches)')

    ax.set_xlim(1850, 2075)
    ax.set_ylim(0, 20)
    ax.xaxis.set_major_formatter(FormatStrFormatter('%.1f'))

    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.grid()
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()
