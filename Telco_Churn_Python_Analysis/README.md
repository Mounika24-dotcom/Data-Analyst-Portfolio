# 📊 Telco Customer Churn Analysis (Python EDA)

## 1. 📌 Project Overview
This project analyzes the **Telco Customer Churn dataset** to uncover which customer behaviors, plans, service patterns, and payment methods lead to higher churn.  
The analysis is performed using Python with a focus on **clean EDA, visual storytelling, and business insights** that support data-driven retention strategies.

---

## 2. 🎯 Objectives
- Identify major **drivers of churn**
- Segment high-risk customer groups
- Explore how contract type, monthly charges, and service bundles affect churn
- Analyze payment methods, internet service types, and tenure patterns
- Deliver business-ready insights and recommendations

---

## 3. 🗂️ Dataset
**File:** `WA_Telco_Churn.csv`  
**Rows:** 7043  
**Columns:** 21  

Key features include:
- Customer demographics (`gender`, `SeniorCitizen`)
- Subscription details (`Contract`, `InternetService`, `PaymentMethod`)
- Charges (`MonthlyCharges`, `TotalCharges`)
- Add-on services (`TechSupport`, `DeviceProtection`, etc.)
- Churn flag (`Churn`)

---

## 4. 🛠️ Tech Stack & Libraries
- **Python**
- **Pandas**
- **NumPy**
- **Matplotlib**
- **Seaborn**
- **Jupyter Notebook**

---

## 5. 🔧 Data Cleaning Steps
- Replaced blank values in `TotalCharges`
- Converted `TotalCharges` → numeric
- Filled missing values for new customers (`tenure = 0`)
- Converted Yes/No columns to binary (0/1)
- Verified datatypes & summary statistics

---

## 6. 📈 Exploratory Data Analysis (EDA)

### **Univariate EDA**
- Churn distribution  
- Tenure distribution  
- Monthly charges histogram  
- Senior Citizen distribution  
- Contract type counts  
- Internet service type  
- Payment method distribution  

### **Bivariate EDA**
- Churn vs Contract Type  
- Churn vs Tenure  
- Churn vs Monthly Charges  
- Churn vs Internet Service  
- Churn vs Senior Citizen  
- Churn vs Payment Method  
- **Correlation Heatmap (numeric features)**  

---

## 7. 🧠 Key Insights (Business-Focused)

### 🔥 1. Early-life churn is the biggest risk  
Customers with **tenure < 6 months** show the highest churn.  
➡️ Improve onboarding, support, and first-90-day experience.

### 🔥 2. Contract type is the strongest churn driver  
Month-to-month customers churn **5× more** than yearly contracts.  
➡️ Promote contract upgrades with loyalty discounts.

### 🔥 3. Fiber customers churn more due to missing support—not pricing  
Fiber users have lower adoption of Tech Support, Security, Backup.  
➡️ Bundle support features for Fiber plans.

### 🔥 4. Mid-range monthly charges ($60–$80) churn the most  
High-paying customers ($100+) are loyal; mid-tier feels expensive.  
➡️ Improve value or discount structure for mid-tier plans.

### 🔥 5. Electronic Check customers churn the highest  
➡️ Encourage switching to auto-pay (Card/Bank Transfer).

### 🔥 6. Missing Tech Support triples churn  
➡️ Make Tech Support a default add-on for new customers.

### 🔥 7. Add-on bundles reduce churn dramatically  
0–1 add-ons = high churn  
3–6 add-ons = very loyal  
➡️ Focus retention on increasing add-on adoption early.

### 🔥 8. Senior Citizens churn due to weak bundles, not age  
➡️ Create senior-friendly support & protection packages.

### 🔥 9. Gender does not impact churn  
➡️ No demographic bias in churn behavior.

### 🔥 10. Paperless billing increases churn only with monthly contracts  
➡️ Promote auto-renewal discounts for paperless+monthly users.

---

## 8. 📊 Visualizations Included
- Churn distribution  
- Tenure distribution  
- Monthly charges distribution  
- Contract vs Churn  
- Monthly charges vs Churn  
- Internet service vs Churn  
- Senior Citizen vs Churn  
- Payment method vs Churn  
- Correlation heatmap  


---


