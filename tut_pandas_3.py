import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.model_selection import train_test_split

# Read data from CSV file
df = pd.read_csv('data.csv')  # Replace 'data.csv' with your actual file path
print("\nDataFrame:\n", df.head())

# One-Hot Encoding categorical variables
encoder = OneHotEncoder(sparse_output=False, drop='first')
cities_encoded = encoder.fit_transform(df[['City']])
city_columns = encoder.get_feature_names_out(['City'])
df_cities = pd.DataFrame(cities_encoded, columns=city_columns)
df = pd.concat([df, df_cities], axis=1).drop(columns=['City'])
print("\nDataFrame after one-hot encoding City column:\n", df.head())

# Feature Scaling
scaler = StandardScaler()
df[['Age', 'Salary', 'Experience']] = scaler.fit_transform(df[['Age', 'Salary', 'Experience']])
print("\nDataFrame after scaling:\n", df.head())

# Splitting Data for Training and Testing
X = df.drop(columns=['Salary'])  # Assuming salary is the target variable
y = df['Salary']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

print("\nTraining Features:\n", X_train.head())
print("\nTesting Features:\n", X_test.head())
