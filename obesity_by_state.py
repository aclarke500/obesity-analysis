import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


def plot_by_state(state):
    # import cleaned data, filter by state, get years, get average percent obese for each year, plot
    df = pd.read_csv('cleaned_obesity_data.csv')
    state_df = df[df['location'] == state]
    years = state_df['year'].unique().tolist()
    years.sort()
    percents = []
    for year in years:
        year_df = state_df[state_df['year'] == year]
        percent_obese_list = year_df['percent_obese'].tolist()
        percent_obese = sum(percent_obese_list)/len(percent_obese_list)
        percents.append(percent_obese)

    x = np.array(years)
    y = np.array(percents)

    slope, intercept = np.polyfit(x, y, 1)
    line_of_best_fit = slope * x + intercept
    equation = 'y = ' + str(round(slope, 2)) + 'x + ' + \
        str(round(intercept, 2))

    plt.scatter(years, percents, c='red')
    plt.plot(x, line_of_best_fit, c='blue',
             label='line of best fit' + '\n' + equation)
    plt.legend()
    plt.xlabel('Year')
    plt.ylabel('Percentage of Adults Obese')
    plt.title('Percentage of Obese Adults in ' + state + ' Over Time')
    plt.savefig(f'./plots/obesity_in_{state}.png')
    plt.clf()

    results = {
        'average_percent_obese': sum(percents)/len(percents),
        'state': state,
        'increase_per_year': slope
    }
    return results

