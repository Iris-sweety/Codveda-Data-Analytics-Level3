# 📊 Level 3 - Task 2 : Dashboard with Power BI
**Internship** : Codveda Technologies — Data Analytics  
**Level** : 3 (Advanced)  
**Dataset** : Telecom Customer Churn (3,333 customers)  
**Tool** : Microsoft Power BI Desktop

---

## 🎯 Objective
Build an interactive 3-page dashboard to analyze customer churn
behavior in a telecom company and identify the key drivers
that lead customers to leave.

---


## 🛠️ Tools & Libraries
| Tool | Usage |
|------|-------|
| `Python / pandas` | Data cleaning and feature engineering |
| `Power BI Desktop` | Dashboard creation and publishing |
| `DAX` | Custom measures and KPIs |

---

## ⚙️ Data Preparation (Python)
Before importing into Power BI, the dataset was cleaned and
enriched with the following steps :
- Merged `churn 80.csv` and `churn 20.csv` → **3,333 rows**
- Standardized column names (lowercase + underscore)
- Converted `churn` boolean to `churn_binary` (0/1)
- Created `account_group` : Short / Medium / Long / Very Long
- Created `service_calls_group` : 0-1 / 2-3 / 4-5 / 6+ calls
- Calculated `total_charges`, `total_minutes`, `total_calls`

---

## 📊 Dashboard Structure

### Page 1 — Overview
**KPI Cards :**
- Total Customers : **3K**
- Churn Rate : **14.49%**
- Avg Service Calls : **1.56**
- Avg Total Charges : **$59.45**

**Charts :**
- Churn Distribution (Donut) →
  85.51% retained vs 14.49% churned
- Churn Rate by International Plan (Bar) →
  customers with international plan churn significantly more
- Churn Rate by Voice Mail Plan (Bar) →
  customers without voice mail plan churn more

---

### Page 2 — Customer Behavior
**Charts :**
- Churn by Customer Service Calls Group (Bar) →
  churn increases sharply after 4+ service calls
- Churn Rate by Account Group (Bar) →
  churn rate is relatively stable across tenure groups
- Top 10 States by Churn Rate (Bar) →
  CA, NJ, TX, MD, SC are the highest churn states

---

### Page 3 — Usages
**Charts :**
- Avg Total Charges by Churn →
  churned customers (True) pay slightly more on average
- Avg Day Charges by International Plan →
  international plan customers have higher day charges
- Avg Voicemail Messages by Churn →
  retained customers use voicemail significantly more
- Avg Day Minutes by Churn →
  churned customers use slightly more day minutes

---

## 🔍 Key Findings

### 1. Overall Churn Rate
The overall churn rate is **14.49%** (482 out of 3,333 customers).
This is a significant business risk — nearly 1 in 7 customers leaves.

### 2. International Plan is a Major Churn Driver
Customers **with** an international plan churn at a much higher
rate (~40%) compared to those without (~11%).
This suggests the international plan pricing or quality
is a key pain point for customers.

### 3. Customer Service Calls = Strongest Churn Predictor
Churn increases dramatically with the number of service calls :
- **0-1 calls** : low churn rate (~8%)
- **2-3 calls** : moderate churn (~12%)
- **4-5 calls** : high churn (~45%)
- **6+ calls** : very high churn (~60%+)

Customers who call support repeatedly are clearly dissatisfied
and at very high risk of leaving.

### 4. Voice Mail Plan Reduces Churn
Customers **without** a voice mail plan churn significantly more.
The voice mail plan may increase engagement and satisfaction,
acting as a retention factor.

### 5. Geographic Concentration
The top 5 churning states (CA, NJ, TX, MD, SC) represent
a disproportionate share of lost customers.
Targeted retention campaigns in these states could have
high business impact.

### 6. Churned Customers Pay More
Churned customers have slightly higher average total charges
and use more day minutes than retained customers.
High-usage customers who feel they are not getting value
for money are more likely to leave.

### 7. Voicemail Usage Signals Loyalty
Retained customers have significantly higher average voicemail
messages, suggesting they are more engaged with the service.

---

## 📈 Results Summary

| KPI | Value |
|-----|-------|
| Total Customers | 3,333 |
| Churn Rate | 14.49% |
| Avg Total Charges | $59.45 |
| Avg Service Calls | 1.56 |
| Top Churn State | CA |
| Highest Risk Group | 6+ service calls |
| International Plan Churn | ~40% |

---

## 💡 Business Recommendations
- **Review international plan pricing** — high churn rate
  among these customers signals dissatisfaction
- **Proactive outreach** after 3+ service calls to prevent
  customers from reaching the high-risk threshold
- **Promote voice mail plan** as a retention tool
- **Targeted campaigns** in CA, NJ, TX, MD and SC
- **Monitor high-usage customers** paying above average —
  offer loyalty discounts before they churn

---

## 🚀 How to Run

1. Run the data preparation notebook
```bash
python data_preparation.py
```

2. Open Power BI Desktop
```
File → Open → churn_dashboard.pbix
```

3. View published dashboard
```
https://app.powerbi.com/groups/me/reports/31678763-ea0f-427f-a9d0-e68a52b31943?experience=power-bi
```

---


*Codveda Technologies Internship — Data Analytics | 2026*
