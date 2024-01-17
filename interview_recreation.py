"""
Recreation problem in Pinterest Interview
January 16th, 2024
Madeleine Lagerberg
"""

import pandas as pd

# Create dictionary for mapping
sample_dictionary = {
    1: 'Good',
    2: 'Neutral',
    3: 'Bad'
    }

print(sample_dictionary)
print(type(sample_dictionary))

df = pd.read_csv('modified_pokemon_data.csv')

print(df.describe())

# df['total_category'] = df[df.loc[['Total'] < 330, 1]]

# for i in range(1,len(sample_dictionary)+1):
#     # print(i)
#     df.loc[df['Total']]

df.loc[df['Total'] < 330,  'total_category'] = 1
df.loc[(df['Total'] >= 330) & (df['Total'] <  450), 'total_category'] = 2
# df.loc[(df['Total'] >= 450) & (df['Total'] < 515),  'total_category'] = 3
# print(df.isna().sum())
# print(df.head())
# print(type(df['total_category']))

# Iterate over a dictionary
for i in range(1, len(sample_dictionary) + 1):
    ith_value = sample_dictionary[i]
    list_index = list(sample_dictionary.keys())
    ith_key = list_index[i-1]
    print(f'{ith_value} and {ith_key}')

# Shows that the column total category  is type float when we want it to be int
print(df.info())


# df['total_category'] = df['total_category'].astype(int) # won't work because there are nulls

# Combine look up with constructing column based on dictionary iteration
for i in range(0, len(sample_dictionary)):
    ith_value = sample_dictionary[i+1]
    # print(type(ith_value))
    list_index = list(sample_dictionary.keys())
    ith_key = float(list_index[i])
    print(type(ith_key))
    print(f'Dictionary value {ith_value} and key {ith_key}')
    df.loc[df['total_category'] == ith_key, 'total_category_name'] =  ith_value

print(df.head())

# The first part of the problem was to replace the nulls with "Unknown"

print(df.isna().sum())
df.loc[df['total_category'].isna(), 'total_category_name'] = 'Unknown'
print(df.head())

# Second part of the problem was to find the average runtime (here we will do average speed) 
# for each total_category limited to one value of another column (we will use 'Grass' from 'Type 1')
# print(df.groupby(['total_category_name']).mean())
condition = (df['Type 1'] == 'Grass')

print(condition.isna().sum())
# print(condition.head())
result = df[condition].groupby('total_category_name')['Speed'].mean()
print(result)

