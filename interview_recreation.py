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
print(df.head())

# Iterate over a dictionary
for i in range(1, len(sample_dictionary) + 1):
    ith_value = sample_dictionary[i]
    list_index = list(sample_dictionary.keys())
    ith_key = list_index[i-1]
    print(f'{ith_value} and {ith_key}')

# Combine look up with constructing column based on dictionary iteration
for i in range(0, len(sample_dictionary)):
    ith_value = sample_dictionary[i+1]
    list_index = list(sample_dictionary.keys())
    ith_key = list_index[i]
    # print(f'{ith_value} and {ith_key}')
    df.loc[df['total_category'] == ith_value, 'total_category_name'] =  ith_key

print(df.describe())