"""
This is a basic project review using pandas of the iris dataset.
The iris dataset is available via seaborn and scikit-learn modules
January 11th, 2024
Madeleine Lagerberg
"""

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


# Check what datasets come with seaborn library
dataset_names = sns.get_dataset_names()
print(dataset_names)

# Lets use the iris dataset
iris = sns.load_dataset('iris')

### Basic Data Exploration
# Check format of dataset we just imported
# print(type(iris))

# Look at the first five rows
# print(iris.head(5))

# Get basic summary statistics
# print(iris.describe())

# Find unique species in dataset
print(iris.groupby(['species']).count())
print(iris['species'].value_counts())

### Data Cleaning
missing_values = iris.isna().sum()
print(missing_values)

### Analysis and Visualization
# print(iris.head(10))

# Calculate average sepal length and width for each species
print(iris[['species', 'sepal_length', 'sepal_width']].groupby(['species']).mean())

# # Plot histogram of petal lengths
# sns.histplot( data = iris, x = 'petal_length')
# plt.show()

# # Plot petal length by species
# sns.histplot( data = iris, x = 'species', y = 'petal_length')
# plt.show()

# # Plot sepal length by width colored by species
# sns.scatterplot( data = iris, x = 'sepal_length', y = 'sepal_width', hue = 'species')
# plt.show()

### Basic Data Manipulation
# Create a new column group petal length in short, medium, and long
# Let's first look at the distribution of petal length and determine our category cutoffs
# print(iris.describe()) # 25% < 1.6, 50% < 4.35 and 75% < 5.10

# Create new column based on percentiles
iris.loc[iris['petal_length'] < 1.6, 'petal_length_group'] = 'short'
iris.loc[(iris['petal_length'] >= 1.6) & (iris['petal_length'] < 4.35), 'petal_length_group'] = 'medium'
iris.loc[iris['petal_length'] >= 4.35, 'petal_length_group'] = 'long'

print(iris.head(100))
    
# Make sure all petal_lengths received a label
print(iris.isna().sum())

# Look at the rows where the sepal length is greater than the average sepal length
mean_sepal_length = iris['sepal_length'].mean()
print(f'The average sepal length is {mean_sepal_length}')
    
print(iris.loc[iris['sepal_length'] > iris['sepal_length'].mean()])



