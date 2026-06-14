"""
Employee Attrition & HR Analytics Dashboard
============================================
Project by: HR Analytics Portfolio Project
Data Period: January – December 2024
Employees Analysed: 100+ records

This script generates a realistic HR dataset and performs
comprehensive attrition and workforce analytics.
"""

import pandas as pd
import numpy as np
import random
import os

random.seed(42)
np.random.seed(42)

# ─────────────────────────────────────────────────────────────────────────────
# 1. DATASET GENERATION
# ─────────────────────────────────────────────────────────────────────────────

departments = ["Sales", "IT", "HR", "Finance", "Operations", "Marketing", "Legal"]
job_roles = {
    "Sales": ["Sales Executive", "Sales Manager", "Account Manager"],
    "IT": ["Software Engineer", "IT Support", "Data Analyst", "DevOps Engineer"],
    "HR": ["HR Executive", "HR Manager", "Recruiter", "L&D Specialist"],
    "Finance": ["Finance Analyst", "Accountant", "Finance Manager", "Auditor"],
    "Operations": ["Operations Analyst", "Process Manager", "Supply Chain Lead"],
    "Marketing": ["Marketing Executive", "Brand Manager", "Digital Marketer"],
    "Legal": ["Legal Analyst", "Compliance Officer", "Legal Counsel"],
}
education_levels = ["High School", "Bachelor's", "Master's", "PhD"]
marital_statuses = ["Single", "Married", "Divorced"]
attrition_reasons = [
    "Better Opportunity", "Work-Life Balance", "Low Salary",
    "Manager Conflict", "Lack of Growth", "Relocation", "Personal Reasons", "N/A"
]
genders = ["Male", "Female"]
overtime_statuses = ["Yes", "No"]
promotion_statuses = ["Promoted", "Not Promoted"]

first_names = [
    "Aarav", "Priya", "Rohan", "Sneha", "Vikram", "Ananya", "Arjun", "Kavya",
    "Rahul", "Neha", "Suresh", "Pooja", "Rajan", "Deepa", "Mohan", "Lakshmi",
    "Siddharth", "Ritu", "Nikhil", "Swati", "Amit", "Divya", "Kiran", "Meena",
    "Varun", "Shreya", "Neeraj", "Preeti", "Rajesh", "Sunita", "Harsh", "Geeta",
    "Ishan", "Tanvi", "Manish", "Shweta", "Piyush", "Rekha", "Gaurav", "Nandita",
    "Chirag", "Alka", "Vishal", "Namrata", "Akash", "Pallavi", "Tushar", "Renu",
    "Nitin", "Ankita"
]
last_names = [
    "Sharma", "Patel", "Verma", "Singh", "Kumar", "Mehta", "Das", "Nair",
    "Iyer", "Gupta", "Reddy", "Joshi", "Mishra", "Rao", "Shah", "Bose",
    "Chatterjee", "Pandey", "Sinha", "Tiwari"
]

records = []
for i in range(1, 121):
    emp_id = f"EMP-{i:04d}"
    name = f"{random.choice(first_names)} {random.choice(last_names)}"
    age = random.randint(22, 58)
    gender = random.choice(genders)
    dept = random.choice(departments)
    role = random.choice(job_roles[dept])
    edu = random.choice(education_levels)
    marital = random.choice(marital_statuses)
    years = random.randint(1, 20)

    # Salary influenced by department and experience
    base_salary = {"Sales": 45000, "IT": 70000, "HR": 40000, "Finance": 60000,
                   "Operations": 50000, "Marketing": 48000, "Legal": 75000}
    salary = int(base_salary[dept] * (1 + years * 0.03) + random.randint(-5000, 5000))

    perf = random.randint(1, 5)
    satisfaction = round(random.uniform(2.0, 10.0), 1)
    wlb = random.randint(1, 5)
    training_hours = random.randint(4, 40)
    promotion = random.choice(["Promoted", "Not Promoted"])
    overtime = random.choice(overtime_statuses)
    mgr_rating = random.randint(1, 5)
    engagement = round(random.uniform(2.0, 10.0), 1)

    # Attrition logic: higher chance if low satisfaction, overtime, low salary
    attrition_prob = 0.15
    if satisfaction < 5: attrition_prob += 0.15
    if overtime == "Yes": attrition_prob += 0.12
    if salary < 45000: attrition_prob += 0.10
    if promotion == "Not Promoted" and years > 3: attrition_prob += 0.08
    if wlb <= 2: attrition_prob += 0.10
    if mgr_rating <= 2: attrition_prob += 0.08

    attrition = "Yes" if random.random() < attrition_prob else "No"

    if attrition == "Yes":
        if overtime == "Yes": reason = "Work-Life Balance"
        elif salary < 45000: reason = "Low Salary"
        elif promotion == "Not Promoted" and years > 3: reason = "Lack of Growth"
        elif satisfaction < 4: reason = "Manager Conflict"
        else: reason = random.choice(attrition_reasons[:-1])
    else:
        reason = "N/A"

    records.append([
        emp_id, name, age, gender, dept, role, edu, marital, years,
        salary, perf, satisfaction, wlb, training_hours,
        promotion, overtime, attrition, reason, mgr_rating, engagement
    ])

columns = [
    "Employee_ID", "Employee_Name", "Age", "Gender", "Department", "Job_Role",
    "Education_Level", "Marital_Status", "Years_at_Company", "Monthly_Income",
    "Performance_Rating", "Job_Satisfaction_Score", "Work_Life_Balance_Score",
    "Training_Hours", "Promotion_Status", "Overtime_Status",
    "Attrition_Status", "Attrition_Reason", "Manager_Rating",
    "Employee_Engagement_Score"
]

df = pd.DataFrame(records, columns=columns)

# ─────────────────────────────────────────────────────────────────────────────
# 2. DATA CLEANING
# ─────────────────────────────────────────────────────────────────────────────
df.drop_duplicates(subset=["Employee_ID"], inplace=True)
df["Attrition_Binary"] = df["Attrition_Status"].map({"Yes": 1, "No": 0})
df["Monthly_Income"] = df["Monthly_Income"].clip(lower=0)
df = df.reset_index(drop=True)

# ─────────────────────────────────────────────────────────────────────────────
# 3. KPI CALCULATIONS
# ─────────────────────────────────────────────────────────────────────────────
total_employees = len(df)
attrition_count = df["Attrition_Binary"].sum()
attrition_rate = round((attrition_count / total_employees) * 100, 1)
retention_rate = round(100 - attrition_rate, 1)
avg_tenure = round(df["Years_at_Company"].mean(), 1)
avg_salary = int(df["Monthly_Income"].mean())
avg_satisfaction = round(df["Job_Satisfaction_Score"].mean(), 1)
avg_engagement = round(df["Employee_Engagement_Score"].mean(), 1)
promotion_rate = round((df["Promotion_Status"] == "Promoted").mean() * 100, 1)
overtime_rate = round((df["Overtime_Status"] == "Yes").mean() * 100, 1)
training_participation = round((df["Training_Hours"] > 0).mean() * 100, 1)

print("=" * 60)
print("EMPLOYEE ATTRITION & HR ANALYTICS DASHBOARD")
print("Key Performance Indicators — 2024")
print("=" * 60)
print(f"  Total Employees         : {total_employees}")
print(f"  Attrition Count         : {attrition_count}")
print(f"  Attrition Rate          : {attrition_rate}%")
print(f"  Retention Rate          : {retention_rate}%")
print(f"  Avg Tenure (Years)      : {avg_tenure}")
print(f"  Avg Monthly Income ($)  : ${avg_salary:,}")
print(f"  Avg Satisfaction Score  : {avg_satisfaction}/10")
print(f"  Avg Engagement Score    : {avg_engagement}/10")
print(f"  Promotion Rate          : {promotion_rate}%")
print(f"  Overtime Rate           : {overtime_rate}%")
print(f"  Training Participation  : {training_participation}%")
print()

# ─────────────────────────────────────────────────────────────────────────────
# 4. DEPARTMENT-WISE ATTRITION ANALYSIS
# ─────────────────────────────────────────────────────────────────────────────
dept_analysis = df.groupby("Department").agg(
    Total_Employees=("Employee_ID", "count"),
    Attrition_Count=("Attrition_Binary", "sum"),
    Avg_Salary=("Monthly_Income", "mean"),
    Avg_Satisfaction=("Job_Satisfaction_Score", "mean"),
    Avg_Engagement=("Employee_Engagement_Score", "mean"),
    Avg_Tenure=("Years_at_Company", "mean"),
    Overtime_Count=("Overtime_Status", lambda x: (x == "Yes").sum()),
).reset_index()
dept_analysis["Attrition_Rate_%"] = round(
    dept_analysis["Attrition_Count"] / dept_analysis["Total_Employees"] * 100, 1)
dept_analysis["Avg_Salary"] = dept_analysis["Avg_Salary"].round(0).astype(int)
dept_analysis["Avg_Satisfaction"] = dept_analysis["Avg_Satisfaction"].round(1)
dept_analysis["Avg_Engagement"] = dept_analysis["Avg_Engagement"].round(1)
dept_analysis["Avg_Tenure"] = dept_analysis["Avg_Tenure"].round(1)

print("Department-wise Attrition Analysis:")
print(dept_analysis[["Department", "Total_Employees", "Attrition_Count",
                       "Attrition_Rate_%", "Avg_Salary", "Avg_Satisfaction"]].to_string(index=False))
print()

# ─────────────────────────────────────────────────────────────────────────────
# 5. ATTRITION REASON ANALYSIS
# ─────────────────────────────────────────────────────────────────────────────
attrition_df = df[df["Attrition_Status"] == "Yes"]
reason_counts = attrition_df["Attrition_Reason"].value_counts().reset_index()
reason_counts.columns = ["Attrition_Reason", "Count"]
reason_counts["Percentage_%"] = round(reason_counts["Count"] / attrition_count * 100, 1)

print("Attrition Reasons Breakdown:")
print(reason_counts.to_string(index=False))
print()

# ─────────────────────────────────────────────────────────────────────────────
# 6. HIGH-RISK EMPLOYEE IDENTIFICATION
# ─────────────────────────────────────────────────────────────────────────────
df["Risk_Score"] = 0
df.loc[df["Job_Satisfaction_Score"] < 5, "Risk_Score"] += 2
df.loc[df["Employee_Engagement_Score"] < 5, "Risk_Score"] += 2
df.loc[df["Overtime_Status"] == "Yes", "Risk_Score"] += 1
df.loc[df["Promotion_Status"] == "Not Promoted", "Risk_Score"] += 1
df.loc[df["Manager_Rating"] <= 2, "Risk_Score"] += 2
df.loc[df["Work_Life_Balance_Score"] <= 2, "Risk_Score"] += 2
df["Risk_Category"] = pd.cut(
    df["Risk_Score"], bins=[-1, 2, 4, 10],
    labels=["Low Risk", "Medium Risk", "High Risk"]
)

high_risk = df[df["Risk_Category"] == "High Risk"][
    ["Employee_ID", "Employee_Name", "Department", "Job_Satisfaction_Score",
     "Overtime_Status", "Promotion_Status", "Risk_Score"]
].sort_values("Risk_Score", ascending=False).head(15)

print(f"High-Risk Employees (Top 15 of {(df['Risk_Category']=='High Risk').sum()}):")
print(high_risk.to_string(index=False))
print()

# ─────────────────────────────────────────────────────────────────────────────
# 7. SAVE OUTPUTS
# ─────────────────────────────────────────────────────────────────────────────
os.makedirs("outputs", exist_ok=True)
df.to_csv("outputs/hr_attrition_dataset.csv", index=False)
dept_analysis.to_csv("outputs/department_analysis.csv", index=False)
reason_counts.to_csv("outputs/attrition_reasons.csv", index=False)
high_risk.to_csv("outputs/high_risk_employees.csv", index=False)

print("✅ All datasets saved to outputs/ folder.")

# Export KPIs for use by dashboard and Excel scripts
kpis = {
    "total_employees": total_employees,
    "attrition_count": int(attrition_count),
    "attrition_rate": attrition_rate,
    "retention_rate": retention_rate,
    "avg_tenure": avg_tenure,
    "avg_salary": avg_salary,
    "avg_satisfaction": avg_satisfaction,
    "avg_engagement": avg_engagement,
    "promotion_rate": promotion_rate,
    "overtime_rate": overtime_rate,
    "training_participation": training_participation,
}

import json
with open("outputs/kpis.json", "w") as f:
    json.dump(kpis, f, indent=2)

print("✅ KPIs saved to outputs/kpis.json")
