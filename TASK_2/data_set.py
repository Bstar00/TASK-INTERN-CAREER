#!/usr/bin/python3

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# Read the dataset from a CSV file
df = pd.read_csv('/home/adduser/TASK-INTERN-CAREER/TASK_2/used_cars.csv')

# Clean the 'Mileage' column and convert it to numeric
mileage_column = 'Mileage'
df[mileage_column] = pd.to_numeric(df[mileage_column].str.replace(' km/kg', '').str.replace(' kmpl', ''), errors='coerce')

# Display basic information about the dataset
print("Dataset Information:")
print(df.info())

# Display summary statistics
print("\nSummary Statistics:")
print(df.describe())

# Data filtering based on specific criteria
#let's filter cars with a mileage greater than 25 kmpl
filtered_data = df[df[mileage_column] > 25]
print("\nFiltered Data:")
print(filtered_data[['Name', mileage_column]])

# Generate a histogram for Kilometers Driven
plt.figure(figsize=(10, 6))
sns.histplot(df['Kilometers_Driven'], bins=30, kde=True)
plt.title('Histogram of Kilometers Driven')
plt.xlabel('Kilometers Driven')
plt.ylabel('Frequency')
plt.show()
