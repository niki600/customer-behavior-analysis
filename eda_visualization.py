import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
df = pd.read_csv("ecommerce_customer_data_custom_ratios.csv")

# Convert 'Purchase Date' to datetime
df['Purchase Date'] = pd.to_datetime(df['Purchase Date'])

# Drop unnecessary columns
df.drop(columns=['Customer Age', 'Customer Name'], inplace=True)

# Fill missing values in 'Returns'
df['Returns'].fillna(0, inplace=True)

# ------------------- EDA Visualizations -------------------

sns.set(style="whitegrid")

# Gender Distribution
plt.figure(figsize=(6, 4))
sns.countplot(data=df, x='Gender', palette='pastel')
plt.title('Gender Distribution')
plt.savefig("gender_distribution.png")
plt.show()

# Churn Distribution
plt.figure(figsize=(6, 4))
sns.countplot(data=df, x='Churn', palette='Set2')
plt.title('Churn Distribution (0 = Active, 1 = Churned)')
plt.savefig("churn_distribution.png")
plt.show()

# Payment Method Preferences
plt.figure(figsize=(8, 4))
sns.countplot(data=df, x='Payment Method', palette='muted')
plt.title('Payment Method Preferences')
plt.xticks(rotation=45)
plt.savefig("payment_method.png")
plt.show()

# Product Categories
plt.figure(figsize=(10, 5))
sns.countplot(data=df, x='Product Category', order=df['Product Category'].value_counts().index, palette='coolwarm')
plt.title('Top Product Categories')
plt.xticks(rotation=45)
plt.savefig("product_categories.png")
plt.show()

# Age Distribution
plt.figure(figsize=(8, 5))
sns.histplot(df['Age'], bins=30, kde=True, color='skyblue')
plt.title('Customer Age Distribution')
plt.savefig("age_distribution.png")
plt.show()

# Purchase Amount Distribution
plt.figure(figsize=(8, 5))
sns.histplot(df['Total Purchase Amount'], bins=50, kde=True, color='lightgreen')
plt.title('Total Purchase Amount Distribution')
plt.savefig("purchase_amount.png")
plt.show()

# Purchases Over Time
df['Month'] = df['Purchase Date'].dt.to_period('M').astype(str)
monthly_sales = df.groupby('Month')['Total Purchase Amount'].sum().reset_index()

plt.figure(figsize=(12, 5))
sns.lineplot(data=monthly_sales, x='Month', y='Total Purchase Amount', marker='o')
plt.xticks(rotation=45)
plt.title('Monthly Total Purchase Amount')
plt.tight_layout()
plt.savefig("monthly_sales.png")
plt.show()
