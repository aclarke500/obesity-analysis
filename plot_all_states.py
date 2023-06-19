import pandas as pd
import matplotlib.pyplot as plt
from obesity_by_state import plot_by_state

df = pd.read_csv('cleaned_obesity_data.csv')
states = df['location'].unique().tolist()

results = {
    'state': [],
    'average_percent_obese': [],
    'increase_per_year': [],
    'index': []
}   

i = 0 # counter for index
for state in states:
    result=plot_by_state(state) # returns the average percent obese for a state
    results['state'].append(state)
    results['average_percent_obese'].append(result['average_percent_obese'])
    results['increase_per_year'].append(result['increase_per_year'])
    results['index'].append(i)
    if result['increase_per_year'] < 0:
        print(f'{state} has a negative increase per year.')
    i += 1

max_increase = 0
state_max_increase = ''
for i in results['index']:
    if results['increase_per_year'][i] > max_increase:
        max_increase = results['increase_per_year'][i]
        state_max_increase = results['state'][i]
print(f'The state with the highest increase in obesity per year is {state_max_increase} with an increase of {max_increase} percent per year.')

max_avg = 0
state_max_avg = ''
for i in results['index']:
    if results['average_percent_obese'][i] > max_avg:
        max_avg = results['average_percent_obese'][i]
        state_max_avg = results['state'][i]
print(f'The state with the highest average obesity rate is {state_max_avg} with an average of {max_avg} percent obese.')


min_increase = 99999999 # arbitrarily large number
state_min_increase = ''
for i in results['index']:
    if results['increase_per_year'][i] < min_increase:
        min_increase = results['increase_per_year'][i]
        state_min_increase = results['state'][i]
print(f'The state with the lowest increase in obesity per year is {state_min_increase} with an increase of {min_increase} percent per year.')

min_avg = 99999999 # arbitrarily large number
state_min_avg = ''
for i in results['index']:
    if results['average_percent_obese'][i] < min_avg:
        min_avg = results['average_percent_obese'][i]
        state_min_avg = results['state'][i]
print(f'The state with the lowest average obesity rate is {state_min_avg} with an average of {min_avg} percent obese.')

results_df = pd.DataFrame(results)
results_df.to_csv('results.csv')

