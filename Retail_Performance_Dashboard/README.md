# Superstore Sales Analysis using Python

### 📊 Project Overview  
Performed exploratory data analysis (EDA) on the Superstore dataset to uncover trends in **sales**, **profit**, and **discount impact** using Python.  
The goal of this project is to turn raw transactional data into **clear, actionable business insights** that support decision-making in pricing, discounting, and product strategy.

---

### ❓ Business Questions Answered  
- Which **regions** and **categories** generate the highest profit?  
- How do **discounts** impact profit margins?  
- Which **customer segments** contribute most to revenue and profit?  
- Which **product sub-categories** are consistently loss-making?  
- How do different **shipping modes** affect profitability?

---

### 🧠 Key Findings  
- **Total Sales:** `$2.3M`  
- **Total Profit:** `$286K`  
- **Average Profit Margin:** `12.4%`  
- Higher discounts correlated with **significant profit loss**, especially in certain furniture sub-categories.  
- Identified top-performing regions and categories based on profitability.  
- Some sub-categories showed **high sales but low or negative profit**, indicating discount or pricing issues.

---

### 🧰 Tools & Libraries  
- **Python**  
- **Pandas** – data cleaning, transformation & aggregations  
- **Matplotlib** – visualizations  
- **Seaborn** – statistical plots & aesthetics  
- (Optionally) **NumPy** for numerical calculations  

---

### 🛠 Skills Demonstrated  
- Data cleaning and preprocessing  
- GroupBy operations, aggregations & KPI calculations (e.g., profit margin)  
- Exploratory Data Analysis (EDA)  
- Creating business-focused charts for stakeholders  
- Interpreting relationships between discount, sales, and profit  
- Communicating insights in a structured, business-friendly format  

---

### 📈 Visualizations  
The project includes multiple visual analyses, such as:

- **Regional Sales Bar Chart** – Compare total sales across regions  
- **Profit by Category** – Identify high- and low-margin product categories  
- **Discount vs Profit Scatter Plot** – Understand how increasing discounts affect profit  
- **Shipping Mode Profit Distribution** – See which shipping modes are more profitable  
- (Optional) **Top/Bottom Sub-Categories by Profit** – Detect loss-making products

---

### 🔄 Analysis Workflow (High Level)  

1. **Load & Inspect Data**  
   - Read `Sample - Superstore.csv` using Pandas  
   - Check data types, missing values, and basic statistics  

2. **Data Cleaning & Feature Engineering**  
   - Convert date columns to datetime  
   - Create **Profit Margin** = `Profit / Sales`  
   - Derive additional time-based fields (e.g., Year, Month) if needed  

3. **Exploratory Data Analysis (EDA)**  
   - Sales & profit by region, category, sub-category, and segment  
   - Distribution of discounts and their relationship with profit  
   - Identify top and bottom contributing segments and products  

4. **Visualization & Insight Generation**  
   - Build charts to visually support findings  
   - Highlight regions/categories where discounts are eroding profit  
   - Summarize insights in a report (`Python_Project_Report.pdf`)  

---

### 🧾 Files  

- `superstore_analysis.py` – main Python script for analysis  
- `Sample - Superstore.csv` – input dataset (Superstore sample data)  
- `Python_Project_Report.pdf` – summary of key insights & charts  
- `README.md` – project documentation (this file)

(Optional, if you add folders later):  
- `plots/` – exported PNGs of charts  

---

### 📁 Suggested Repository Structure  

```bash
Superstore_Python_Analysis/
│── superstore_analysis.py
│── Sample - Superstore.csv
│── Python_Project_Report.pdf
└── README.md
# (Optional)
└── plots/
    ├── regional_sales_bar_chart.png
    ├── profit_by_category.png
    ├── discount_vs_profit_scatter.png
    └── shipping_mode_profit.png
