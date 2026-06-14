# Employee Attrition & HR Analytics Dashboard

A comprehensive **end-to-end HR analytics project** that analyses employee attrition patterns, identifies retention risks, and delivers actionable recommendations for workforce optimization.

## 📊 Project Overview

This portfolio project demonstrates **full-stack business analytics capability** — from data collection and cleaning through KPI design, advanced visualization, and strategic recommendation development.

**Data Period:** January – December 2024  
**Employees Analysed:** 120 records across 7 departments  
**Key Insight:** 36.7% attrition rate (3x industry benchmark), with 59.1% driven by work-life balance issues.

---

## 🎯 Key Findings

| Metric | Value | Status |
|--------|-------|--------|
| **Attrition Rate** | 36.7% | 🔴 Critical (benchmark: 15–20%) |
| **Retention Rate** | 63.3% | ⚠️ Below target (goal: 80%+) |
| **Avg Job Satisfaction** | 6.1/10 | ⚠️ Below threshold (target: 7.0+) |
| **Avg Engagement** | 5.8/10 | ⚠️ Below threshold (target: 7.0+) |
| **Overtime Rate** | 47.5% | 🔴 Critical |
| **Promotion Rate** | 45.8% | ⚠️ Only 55% promoted in 2024 |
| **High-Risk Employees** | 50 | 🔴 Immediate intervention needed |

### Top 5 Attrition Drivers:
1. **Work-Life Balance** — 59.1% of departures
2. **Lack of Career Growth** — 25.0%
3. **Manager Conflict** — 11.4%
4. **Low Salary** — 3.2%
5. **Other Reasons** — 1.3%

### Highest-Risk Departments:
- 🔴 **Legal** — 50.0% attrition
- 🔴 **Marketing** — 50.0% attrition
- 🟠 **Sales** — 43.8% attrition
- 🟠 **IT** — 42.1% attrition

---

## 📁 Project Structure

```
Employee-Attrition-HR-Analytics/
├── README.md                                    # This file
│
├── python/
│   │   ├── hr_analytics_data.py                # Dataset generation & KPI calculation
│   │   ├── hr_dashboard.py                     # Dashboard visualization (3 pages)
│   │
├── data/
│       ├── dataset.xlsx                        # Raw data
│
├── dashboard
│   ├── Page1_KPI_Attrition_Overview.png        # KPIs + attrition analysis (6 charts)
│   ├── Page2_Demographics_Department.png       # Workforce profiling + dept analysis (8 charts)
│   └── Page3_Engagement_Retention.png          # Engagement deep dive + opportunities (7 charts)
│
├── reports
│   ├── HR_Attrition_Recommendations_Report.pdf         # 6-page recommendations report
|
├── excel
│   └── Employee_Attrition_HR_Analytics_Excel Analysis.xlsx      # 5-sheet Excel workbook

```

---


## 📊 Dashboard Overview

<img width="3075" height="1941" alt="Page1_KPI_Attrition_Overview" src="https://github.com/user-attachments/assets/4f314a09-41da-438d-ac30-bc3d596be85e" />
<img width="3143" height="1941" alt="Page2_Demographics_Department" src="https://github.com/user-attachments/assets/ac1716c6-ab9c-4b1f-b35c-d28be7d983d0" />
<img width="3032" height="1882" alt="Page3_Engagement_Retention" src="https://github.com/user-attachments/assets/0d5c7327-4d0d-4611-9f8d-5f97b8512b27" />

### **Page 1: KPI Overview & Attrition Summary**
- 10 KPI cards (colour-coded metrics)
- Attrition rate by department (horizontal bar chart)
- Attrition reasons breakdown (pie chart)
- Attrition by gender, tenure, overtime status, promotion status
- Satisfaction vs engagement scatter plot

### **Page 2: Workforce Demographics & Department Analysis**
- Age distribution by attrition status (histogram)
- Gender split (donut chart)
- Education level impact on attrition
- Marital status analysis
- Department performance heatmap
- Average salary by department
- Top 10 job roles by attrition count
- Performance rating vs attrition correlation

### **Page 3: Engagement, Satisfaction & Retention Opportunities**
- Engagement score distribution
- Avg satisfaction & engagement by department (grouped bar)
- Training hours vs attrition rate correlation
- Manager rating impact on attrition (line chart)
- Work-life balance vs attrition (bar chart)
- Employee risk category distribution
- **5 retention opportunity recommendations** with implementation strategies

---

## 📋 Excel Workbook (5 Sheets)

| Sheet | Content | Features |
|-------|---------|----------|
| **Employee Data** | 120 employee records | Colour-coded attrition status, all 20 attributes |
| **KPI Summary** | 10 KPI cards + dept table | Formatted cards, performance metrics |
| **Department Analysis** | Dept-wise metrics + chart | Bar chart, risk levels, salary comparison |
| **Attrition Analysis** | Reasons + tenure breakdown | Pie chart, actionable insights |
| **Engagement Dashboard** | Satisfaction/engagement table | Risk levels, line chart, trends |

---

## 📄 Reports

### **PDF Report (6 Pages)**
1. Cover page with KPI strip
2. Executive summary + KPI cards
3. Key findings breakdown
4. Department performance table
5. Recommendations table + roadmap + methodology
6. Conclusion + project signature

---

## 🔍 Methodology

### **1. Data Profiling**
- 120 employee records across 7 departments (Finance, HR, IT, Legal, Marketing, Operations, Sales)
- 20 attributes per employee: demographics, job info, performance, satisfaction, engagement, attrition status

### **2. KPI Framework**
10 key performance indicators designed to capture complete workforce health:
- Attrition Rate % — 36.7% (vs 15–20% benchmark)
- Retention Rate % — 63.3%
- Average Tenure — 11.1 years
- Average Monthly Income — $72.5K
- Job Satisfaction Score — 6.1/10
- Employee Engagement Score — 5.8/10
- Promotion Rate % — 45.8%
- Overtime Rate % — 47.5%
- Training Participation % — 100%
- Department-wise Attrition Rate — varies by dept

### **3. Risk Scoring Model**
Composite Risk Score (0–10) based on 6 weighted factors:
- Job Satisfaction Score (weight: 2)
- Employee Engagement Score (weight: 2)
- Overtime Status (weight: 1)
- Promotion Status (weight: 1)
- Manager Rating (weight: 2)
- Work-Life Balance Score (weight: 2)

**Risk Categories:**
- 🟢 Low Risk (0–2) — 29 employees
- 🟡 Medium Risk (3–5) — 41 employees
- 🔴 High Risk (6+) — 50 employees flagged for intervention

### **4. Root Cause Analysis**
Cross-referenced attrition with:
- Tenure bands (0–3 yrs shows 39% attrition)
- Department (Legal/Marketing at 50%)
- Overtime status (overtime employees 2.8× higher attrition)
- Satisfaction levels (<5.0 score = 2.8× attrition risk)
- Manager quality (low manager ratings strongly correlated with departures)
- Promotion history (unpromoted 4+ yr employees at elevated risk)

### **5. Cost Analysis**
- Estimated replacement cost: **1.5–2× annual salary per employee**
- Current annual attrition cost: **~$3.3M–$4.4M** (44 departures × avg $75K salary)
- **ROI opportunity:** 20–30% attrition reduction = $660K–$1.3M annual savings

---

## 💡 Improvement Recommendations (8-Point Roadmap)

| # | Finding | Priority | Recommendation | Expected Benefit | Timeline |
|---|---------|----------|-----------------|-----------------|----------|
| 1 | WLB drives 59% of attrition | HIGH | Flexible scheduling, hybrid work, overtime caps | Attrition ↓20–25% | Q1 2025 |
| 2 | Lack of growth (25%) | HIGH | Career ladder framework, structured promotions | Attrition ↓15% | Q1 2025 |
| 3 | Legal/Marketing at 50% | HIGH | Stay interviews, compensation review, coaching | Attrition ↓30% | Q2 2025 |
| 4 | Manager conflict (11%) | MEDIUM | 360° feedback, leadership coaching | Attrition ↓10% | Q2 2025 |
| 5 | Low satisfaction <5 | MEDIUM | Quarterly pulse surveys + action planning | Satisfaction ↑15% | Q2 2025 |
| 6 | 50 high-risk employees | MEDIUM | Personalised retention plans | Retention ↑10% | Q3 2025 |
| 7 | Overtime at 47.5% | MEDIUM | Workload audit, right-sizing, automation | WLB score ↑20% | Q3 2025 |
| 8 | Training impact on retention | LOW | L&D linked to career progression | Engagement ↑10% | Q4 2025 |

### **4-Phase Implementation Roadmap**

**Phase 1 — Quick Wins (Q1 2025)**
- Deploy hybrid/flexible work policy
- Launch overtime tracking & escalation alerts
- Begin stay interviews (Legal & Marketing)
- Target: 15% attrition reduction

**Phase 2 — Structural (Q2 2025)**
- Career ladder framework across all departments
- 360° feedback programme for all people-managers
- Quarterly employee engagement pulse surveys
- Target: +15% satisfaction, +20% promotion visibility

**Phase 3 — Engagement (Q3 2025)**
- Personalised retention plans for 50 high-risk employees
- L&D programme linked to clear career paths
- Manager coaching & development programme
- Target: +15% engagement, +10% retention

**Phase 4 — Continuous Improvement (2026+)**
- Monthly attrition KPI dashboard reviews
- Predictive attrition modelling (machine learning)
- HR governance & standardised processes
- Target: Sustained <20% attrition, 85%+ retention

---

## 📊 Data Specifications

### **Employee Dataset (120 records)**
```
Columns: 20 attributes
- Employee_ID (EMP-0001 to EMP-0120)
- Employee_Name (realistic first + last names)
- Age (22–58 years)
- Gender (Male/Female)
- Department (7 depts: Sales, IT, HR, Finance, Operations, Marketing, Legal)
- Job_Role (22 different roles)
- Education_Level (High School, Bachelor's, Master's, PhD)
- Marital_Status (Single, Married, Divorced)
- Years_at_Company (1–20 years)
- Monthly_Income ($40K–$102K range)
- Performance_Rating (1–5 scale)
- Job_Satisfaction_Score (1–10 scale)
- Work_Life_Balance_Score (1–5 scale)
- Training_Hours (4–40 hours annually)
- Promotion_Status (Promoted / Not Promoted)
- Overtime_Status (Yes / No)
- Attrition_Status (Yes / No)
- Attrition_Reason (7 categories)
- Manager_Rating (1–5 scale)
- Employee_Engagement_Score (1–10 scale)
```

### **Attrition Reasons Breakdown**
- Work-Life Balance — 26 employees (59.1%)
- Lack of Growth — 11 employees (25.0%)
- Manager Conflict — 5 employees (11.4%)
- Low Salary — 1 employee (2.3%)
- Other — 1 employee (2.3%)
- **Total Attrition:** 44 employees / 120 = 36.7%

---

## 🛠️ Technologies Used

| Tool | Purpose |
|------|---------|
| **Python 3.9+** | Data generation, analysis, automation |
| **Pandas** | Data manipulation & aggregation |
| **NumPy** | Numerical computing |
| **Matplotlib & Seaborn** | Professional visualizations & dashboards |

---

## 📈 Key Statistics

| Metric | Value |
|--------|-------|
| Total Employees | 120 |
| Departments | 7 |
| Attrition Count | 44 |
| Retention Count | 76 |
| Avg Tenure | 11.1 years |
| Avg Monthly Salary | $72,514 |
| Highest-Paid Dept | Legal ($101.7K avg) |
| Lowest-Paid Dept | HR ($52.0K avg) |
| Highest Attrition Dept | Legal & Marketing (50% each) |
| Lowest Attrition Dept | Finance (27.3%) |
| High-Risk Employees | 50 (41.7%) |
| Medium-Risk Employees | 41 (34.2%) |
| Low-Risk Employees | 29 (24.2%) |

---

## 📊 Visual Sneak Peek

**Page 1: KPI Overview**
- 10 colour-coded metric cards
- Attrition breakdown by department, gender, tenure
- Overtime vs attrition correlation
- Promotion vs attrition comparison

**Page 2: Demographics & Departments**
- Age distribution, gender split, education impact
- Department performance heatmap
- Salary by department
- Job role analysis

**Page 3: Engagement & Retention**
- Satisfaction & engagement distribution
- Training hours correlation
- Manager rating impact
- Work-life balance vs attrition
- 5 retention opportunity cards with specific actions

---

## ✨ Key Takeaway

**This project demonstrates that data-driven HR strategy can unlock significant value.** By systematically addressing work-life balance, career development, and manager effectiveness, organisations can realistically improve retention by 20–30% and save hundreds of thousands annually — all grounded in solid analytics.
