import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv('cleaned_obesity_data.csv')
# obese_adults = data[data['Question'] == 'Percent of adults aged 18 years and older who have obesity']
# years=obese_adults['YearStart'].unique().tolist()
years = df['year'].unique().tolist()
years.sort()
print(years)
percents=[]
for year in years:
    year_df = df[df['year'] == year]
    percent_obese_list = year_df['percent_obese'].tolist()
    percent_obese=sum(percent_obese_list)/len(percent_obese_list)
    percents.append(percent_obese)

x = np.array(years)
y = np.array(percents)

slope, intercept = np.polyfit(x, y, 1)
line_of_best_fit = slope * x + intercept
equation = 'y = ' + str(round(slope, 2)) + 'x + ' + str(round(intercept, 2))

plt.scatter(years, percents,c='red')
plt.plot(x, line_of_best_fit, c='blue', label='line of best fit' + '\n' + equation)
plt.legend()
plt.xlabel('Year')
plt.ylabel('Percentage of Adults Obese')
plt.title('Percentage of Obese Adults in the US Over Time')
plt.savefig('./plots/national_obesity_in_us.png')
plt.show()
