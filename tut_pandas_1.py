import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns



# Create a sample dataset
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eva', 'Frank', 'Grace', 'Helen'],
    'Age': [25, 30, 35, 40, 22, 28, 32, 26],
    'City': ['New York', 'Los Angeles', 'Chicago', 'Houston', 'Phoenix', 'Philadelphia', 'San Antonio', 'San Diego'],
    'Salary': [70000, 80000, 65000, 90000, 48000, 72000, 85000, 62000],
    'Experience': [2, 5, 7, 10, 1, 3, 6, 2]
}

# Create a DataFrame
df = pd.DataFrame(data)
print("\nDataFrame:\n", df)

# Basic Operations
print("\nDataFrame Info:")
df.info()
print("\nSummary Statistics:\n", df.describe())

# Visualization
plt.figure(figsize=(10, 5))
sns.histplot(df['Age'], bins=5, kde=True, color='skyblue')
plt.title("Age Distribution")
plt.xlabel("Age")
plt.ylabel("Count")
plt.show()

# Filtering Data
high_salary = df[df['Salary'] > 70000]
print("\nEmployees with Salary > 70k:\n", high_salary)

# Finding a Specific Record
record = df[df['Name'] == 'Alice']
print("\nRecord for Alice:\n", record)

# Grouping Data
avg_salary_per_experience = df.groupby('Experience')['Salary'].mean()
print("\nAverage Salary by Experience:\n", avg_salary_per_experience)

# Bar Plot for Salary vs Experience
plt.figure(figsize=(8, 5))
sns.barplot(x=avg_salary_per_experience.index, y=avg_salary_per_experience.values, palette='viridis')
plt.title("Average Salary by Experience")
plt.xlabel("Years of Experience")
plt.ylabel("Average Salary")
plt.show()

# Adding a New Column
df['Tax'] = df['Salary'] * 0.2  # Assuming 20% tax
print("\nDataFrame after adding Tax column:\n", df)

# Scatter Plot for Salary vs Age
plt.figure(figsize=(8, 5))
sns.scatterplot(x=df['Age'], y=df['Salary'], hue=df['Experience'], palette='coolwarm', size=df['Experience'], sizes=(20, 200))
plt.title("Salary vs Age with Experience Levels")
plt.xlabel("Age")
plt.ylabel("Salary")
plt.legend(title="Experience (years)")
plt.show()
