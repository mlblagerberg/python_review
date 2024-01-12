"""
This is a basic project review using pandas of the iris dataset.
The iris dataset is available via seaborn and scikit-learn modules
January 11th, 2024
Madeleine Lagerberg
"""

import pandas as pd
import seaborn as sns


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



