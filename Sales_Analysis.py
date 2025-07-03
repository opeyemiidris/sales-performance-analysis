
# Sales Performance Analysis

## 1. Import Libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
df = pd.read_excel('sales_data.xlsx')

# Preview
df.head()

## 2. Monthly Sales Trend
df['Date'] = pd.to_datetime(df['Date'])
df['Month'] = df['Date'].dt.to_period('M')
monthly_sales = df.groupby('Month')['Total_Sales'].sum().reset_index()

plt.figure(figsize=(10,5))
sns.lineplot(data=monthly_sales, x='Month', y='Total_Sales', marker='o')
plt.title('Monthly Sales Trend')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

## 3. Sales by Region
region_sales = df.groupby('Region')['Total_Sales'].sum().sort_values(ascending=False)

plt.figure(figsize=(8,5))
sns.barplot(x=region_sales.index, y=region_sales.values)
plt.title('Sales by Region')
plt.ylabel('Total Sales')
plt.tight_layout()
plt.show()

## 4. Top Products by Sales
product_sales = df.groupby('Product')['Total_Sales'].sum().sort_values(ascending=False)

plt.figure(figsize=(8,5))
sns.barplot(x=product_sales.index, y=product_sales.values, palette='viridis')
plt.title('Top Products by Sales')
plt.ylabel('Total Sales')
plt.tight_layout()
plt.show()

## 5. Sales by Sales Rep
rep_sales = df.groupby('Sales_Rep')['Total_Sales'].sum().sort_values(ascending=False)

plt.figure(figsize=(8,5))
sns.barplot(x=rep_sales.index, y=rep_sales.values, palette='coolwarm')
plt.title('Sales by Sales Rep')
plt.ylabel('Total Sales')
plt.tight_layout()
plt.show()

## 6. Insights:
# - Which region has the highest sales?
# - What product line performs best?
# - How evenly are sales distributed among reps?
