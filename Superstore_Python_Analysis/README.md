# Superstore Sales Analysis (Python)

## 1. Project Overview
This project explores the Superstore sales dataset using Python to understand 
which **regions, categories, and discounts** drive profit and where money is 
being lost. The goal is to produce clear, business-ready insights that can be 
used in a presentation or dashboard.

---

## 2. Objectives
- Identify the most and least profitable:
  - Regions
  - Product categories / sub-categories
  - Customer segments
- Quantify the impact of **discounts on profit**.
- Build simple visualizations that can be reused in a slide deck or dashboard.
- Practice an end-to-end analytics workflow using Python.

---

## 3. Dataset
- Source: Superstore sales data (same dataset used for the Tableau dashboard).
- Typical columns:
  - `Order ID`, `Order Date`, `Ship Date`, `Ship Mode`
  - `Customer ID`, `Segment`, `Region`
  - `Category`, `Sub-Category`
  - `Sales`, `Quantity`, `Discount`, `Profit`

You can place the CSV file here:  
`Superstore_Python_Analysis/data/superstore.csv`

---

## 4. Tech Stack & Skills Demonstrated
- **Python**: data wrangling & analysis
- **Pandas**: cleaning, aggregations, groupby
- **NumPy**: numerical operations
- **Matplotlib / Seaborn**: visualizations
- **Jupyter Notebook**: analysis workflow & storytelling

Key skills:
- Handling missing / inconsistent values  
- Creating derived KPIs (e.g., profit margin)  
- Grouped analysis by region, category, and segment  
- Visual storytelling for business users  

---

## 5. Key Questions
1. Which **regions** and **categories** contribute the most to total sales and profit?
2. Are there any regions / categories where **high discounts** are causing **profit loss**?
3. How does **profit margin** vary by:
   - Region
   - Category
   - Customer segment?
4. Are there specific **product sub-categories** that are consistently unprofitable?

---

## 6. Analysis Steps

1. **Import & Inspect**
   - Load the dataset with Pandas.
   - Check shape, column types, and basic statistics.

2. **Data Cleaning**
   - Handle missing values if any.
   - Fix data types for dates (`Order Date`, `Ship Date`).
   - Create new columns:
     - `Profit_Margin = Profit / Sales`
     - `Year`, `Month` from `Order Date`.

3. **Exploratory Data Analysis (EDA)**
   - Overall descriptive stats of `Sales`, `Profit`, `Discount`, `Profit_Margin`.
   - Sales & profit by:
     - Region
     - Category
     - Segment
   - Top 10 sub-categories by sales vs by profit.

4. **Discount vs Profit**
   - Scatter plot: `Discount` vs `Profit`.
   - Group by discount buckets (e.g. 0–10%, 10–20%, 20%+).
   - Compare average profit margin across buckets.

5. **Time Trends**
   - Monthly sales & profit trend.
   - Highlight any seasonality or drops.

---

## 7. Visualizations
Some suggested plots:
- Bar chart: Sales & Profit by Region
- Bar chart: Profit Margin by Category
- Scatter plot: Discount vs Profit
- Line chart: Monthly Profit trend
- Horizontal bar: Top/Bottom 10 Sub-Categories by Profit

These can be exported as PNGs and reused in:
- PowerPoint / Google Slides
- Portfolio case study
- Tableau / Power BI dashboards

---

## 8. Results & Insights (Example Template)
You can adjust these based on your actual results:

- The **West** region drives the highest profit, while the **Central** region 
  shows lower profit margins despite strong sales.
- High discounts (>30%) are strongly associated with **negative profit** in the 
  Furniture category.
- A small set of sub-categories (e.g., Tables, Bookcases) are responsible for a 
  large share of total losses.
- Reducing discount levels for specific loss-making categories by 10–15% could 
  significantly improve overall profit.

---

## 9. How to Run This Project

1. Clone the repository:
   ```bash
   git clone https://github.com/Mounika24-dotcom/Data-Analyst-Portfolio.git
   cd Data-Analyst-Portfolio/Superstore_Python_Analysis
