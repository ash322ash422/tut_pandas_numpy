import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Read from CSV
df = pd.read_csv("data.csv")
print(df.shape)
print("\nDataFrame1:\n", df)

# change values
df.loc[1, 'Salary'] = 30  # Set a value in Salary
df.loc[2, 'City'] = "delhi"  # Set a value in City
print("\nDataFrame2:\n", df)


# Applying .map() to increase salary by 10%
df['Salary_increase'] = df['Salary'].map(lambda x: x * 1.1)
print("\nAfter salary increase:\n",df)

# Lets drop the above 'Salary_increase' column
df.drop(columns=['Salary_increase'], inplace=True)
print("\nAfter dropping a column:\n",df)


# Handling Missing Values
print("\nMissing Values:\n", df.isnull().sum())


df_filled = df.fillna({'Salary': df['Salary'].median(), 'City': 'Unknown'})
print("\nDataFrame after filling missing values:\n", df_filled)

# Finding and Handling Duplicate Records
duplicates = df.duplicated()
print("\nDuplicate Records:\n", df[duplicates])


# Removing duplicates
df = df.drop_duplicates()
print("\nDataFrame after removing duplicates:\n", df)

#Save the clean data to CSV file
df.to_csv("data_clean.csv")


from sklearn.preprocessing import StandardScaler, LabelEncoder

# Encoding categorical variables
label_encoder = LabelEncoder()
df['City_encoded'] = label_encoder.fit_transform(df['City'])
print("\nDataFrame after encoding City column:\n", df)

# Feature Scaling
scaler = StandardScaler()
df[['Age', 'Salary', 'Experience']] = scaler.fit_transform(df[['Age', 'Salary', 'Experience']])
print("\nDataFrame after scaling:\n", df)

# Splitting Data for Training and Testing
from sklearn.model_selection import train_test_split
X = df[['Age', 'Experience', 'City_encoded']]
y = df['Salary']  # Assuming salary is the target variable
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

print("\nTraining Features:\n", X_train)
print("\nTesting Features:\n", X_test)
