import pandas as pd
# original name : Nutrition__Physical_Activity__and_Obesity_-_Behavioral_Risk_Factor_Surveillance_System.
df = pd.read_csv('data.csv')
print(df.head(5)) # print first 5 rows of the dataframe
# now we want to see all the questions asked in the survey
# grab all unique values from the column 'Question'
all_questions = df['Question'].unique().tolist() 
# create a new dataframe with the questions
questions_df = pd.DataFrame(all_questions, columns=['Question']) 
# save the questions to a csv file
questions_df.to_csv('all_questions.csv', index=False) 