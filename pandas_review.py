"""
General Pandas Review
January 10th, 2024
Madeleine Lagerberg
"""

import pandas as pd
import re
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

# # Create a total score column (easiest way to read but not fastest)
# start_time = time()
# df['Total'] = df['HP'] + df['Attack'] + df['Defense'] + df['Sp. Atk'] + df['Sp. Def'] + df['Speed']
# run_time = time() - start_time
# print(f'Elapsed time of operation 1: {run_time} seconds')
# # print(df[['Name', 'Total']])

# # print(df.sort_values(['Name', 'Total'], ascending=[1,0]))

# # print(df.sort_values(['Total'], ascending=False))

# # df_legend = df.loc[df['Legendary'] == True]
# # print(df_legend.describe())

# # print(df.describe())

# # Drop a column 
# df = df.drop(columns=['Total'])

# Create a total score column (more succinct way)
# start_time = time()

df['Total'] = df.iloc[:,4:10].sum(axis=1) # axis = 1 adds horizontally, axis = 0 adds vertically

# run_time = time() - start_time
# print(f'Elapsed time of operation 2: {run_time} seconds')
# print(df.head(5))

# Run check to make sure the totals are accurate
# print(45+49+49+65+65+45)

# # Move column naive way
# start_time = time()

# cols = list(df.columns.values)
# df2 = df[cols[0:10] + [cols[12]] + cols[10:12]] # single columns like cols[12] are type str so surround with [] to make list

# run_time = time() - start_time
# print(f'Elapsed time of operation 3: {run_time} seconds')
# print(df2.head(5))


# Move column efficient way
# start_time = time()

column_to_move = df.pop('Total')
df.insert(10, 'Total', column_to_move)

# run_time = time() - start_time
# print(f'Elapsed time of operation 4: {run_time} seconds')
# print(df.head(5))

# Save new dataframe as csv or tab seperated
# df.to_csv('modified_pokemon_data.csv', index=False)

# df.to_csv('modified_pokemon_data.txt', index=False, sep='\t')

### Filtering Data
# print(df.loc[(df['Type 1'] == 'Grass') & (df['Type 2'] == 'Poison') & (df['Total'] > 300)]) # To change and to an or statment use | operator

# # Save altered dataframe 
# df_new = df.loc[(df['Type 1'] == 'Grass') & (df['Type 2'] == 'Poison') & (df['Total'] > 300)]
# print(df_new)

# # Create new index and save old as a columne
# # df_new = df_new.reset_index()
# # print(df_new)

# # Create new index and don't save old index
# df_new = df_new.reset_index(drop=True)
# print(df_new)

# # Exclude rows with/without particular word in a column
# print(df.loc[df['Name'].str.contains('Mega')].head(5))
# print(df.loc[~df['Name'].str.contains('Mega')].head(5))

# Contains function works with regex expressions and complicated filtering as well 
# print( df.loc[df['Type 1'].str.contains('fire|grass', regex=True)]) # flags field in the contains function can help you ignore case 

# print( df.loc[df['Type 1'].str.contains('fire|grass', flags=re.I, regex=True)]) # flags I for ignore

# print( df.loc[df['Name'].str.contains('ven[a - z]*', flags=re.I, regex=True)]) # a -z is any letters and * is zero or more

### Conditional Changes
# df.loc[df['Type 1'] == 'Fire', 'Type 2'] = 'Lava'
# print(df.loc[df['Type 2'] == 'Lava'].head(5)) 

# # Change multiple values given a condition
# df.loc[df['Type 2'] == 'Lava', ['Generation', 'Legendary']] = 'TEST'

# # Modify them individuall
# df.loc[df['Type 2'] == 'Lava', ['Name', 'Legendary']] = ['Test 1', 'Test 2']
# print(df.loc[df['Type 2'] == 'Lava'].head(10))


### Aggregate Statistics (Groupby)

# df = pd.read_csv('modified_pokemon_data.csv')
# print(df.head(100))
# # print(df.groupby(['Type 1']).mean())

# # print(df.groupby(['Type 1']).describe())

# # print(df.describe()) # works fine, not sure why mean() wouldn't just calculate for numeric columns automatically

# df2 = df.drop(columns = ['Name', 'Type 2'])
# print(df2)

# print(df2.groupby(['Type 1']).mean().sort_values('Speed', ascending=False))

# # Group by multiple fields
# df3 = df.drop(columns = ['Name'])
# df3_sorted = df3.groupby(['Type 1', 'Type 2']).mean().sort_values(['Type 1', 'Speed', 'Type 2'], ascending=[1,0,1])

# df3_sorted.to_csv('sorted_fastest_pokemon_types.txt', sep='\t')
# print(df3_sorted.head(20))

# # other aggregate stats: sum and count
# print(df.groupby(['Type 1']).count())


# ### Working with large amounts of data
# # use chunksize = (row count you want to consume) 
# i = 1
# for df in pd.read_csv('modified_pokemon_data.csv', chunksize=10): # df will be 10 rows of the total dataset
#     print(f'Chunk  {i}')
#     print(df)
#     i += 1

# # run operation over chunks and concatenate to new df
# new_df = pd.DataFrame(columns=df.columns)

# for df in pd.read_csv('modified_pokemon_data.csv', chunksize=100):
#     results = df.groupby(['Type 1']).count()

#     new_df = pd.concat([new_df, results])

# print(new_df.sum())

# print(new_df.columns)
# print(new_df.head(20))

# final_df = new_df.groupby(new_df.index).sum()
# print(final_df)


### Handling nulls or missing values
df = pd.read_csv('modified_pokemon_data.csv')

# Count missing values in dataframe
missing_values = df.isna().sum()
print(f'Total missing values in pokemon data is: {missing_values}')

# Let's look at the rows with missing values in them
print(df[df.isna().any(axis=1)])


# df['Type 2'].isna() == df['Type 1']
# print(df[df.isna().any(axis=1)])

# Replae the null values with Type 1 for that pokemon
df.loc[df['Type 2'].isna(), 'Type 2'] = df['Type 1']
print(df[df.isna().any(axis=1)])

# Recheck to see if there are any missing values
missing_values = df.isna().sum()
print(f'Total missing values in pokemon data is: {missing_values}')

# Check that replacement of Type 2 nulls with Type 1 was accurate
print(df.loc[df['Type 2'] == df['Type 1']])

