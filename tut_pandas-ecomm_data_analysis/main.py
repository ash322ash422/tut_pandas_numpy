import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Simulate customer transaction data
def generate_data():
    
    np.random.seed(42)
    
    # Simulate product data
    product_ids = [f'P{i}' for i in range(1, 21)]
    product_names = [f'Product {i}' for i in range(1, 21)]
    
    # Simulate customer demographic data
    data_size = 100
    customers = ['Customer {}'.format(i) for i in range(1, data_size+1)]
    regions = ['North', 'South', 'East', 'West']
    ages = np.random.randint(18, 65, size=data_size)
    gender = np.random.choice(['Male', 'Female'], size=data_size)
    
    # Create a DataFrame for customer demographics
    customer_df = pd.DataFrame({
        'CustomerID': customers,
        'Age': ages,
        'Gender': gender,
        'Region': np.random.choice(regions, size=100)
    })
    
    # Simulate transactions
    transactions = []
    for customer in customers:
        num_transactions = np.random.randint(1, 6)  # each customer makes 1-5 purchases
        for _ in range(num_transactions):
            product = np.random.choice(product_ids)
            price = np.random.randint(10, 500)
            transactions.append([customer, product, price])
    
    # Create a DataFrame for transactions
    transaction_df = pd.DataFrame(transactions, columns=['CustomerID', 'ProductID', 'Price'])
    
    # data.to_csv("ecomm_data.csv") # If you want to save it
    # return data.read_csv("ecomm_data.csv")

    return customer_df, transaction_df

# Data Cleaning and Merging
def clean_data(customer_df, transaction_df):
    # Remove duplicate transactions (if any)
    transaction_df.drop_duplicates(inplace=True)

    # Handle missing values: assume we want to fill missing age with the median
    customer_df['Age'].fillna(customer_df['Age'].median(), inplace=True)
    
    # Merging customer demographics with transaction data
    merged_df = pd.merge(transaction_df, customer_df, on='CustomerID', how='left')
    
    return merged_df

# Analyzing Data: Grouping by Customer and Summarizing Sales
def analyze_sales(merged_df):
    # Calculate total sales per customer
    customer_sales = merged_df.groupby('CustomerID').agg(TotalSales=('Price', 'sum'), TransactionCount=('Price', 'count')).reset_index()
    
    # Top 10 customers by total sales
    top_customers = customer_sales.sort_values(by='TotalSales', ascending=False).head(10)
    print("Top 10 customers by Total Sales:")
    print(top_customers)
    
    return top_customers

# Aggregating Data: Grouping by Region and Summarizing
def analyze_region_sales(merged_df):
    # Sales summary by region
    region_sales = merged_df.groupby('Region').agg(TotalSales=('Price', 'sum'), TransactionCount=('Price', 'count')).reset_index()
    print("\nSales by Region:")
    print(region_sales)
    
    return region_sales

# Visualizing Data: Bar chart for Total Sales by Region
def plot_sales_by_region(region_sales):
    plt.figure(figsize=(8, 6))
    sns.barplot(x='Region', y='TotalSales', data=region_sales, palette='viridis')
    plt.title('Total Sales by Region')
    plt.xlabel('Region')
    plt.ylabel('Total Sales')
    plt.tight_layout()
    plt.show()

# Visualizing Data: Age vs. Sales Scatter Plot
def plot_age_vs_sales(merged_df):
    plt.figure(figsize=(8, 6))
    sns.scatterplot(data=merged_df, x='Age', y='Price', hue='Gender', palette='coolwarm', alpha=0.7)
    plt.title('Age vs Sales')
    plt.xlabel('Age')
    plt.ylabel('Sales Amount')
    plt.tight_layout()
    plt.show()

# Visualizing Data: Gender Distribution of Customers
def plot_gender_distribution(customer_df):
    plt.figure(figsize=(8, 6))
    gender_count = customer_df['Gender'].value_counts()
    sns.barplot(x=gender_count.index, y=gender_count.values, palette='Blues')
    plt.title('Gender Distribution of Customers')
    plt.xlabel('Gender')
    plt.ylabel('Count')
    plt.tight_layout()
    plt.show()

# Main function to run the analysis and visualization
def main():
    # Generate data
    customer_df, transaction_df = generate_data()
    
    # Clean data and merge
    merged_df = clean_data(customer_df, transaction_df)
    
    # Sales analysis
    top_customers = analyze_sales(merged_df)
    
    # Regional sales analysis
    region_sales = analyze_region_sales(merged_df)
    
    # Plot results
    plot_sales_by_region(region_sales)
    plot_age_vs_sales(merged_df)
    plot_gender_distribution(customer_df)
    
if __name__ == "__main__":
    main()
