import numpy as np
import matplotlib.pyplot as plt

# 1. Generate a simulated population dataset (ages and incomes)
def generate_population_data(num_people=1000):
    # Simulate ages between 18 and 100
    ages = np.random.randint(18, 100, size=num_people)
    
    # Simulate income with a normal distribution, mean income of $50,000 and SD of $20,000
    income = np.random.normal(50000, 20000, size=num_people)
    income = np.clip(income, 10000, 120000)  # Income should be between $10,000 and $120,000
    
    return ages, income

# 2. Statistical Analysis
def statistical_analysis(ages, income):
    print("Mean Age:", np.mean(ages))
    print("Mean Income:", np.mean(income))
    print("Standard Deviation of Age:", np.std(ages))
    print("Standard Deviation of Income:", np.std(income))
    
    # Correlation between age and income
    correlation = np.corrcoef(ages, income)[0, 1]
    print("Correlation between Age and Income:", correlation)
    
# 3. Basic Mathematical Operations
def basic_operations(ages, income):
    # Element-wise operations
    income_doubled = income * 2
    age_plus_10 = ages + 10
    
    return income_doubled, age_plus_10

# 4. Linear Algebra: Matrix Operations
def matrix_operations(): # presently just do multiplication
    # Example matrices (2x2 and 2x2 matrix)
    A = np.array([[1, 2], [3, 4]])
    B = np.array([[5, 6], [7, 8]])
    
    # Matrix multiplication
    C = np.dot(A, B)
    
    print("\nMatrix A:")
    print(A)
    print("\nMatrix B:")
    print(B)
    print("\nMatrix multiplication (A dot B):")
    print(C)
    
# 5. Random Data Generation and Manipulation
def analyze_random_data():
    # Create random dataset with 1000 values
    data = np.random.randn(1000)
    
    # Find mean, std, min, and max
    mean = np.mean(data)
    std = np.std(data)
    min_val = np.min(data)
    max_val = np.max(data)
    
    print("\nRandom Data Analysis:")
    print(f"Mean: {mean}, Std Dev: {std}, Min: {min_val}, Max: {max_val}")
    
# 6. Data Visualization
def plot_data(ages, income, income_doubled, age_plus_10):
    # Scatter plot of age vs income
    plt.figure(figsize=(10, 6))
    plt.scatter(ages, income, color='blue', alpha=0.5)
    plt.title('Age vs Income')
    plt.xlabel('Age')
    plt.ylabel('Income')
    plt.show()
    
    # Histogram of ages and incomes
    plt.figure(figsize=(10, 6))
    plt.hist(ages, bins=30, alpha=0.5, label='Age', color='purple')
    plt.hist(income, bins=30, alpha=0.5, label='Income', color='green')
    plt.title('Distribution of Ages and Incomes')
    plt.xlabel('Value')
    plt.ylabel('Frequency')
    plt.legend()
    plt.show()

    # Line plot for doubled income and age+10
    plt.figure(figsize=(10, 6))
    plt.plot(income, label='Income')
    plt.plot(income_doubled, label='Doubled Income', linestyle='--')
    plt.plot(age_plus_10, label='Age + 10', linestyle=':')
    plt.title('Income and Age Manipulations')
    plt.xlabel('Person Index')
    plt.ylabel('Value')
    plt.legend()
    plt.show()

# 7. Putting it all together
def main():
    # 1. Generate simulated population data
    ages, income = generate_population_data()
    
    # 2. Perform statistical analysis
    statistical_analysis(ages, income)
    
    # 3. Perform basic mathematical operations
    income_doubled, age_plus_10 = basic_operations(ages, income)
    
    # 4. Perform matrix operations (linear algebra)
    matrix_operations()
    
    # 5. Generate random data and analyze it
    analyze_random_data()
    
    # 6. Visualize the data
    plot_data(ages, income, income_doubled, age_plus_10)
    
if __name__ == "__main__":
    main()
