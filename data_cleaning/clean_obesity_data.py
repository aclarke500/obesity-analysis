import pandas as pd

data = pd.read_csv('data.csv')
obese_adults = data[data['Question'] == 'Percent of adults aged 18 years and older who have obesity']
# obese_adults.to_csv('obese_adults.csv', index=False)
years=obese_adults['YearStart'].unique().tolist()
# print(years)
cleaned_df = {
    'year': [],
    'location': [],
    'percent_obese': []
}

# check if number
def is_number(s):
    return (isinstance(s, int) or isinstance(s, float)) and len(str(s)) > 0

# we want question = adults age 18 obese, location != national, year start, location, data value 
for index, row in obese_adults.iterrows():
    # if is_number(row['Data_Value']) and row['LocationDesc'] != 'National':
    if row['Data_Value_Footnote_Symbol'] != '~' and row['LocationDesc'] != 'National':
        cleaned_df['year'].append(row['YearStart'])
        cleaned_df['location'].append(row['LocationDesc'])
        cleaned_df['percent_obese'].append(row['Data_Value'])

cleaned_df = pd.DataFrame(cleaned_df)
cleaned_df.to_csv('../cleaned_obesity_data.csv', index=False)

