# 1. Import necessary libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 2. Load the dataset
file_path = "/Users/pastorbobby/Documents/Mall_Customers.csv"
data = pd.read_csv(file_path)

# 3. Age Distribution Histogram with KDE
plt.figure(figsize=(10, 6))
sns.histplot(data['Age'], bins=20, kde=True, color='royalblue', edgecolor='black')
plt.title('Age Distribution of Customers', fontsize=14, fontweight='bold')
plt.xlabel('Age', fontsize=12)
plt.ylabel('Number of Customers', fontsize=12)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.savefig("/Users/pastorbobby/Documents/Age_Distribution.png")  # Save image
plt.show()

# 4. Annual Income Distribution
plt.figure(figsize=(10, 6))
sns.histplot(data['Annual Income (k$)'], bins=20, kde=True, color='seagreen', edgecolor='black')
plt.title('Annual Income Distribution of Customers', fontsize=14, fontweight='bold')
plt.xlabel('Annual Income (in $1000s)', fontsize=12)
plt.ylabel('Number of Customers', fontsize=12)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.savefig("/Users/pastorbobby/Documents/Annual_Income_Distribution.png")
plt.show()

# 5. Spending Score Distribution
plt.figure(figsize=(10, 6))
sns.histplot(data['Spending Score (1-100)'], bins=20, kde=True, color='crimson', edgecolor='black')
plt.title('Spending Score Distribution of Customers', fontsize=14, fontweight='bold')
plt.xlabel('Spending Score', fontsize=12)
plt.ylabel('Number of Customers', fontsize=12)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.savefig("/Users/pastorbobby/Documents/Spending_Score_Distribution.png")
plt.show()

# 6. Pairplot for Age, Income, and Spending Score
sns.pairplot(data[['Age', 'Annual Income (k$)', 'Spending Score (1-100)']], diag_kind='kde', corner=True)
plt.savefig("/Users/pastorbobby/Documents/Pairplot_Customer_Data.png")
plt.show()