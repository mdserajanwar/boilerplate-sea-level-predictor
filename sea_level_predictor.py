import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')

    # Create scatter plot 
    plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'])


    # Create first line of best fit
    years = df['Year']
    sea_level = df['CSIRO Adjusted Sea Level']

    slope, intercept, r_value, p_value, std_err = linregress(years, sea_level)

    x_pred = range(1880, 2051)
    y_pred = [slope * year + intercept for year in x_pred]

    plt.plot(x_pred, y_pred) 

    # Create second line of best fit
    recent_df = df[df['Year'] >= 2000]

    slope, intercept, r_value, p_value, std_err = linregress(
        recent_df['Year'],
        recent_df['CSIRO Adjusted Sea Level']
    )

    x_pred = range(2000, 2051)
    y_pred = [slope * year + intercept for year in x_pred]

    plt.plot(x_pred, y_pred) 

    # Add labels and title
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level') 
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()