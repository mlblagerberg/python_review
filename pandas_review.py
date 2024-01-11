"""
General Pandas review
January 10th, 2024
Madeleine Lagerberg
"""

import pandas as pd
from time import time

# Read csv file
df = pd.read_csv('pokemon_data.csv') # df = pd.read_csv('pokemon_data.csv')

# # Print top and bottom of dataframe
# print(df.head(5))
# print(df.tail(5))

# # Read Excel file type
# df_xlsx = pd.read_excel('pokemon_data.xlsx')
# print(df_xlsx.head(5))

# # Load tab seperated file
# df_tab = pd.read_csv('pokemon_data.txt', delimiter='\t')
# print(df_tab.head(3))

# # Read column headers
# print(df.columns)

# # Read individual column
# print(df['Name'])

# # Read multiple columns
# print(df[['Name', 'Type 2', 'Type 1']])

# # Read each row iloc stands for integer location
# print(df.iloc[1])

# # Read a specific location (R, C) iloc[row, column]
# print(df.iloc[798])

# print('Columns are also indexed on zero: ' + df.iloc[798,2])

# # Iterate through rows 
# for index, row in df.iterrows():
#     print(index, row['Name'])

# # To find specific data in our df that isn't based on rows
# print(df.loc[df['Type 1'] == "Fire"])

# Get high level statistics on data
# print(df.describe())

# ## Sorting df

# # Sort by a single value
# df_sort = df.sort_values('Name')
# print(df_sort.head(50))

# # Sort by multiple values
# print(df.sort_values(['Type 1', 'HP'], ascending=[1,0]))

### Making changes to the data

# Create a total score column (easiest way to read but not fastest)
start_time = time()
df['Total'] = df['HP'] + df['Attack'] + df['Defense'] + df['Sp. Atk'] + df['Sp. Def'] + df['Speed']
run_time = time() - start_time
print(f'Elapsed time of operation 1: {run_time} seconds')
# print(df[['Name', 'Total']])

# print(df.sort_values(['Name', 'Total'], ascending=[1,0]))

# print(df.sort_values(['Total'], ascending=False))

# df_legend = df.loc[df['Legendary'] == True]
# print(df_legend.describe())

# print(df.describe())

# Drop a column 
df = df.drop(columns=['Total'])

# Create a total score column (more succinct way)
start_time = time()
df['Total'] = df.iloc[:,4:10].sum(axis=1) # axis = 1 adds horizontally, axis = 0 adds vertically
run_time = time() - start_time
print(f'Elapsed time of operation 2: {run_time} seconds')
print(df.head(5))

# Run check to make sure the totals are accurate
print(45+49+49+65+65+45)

# Move column naive way
start_time = time()
cols = list(df.columns.values)
df2 = df[cols[0:10] + [cols[12]] + cols[10:12]] # single columns like cols[12] are type str so surround with [] to make list
run_time = time() - start_time
print(f'Elapsed time of operation 3: {run_time} seconds')
print(df2.head(5))


# Move column efficient way
start_time = time()
column_to_move = df.pop('Total')
df.insert(10, 'Total', column_to_move)
run_time = time() - start_time
print(f'Elapsed time of operation 4: {run_time} seconds')
print(df.head(5))

# Save new dataframe
df.to_csv('modified_pokemon_data.csv')


