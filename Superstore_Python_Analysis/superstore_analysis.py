# STEP 1: Import Libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# STEP 2: Load Dataset
df = pd.read_csv("/Users/yegireddimounika/Downloads/Sample - Superstore.csv", encoding='latin1')
print("✅ Data Loaded Successfully!")
print("Shape of data:", df.shape)

# STEP 3: Basic Info
print("\n--- Data Summary ---")
print(df.info())
print("\nMissing Values:\n", df.isnull().sum().sum())
print("\nSample Rows:\n", df.head())

# STEP 4: Data Cleaning & Feature Engineering
df['Order Date'] = pd.to_datetime(df['Order Date'])
df['Ship Date'] = pd.to_datetime(df['Ship Date'])
df['Year'] = df['Order Date'].dt.year
df['Month'] = df['Order Date'].dt.month
df['Weekday'] = df['Order Date'].dt.day_name()
df['Profit Margin'] = (df['Profit'] / df['Sales']) * 100

# STEP 5: Quick Duplicate Check
dupes = df.duplicated().sum()
print(f"\nDuplicates Found: {dupes}")

# STEP 6: Key KPIs
total_sales = df['Sales'].sum()
total_profit = df['Profit'].sum()
avg_margin = df['Profit Margin'].mean()

print("\n📊 --- Key Performance Indicators ---")
print(f"Total Sales: ${total_sales:,.2f}")
print(f"Total Profit: ${total_profit:,.2f}")
print(f"Average Profit Margin: {avg_margin:.2f}%")

# STEP 7: Regional & Category Analysis
region_sales = df.groupby('Region')['Sales'].sum().sort_values(ascending=False)
category_profit = df.groupby('Category')['Profit'].sum().sort_values(ascending=False)

print("\nSales by Region:\n", region_sales)
print("\nProfit by Category:\n", category_profit)

# Visualization
region_sales.plot(kind='bar', title='Total Sales by Region')
plt.ylabel('Sales ($)')
plt.show()

category_profit.plot(kind='bar', color='orange', title='Total Profit by Category')
plt.ylabel('Profit ($)')
plt.show()

# STEP 8: Discount vs Profit Relationship
plt.figure(figsize=(7,5))
sns.scatterplot(data=df, x='Discount', y='Profit', alpha=0.5)
plt.title('Discount vs Profit')
plt.xlabel('Discount (%)')
plt.ylabel('Profit ($)')
plt.show()

# STEP 9: Shipping Speed vs Profitability
ship_profit = df.groupby('Ship Mode')['Profit'].mean().sort_values(ascending=False)
ship_sales = df.groupby('Ship Mode')['Sales'].sum().sort_values(ascending=False)
ship_margin = (df.groupby('Ship Mode')['Profit'].sum() /
               df.groupby('Ship Mode')['Sales'].sum()) * 100

print("\nAverage Profit by Ship Mode:\n", ship_profit)
print("\nTotal Sales by Ship Mode:\n", ship_sales)
print("\nProfit Margin (%) by Ship Mode:\n", ship_margin.round(2))

plt.figure(figsize=(7,5))
sns.boxplot(data=df, x='Ship Mode', y='Profit', palette='Set2')
plt.title('Profit Distribution by Shipping Mode')
plt.ylabel('Profit ($)')
plt.xlabel('Shipping Mode')
plt.show()

print("\n✅ Analysis Completed Successfully!")

# Export cleaned dataset for Tableau
df.to_csv("/Users/yegireddimounika/Downloads/Superstore_Cleaned.csv", index=False)
print("✅ Cleaned dataset exported successfully for Tableau!")
