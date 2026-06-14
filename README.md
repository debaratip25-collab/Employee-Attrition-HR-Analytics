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
├── requirements.txt                             # Python dependencies
│
├── 📊 DATA & ANALYSIS
│   ├── python/
│   │   ├── hr_analytics_data.py                # Dataset generation & KPI calculation
│   │   ├── hr_dashboard.py                     # Dashboard visualization (3 pages)
│   │   └── hr_excel.py                         # Excel workbook generation
│   │
│   └── outputs/
│       ├── hr_attrition_dataset.csv            # 120 employee records (raw data)
│       ├── department_analysis.csv             # Department-wise metrics
│       ├── attrition_reasons.csv               # Attrition breakdown
│       ├── high_risk_employees.csv             # Top 50 at-risk profiles
│       └── kpis.json                           # All 10 KPIs in JSON format
│
├── 📈 DASHBOARDS & VISUALIZATIONS
│   ├── Page1_KPI_Attrition_Overview.png        # KPIs + attrition analysis (6 charts)
│   ├── Page2_Demographics_Department.png       # Workforce profiling + dept analysis (8 charts)
│   └── Page3_Engagement_Retention.png          # Engagement deep dive + opportunities (7 charts)
│
├── 📄 PROFESSIONAL REPORTS
│   ├── Employee_Attrition_HR_Analytics_Dashboard.docx  # 12-section Word document
│   ├── HR_Attrition_Recommendations_Report.pdf         # 6-page recommendations report
│   └── Employee_Attrition_HR_Analytics_Excel.xlsx      # 5-sheet Excel workbook
│
└── 🔧 SUPPORTING FILES
    └── (dashboard/): Raw PNG exports
```

---

## 🚀 Quick Start

### Prerequisites
```bash
pip install pandas numpy matplotlib seaborn openpyxl reportlab
```

### Running the Project

**Step 1: Generate Data & Calculate KPIs**
```bash
cd python/
python hr_analytics_data.py
```
Output: CSV files + KPI metrics

**Step 2: Create Dashboards**
```bash
python hr_dashboard.py
```
Output: 3 publication-ready PNG dashboard pages

**Step 3: Generate Excel Workbook**
```bash
python hr_excel.py
```
Output: Professional 5-sheet Excel file with charts

**Step 4: Generate PDF Report**
```bash
python hr_pdf.py
```
Output: 6-page recommendations report

---

## 📊 Dashboard Overview

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

### **Word Document (12 Sections)**
1. Cover page with branding
2. Executive summary
3. Key findings (5 critical insights)
4. Department performance summary
5. Business analysis activities
6. HR metrics & KPI framework
7. 8-point improvement recommendations
8. 4-phase implementation roadmap
9. Dashboard design guide
10. Business insights Q&A
11. GitHub & LinkedIn showcase guide
12. Interview preparation (Q&A)

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
| **OpenPyXL** | Excel workbook generation with formatting |
| **ReportLab** | PDF report generation |
| **Node.js + docx** | Word document generation |

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

## 💼 Career Applications

This project demonstrates:

✅ **Data Analysis** — Dataset creation, cleaning, KPI calculation, trend analysis  
✅ **Data Visualization** — Multi-page dashboards, chart selection, professional styling  
✅ **Business Intelligence** — Insight extraction, risk identification, actionable recommendations  
✅ **Automation** — Python scripting to generate 120+ outputs in seconds  
✅ **Reporting** — Professional documents (PDF, Excel, Word) with branded formatting  
✅ **Problem-Solving** — Root cause analysis, cost quantification, solution roadmap  
✅ **Communication** — Clear findings, visual storytelling, executive-ready output  

**Relevant Job Roles:**
- Business Analyst
- Data Analyst
- HR Analytics / People Operations Analyst
- BI Analyst / Dashboard Developer
- Operations Analyst

---

## 🎓 Interview Questions & Answers

### **Q1: Explain your project.**
A: I built an end-to-end HR Analytics Dashboard that analyses 120 employee records across 7 departments to identify attrition patterns and retention risks. The project includes Python-driven data analysis, three professional dashboard pages with 20+ charts, and strategic recommendations. I discovered that 36.7% attrition — driven primarily by work-life balance issues (59.1%) and lack of career growth (25%) — presents a 20–30% reduction opportunity worth $660K–$1.3M annually.

### **Q2: What is employee attrition?**
A: Attrition is the gradual reduction of workforce headcount through voluntary resignations or non-replacement of departing employees. It differs from layoffs in that it's employee-driven. High attrition increases recruitment costs, disrupts team continuity, and signals organizational health issues. Industry benchmarks are 15–20% annually; our analysis found 36.7%.

### **Q3: Why does attrition matter to businesses?**
A: High attrition is extremely costly — estimated at 1.5–2× annual salary per departing employee for recruitment, onboarding, training, and lost productivity. In this case, 44 departures cost ~$3.3M–$4.4M annually. More critically, losing experienced employees disrupts operations, damages team morale, and reduces organizational knowledge.

### **Q4: What tools did you use?**
A: Python (pandas, numpy, matplotlib, seaborn) for data analysis and dashboard generation; openpyxl for Excel automation; reportlab for PDF generation; and docx library for Word documents. I chose Python for its power to automate all 120 outputs in seconds — recreating these manually would take weeks.

### **Q5: How did you identify high-risk employees?**
A: I built a composite Risk Score (0–10) based on 6 weighted factors: satisfaction, engagement, overtime status, promotion history, manager rating, and work-life balance. Employees scoring 6+ were flagged as High Risk. This identified 50 employees requiring immediate retention intervention.

### **Q6: What's your biggest insight from this analysis?**
A: Work-life balance is the dominant attrition driver at 59.1%. With 47.5% of the workforce on overtime, this is a systemic workload issue rather than individual cases. A targeted flexible work policy, overtime reduction programme, and role right-sizing could realistically reduce attrition by 20–25% within one year — saving over $660K annually.

---

## 📚 How to Use This Repository

### **For Portfolio/Interview Showcase:**
1. Clone the repo
2. Review README.md (you're reading it!)
3. Check the three dashboard PNG images
4. Open the Excel workbook to explore interactive data
5. Read the PDF report for findings & recommendations
6. Open the Word document for full project scope

### **To Recreate the Analysis:**
1. Install dependencies: `pip install -r requirements.txt`
2. Run `python/hr_analytics_data.py` → generates CSV datasets
3. Run `python/hr_dashboard.py` → creates 3 dashboard PNGs
4. Run `python/hr_excel.py` → creates Excel workbook
5. Run `python/hr_pdf.py` → generates PDF report

### **To Modify the Project:**
- Change dataset size in `hr_analytics_data.py` (line: `for i in range(1, 121)`)
- Modify colour palette in `hr_dashboard.py` (PRIMARY, SECONDARY, etc.)
- Edit recommendations in `hr_pdf.py` or `hr_word.js`
- Update date from June 2026 to current date

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

## 🤝 Contributing

This is a portfolio project. If you'd like to extend it:
- Add machine learning predictions (attrition probability model)
- Integrate live HR data sources (Workday, SAP SuccessFactors)
- Create interactive Power BI / Tableau dashboard
- Add sentiment analysis on exit interview feedback
- Implement predictive retention scoring

---

## 📞 Contact & Social

**LinkedIn:** [Your LinkedIn URL]  
**Email:** [Your Email]  
**Portfolio:** [Your Portfolio Site]

---

## 📄 License

This project is shared as a portfolio demonstration. Feel free to fork, modify, and use for learning purposes.

---

## 🙏 Acknowledgments

Inspired by BPO (Business Process Optimization) analysis frameworks and real-world HR analytics challenges. Built as a complete end-to-end business analytics demonstration.

---

**Last Updated:** June 2026  
**Project Type:** Portfolio / Educational  
**Difficulty Level:** Intermediate–Advanced  
**Time to Complete:** 2–3 hours (running all scripts + reviewing outputs)

---

## ✨ Key Takeaway

**This project demonstrates that data-driven HR strategy can unlock significant value.** By systematically addressing work-life balance, career development, and manager effectiveness, organisations can realistically improve retention by 20–30% and save hundreds of thousands annually — all grounded in solid analytics.
