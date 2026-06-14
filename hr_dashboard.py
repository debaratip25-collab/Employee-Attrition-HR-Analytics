"""
Employee Attrition & HR Analytics Dashboard
Python Dashboard (Matplotlib/Seaborn)
======================================
Generates a professional multi-page dashboard with:
  - KPI Summary Cards
  - Attrition Analysis
  - Department Analysis
  - Workforce Demographics
  - Engagement & Satisfaction Analysis
  - Overtime & Promotion Analysis
  - Retention Opportunity Dashboard
"""

import pandas as pd
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import matplotlib.gridspec as gridspec
from matplotlib.patches import FancyBboxPatch
import warnings
import os
import json

warnings.filterwarnings("ignore")

# ── Load data ────────────────────────────────────────────────────────────────
df = pd.read_csv("outputs/hr_attrition_dataset.csv")
with open("outputs/kpis.json") as f:
    kpis = json.load(f)

dept_df = pd.read_csv("outputs/department_analysis.csv")
os.makedirs("outputs/dashboard", exist_ok=True)

# ── Color Palette ─────────────────────────────────────────────────────────────
PRIMARY     = "#1B3A6B"      # Deep navy
SECONDARY   = "#2E75B6"      # Corporate blue
ACCENT      = "#4CAF82"      # Teal green
WARNING     = "#E8923A"      # Amber
DANGER      = "#D63B3B"      # Red
LIGHT_BG    = "#F0F4FA"      # Light blue-grey
CARD_BG     = "#FFFFFF"
GRID_COLOR  = "#E8ECF2"
TEXT_DARK   = "#1B2A3B"
TEXT_MED    = "#4A5568"
TEXT_LIGHT  = "#8A9BB0"

ATT_COLOR   = DANGER
RET_COLOR   = ACCENT
DEPT_COLORS = ["#2E75B6","#4CAF82","#E8923A","#D63B3B","#7B5EA7","#4DD9D9","#E87F3A"]

def set_clean_ax(ax, title="", xlabel="", ylabel="", grid_axis="y"):
    ax.set_facecolor(LIGHT_BG)
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    ax.spines["left"].set_color(GRID_COLOR)
    ax.spines["bottom"].set_color(GRID_COLOR)
    ax.tick_params(colors=TEXT_MED, labelsize=8)
    if title:
        ax.set_title(title, fontsize=10, fontweight="bold", color=TEXT_DARK,
                     pad=8, loc="left")
    if xlabel: ax.set_xlabel(xlabel, fontsize=8, color=TEXT_MED)
    if ylabel: ax.set_ylabel(ylabel, fontsize=8, color=TEXT_MED)
    if grid_axis:
        ax.grid(axis=grid_axis, color=GRID_COLOR, linewidth=0.8, alpha=0.8)
        ax.set_axisbelow(True)

def kpi_card(ax, value, label, sublabel="", color=SECONDARY, icon=""):
    ax.set_xlim(0, 1); ax.set_ylim(0, 1)
    ax.axis("off")
    # Card background
    rect = FancyBboxPatch((0.04, 0.06), 0.92, 0.88,
                          boxstyle="round,pad=0.02",
                          linewidth=1.5, edgecolor=color,
                          facecolor=CARD_BG)
    ax.add_patch(rect)
    # Top accent bar
    accent = FancyBboxPatch((0.04, 0.82), 0.92, 0.12,
                            boxstyle="round,pad=0.0",
                            linewidth=0, facecolor=color, alpha=0.12)
    ax.add_patch(accent)
    ax.text(0.5, 0.88, label, ha="center", va="center",
            fontsize=7, color=color, fontweight="bold",
            transform=ax.transAxes)
    ax.text(0.5, 0.52, str(value), ha="center", va="center",
            fontsize=18, fontweight="bold", color=TEXT_DARK,
            transform=ax.transAxes)
    if sublabel:
        ax.text(0.5, 0.22, sublabel, ha="center", va="center",
                fontsize=7, color=TEXT_MED, transform=ax.transAxes)


# ══════════════════════════════════════════════════════════════════════════════
# PAGE 1 — KPI OVERVIEW + ATTRITION SUMMARY
# ══════════════════════════════════════════════════════════════════════════════
fig1 = plt.figure(figsize=(20, 13))
fig1.patch.set_facecolor(LIGHT_BG)

# ── Header banner ────────────────────────────────────────────────────────────
header = fig1.add_axes([0, 0.93, 1, 0.07])
header.set_facecolor(PRIMARY)
header.axis("off")
header.text(0.03, 0.55, "EMPLOYEE ATTRITION & HR ANALYTICS DASHBOARD",
            ha="left", va="center", fontsize=18, fontweight="bold",
            color="white", transform=header.transAxes)
header.text(0.97, 0.55,
            f"Data Period: Jan–Dec 2024  |  Total Employees: {kpis['total_employees']}  |  Prepared: June 2025",
            ha="right", va="center", fontsize=9, color="#B8D4F0",
            transform=header.transAxes)

# ── KPI Cards row ─────────────────────────────────────────────────────────────
kpi_data = [
    (f"{kpis['total_employees']}", "TOTAL EMPLOYEES", "120 Active Records", SECONDARY),
    (f"{kpis['attrition_rate']}%", "ATTRITION RATE", f"{kpis['attrition_count']} Employees Left", DANGER),
    (f"{kpis['retention_rate']}%", "RETENTION RATE", "Active Workforce", ACCENT),
    (f"{kpis['avg_tenure']} Yrs", "AVG TENURE", "Avg Years at Company", WARNING),
    (f"${kpis['avg_salary']//1000}K", "AVG MONTHLY INCOME", "Across All Departments", "#7B5EA7"),
    (f"{kpis['avg_satisfaction']}/10", "AVG SATISFACTION", "Employee Survey Score", SECONDARY),
    (f"{kpis['avg_engagement']}/10", "AVG ENGAGEMENT", "Engagement Index", ACCENT),
    (f"{kpis['overtime_rate']}%", "OVERTIME RATE", "Staff on Overtime", WARNING),
    (f"{kpis['promotion_rate']}%", "PROMOTION RATE", "Staff Promoted in 2024", DANGER),
    (f"{kpis['training_participation']}%", "TRAINING PARTICIPATION", "Training Coverage", "#4DD9D9"),
]
for idx, (val, lbl, sub, clr) in enumerate(kpi_data):
    ax_c = fig1.add_axes([0.01 + idx * 0.098, 0.75, 0.092, 0.165])
    kpi_card(ax_c, val, lbl, sub, clr)

# ── Attrition by Department ───────────────────────────────────────────────────
ax1 = fig1.add_axes([0.02, 0.41, 0.30, 0.30])
set_clean_ax(ax1, "Attrition Rate by Department (%)")
depts = dept_df.sort_values("Attrition_Rate_%", ascending=True)
bars = ax1.barh(depts["Department"], depts["Attrition_Rate_%"],
                color=DEPT_COLORS[:len(depts)], height=0.6, edgecolor="white")
for bar, val in zip(bars, depts["Attrition_Rate_%"]):
    ax1.text(bar.get_width() + 0.4, bar.get_y() + bar.get_height() / 2,
             f"{val:.1f}%", va="center", fontsize=8, color=TEXT_DARK, fontweight="bold")
ax1.set_xlim(0, max(depts["Attrition_Rate_%"]) * 1.25)
ax1.axvline(kpis["attrition_rate"], color=DANGER, linestyle="--", linewidth=1.5, alpha=0.7)
ax1.text(kpis["attrition_rate"] + 0.2, -0.7,
         f"Avg {kpis['attrition_rate']}%", fontsize=7, color=DANGER)

# ── Attrition Reasons pie ─────────────────────────────────────────────────────
ax2 = fig1.add_axes([0.34, 0.41, 0.22, 0.30])
reasons = df[df["Attrition_Status"] == "Yes"]["Attrition_Reason"].value_counts()
colors_pie = [DANGER, WARNING, SECONDARY, ACCENT, "#7B5EA7"]
wedges, texts, autotexts = ax2.pie(
    reasons.values, labels=reasons.index,
    colors=colors_pie[:len(reasons)],
    autopct="%1.1f%%", startangle=140,
    pctdistance=0.75,
    textprops={"fontsize": 7, "color": TEXT_DARK},
    wedgeprops={"edgecolor": "white", "linewidth": 1.5}
)
for at in autotexts:
    at.set_fontsize(7)
    at.set_color("white")
    at.set_fontweight("bold")
ax2.set_title("Attrition Reasons Breakdown", fontsize=10,
              fontweight="bold", color=TEXT_DARK, pad=8, loc="left",
              x=-0.05)

# ── Attrition by Gender ───────────────────────────────────────────────────────
ax3 = fig1.add_axes([0.59, 0.41, 0.18, 0.30])
set_clean_ax(ax3, "Attrition by Gender", grid_axis="y")
gender_att = df.groupby("Gender")["Attrition_Binary"].agg(["sum", "count"])
gender_att["rate"] = gender_att["sum"] / gender_att["count"] * 100
bars3 = ax3.bar(gender_att.index, gender_att["rate"],
                color=[SECONDARY, ACCENT], width=0.5, edgecolor="white")
for b in bars3:
    ax3.text(b.get_x() + b.get_width() / 2, b.get_height() + 0.5,
             f"{b.get_height():.1f}%", ha="center", fontsize=9,
             fontweight="bold", color=TEXT_DARK)
ax3.set_ylabel("Attrition Rate %", fontsize=8, color=TEXT_MED)
ax3.set_ylim(0, 60)

# ── Attrition by Tenure ───────────────────────────────────────────────────────
ax4 = fig1.add_axes([0.80, 0.41, 0.18, 0.30])
set_clean_ax(ax4, "Attrition by Tenure", grid_axis="y")
df["Tenure_Band"] = pd.cut(df["Years_at_Company"], bins=[0,3,7,12,20],
                            labels=["0–3 Yrs", "4–7 Yrs", "8–12 Yrs", "13+ Yrs"])
tenure_att = df.groupby("Tenure_Band", observed=True)["Attrition_Binary"].agg(["sum","count"])
tenure_att["rate"] = tenure_att["sum"] / tenure_att["count"] * 100
ax4.bar(tenure_att.index, tenure_att["rate"],
        color=[DANGER, WARNING, SECONDARY, ACCENT], width=0.6, edgecolor="white")
for i, (idx, row) in enumerate(tenure_att.iterrows()):
    ax4.text(i, row["rate"] + 0.5, f"{row['rate']:.1f}%",
             ha="center", fontsize=8, fontweight="bold", color=TEXT_DARK)
ax4.set_ylabel("Attrition Rate %", fontsize=8, color=TEXT_MED)
ax4.set_ylim(0, 65)

# ── Attrition vs Overtime ─────────────────────────────────────────────────────
ax5 = fig1.add_axes([0.02, 0.05, 0.28, 0.28])
set_clean_ax(ax5, "Overtime vs Attrition", grid_axis="y")
ot = df.groupby(["Overtime_Status", "Attrition_Status"]).size().unstack(fill_value=0)
x = np.arange(len(ot.index))
w = 0.35
ax5.bar(x - w/2, ot.get("No", 0), w, label="Retained", color=RET_COLOR, edgecolor="white")
ax5.bar(x + w/2, ot.get("Yes", 0), w, label="Attrition", color=ATT_COLOR, edgecolor="white")
ax5.set_xticks(x)
ax5.set_xticklabels(["No Overtime", "Overtime"], fontsize=9)
ax5.legend(fontsize=8)
ax5.set_ylabel("# Employees", fontsize=8, color=TEXT_MED)

# ── Satisfaction vs Attrition scatter ─────────────────────────────────────────
ax6 = fig1.add_axes([0.36, 0.05, 0.28, 0.28])
set_clean_ax(ax6, "Satisfaction Score vs Attrition", grid_axis="both")
for status, grp in df.groupby("Attrition_Status"):
    color = ATT_COLOR if status == "Yes" else ACCENT
    ax6.scatter(grp["Job_Satisfaction_Score"], grp["Employee_Engagement_Score"],
                alpha=0.55, s=28, color=color, label=f"Attrition={status}")
ax6.set_xlabel("Job Satisfaction Score", fontsize=8, color=TEXT_MED)
ax6.set_ylabel("Engagement Score", fontsize=8, color=TEXT_MED)
ax6.legend(fontsize=8)

# ── Promotion vs Attrition ─────────────────────────────────────────────────────
ax7 = fig1.add_axes([0.70, 0.05, 0.28, 0.28])
set_clean_ax(ax7, "Promotion Status vs Attrition Rate (%)", grid_axis="y")
promo = df.groupby("Promotion_Status")["Attrition_Binary"].agg(["sum","count"])
promo["rate"] = promo["sum"] / promo["count"] * 100
bars7 = ax7.bar(promo.index, promo["rate"],
                color=[DANGER, ACCENT], width=0.45, edgecolor="white")
for b in bars7:
    ax7.text(b.get_x() + b.get_width() / 2, b.get_height() + 0.5,
             f"{b.get_height():.1f}%", ha="center", fontsize=10,
             fontweight="bold", color=TEXT_DARK)
ax7.set_ylabel("Attrition Rate %", fontsize=8, color=TEXT_MED)
ax7.set_ylim(0, 55)

plt.savefig("outputs/dashboard/Page1_KPI_Attrition_Overview.png",
            dpi=150, bbox_inches="tight", facecolor=LIGHT_BG)
plt.close(fig1)
print("✅ Page 1 saved: KPI Attrition Overview")


# ══════════════════════════════════════════════════════════════════════════════
# PAGE 2 — WORKFORCE DEMOGRAPHICS & DEPARTMENT DEEP DIVE
# ══════════════════════════════════════════════════════════════════════════════
fig2 = plt.figure(figsize=(20, 13))
fig2.patch.set_facecolor(LIGHT_BG)

header2 = fig2.add_axes([0, 0.93, 1, 0.07])
header2.set_facecolor(PRIMARY)
header2.axis("off")
header2.text(0.03, 0.55, "WORKFORCE DEMOGRAPHICS & DEPARTMENT ANALYSIS",
             ha="left", va="center", fontsize=18, fontweight="bold",
             color="white", transform=header2.transAxes)
header2.text(0.97, 0.55, "Employee Attrition & HR Analytics Dashboard | 2024",
             ha="right", va="center", fontsize=9, color="#B8D4F0",
             transform=header2.transAxes)

# ── Age Distribution ──────────────────────────────────────────────────────────
ax_age = fig2.add_axes([0.02, 0.61, 0.28, 0.28])
set_clean_ax(ax_age, "Age Distribution by Attrition Status", grid_axis="y")
for status, color in [("No", ACCENT), ("Yes", ATT_COLOR)]:
    sub = df[df["Attrition_Status"] == status]["Age"]
    ax_age.hist(sub, bins=15, alpha=0.65, color=color,
                label=f"Attrition={status}", edgecolor="white")
ax_age.set_xlabel("Age", fontsize=8, color=TEXT_MED)
ax_age.set_ylabel("# Employees", fontsize=8, color=TEXT_MED)
ax_age.legend(fontsize=8)

# ── Gender distribution donut ─────────────────────────────────────────────────
ax_gen = fig2.add_axes([0.33, 0.61, 0.18, 0.28])
gen_counts = df["Gender"].value_counts()
wedges, texts, autos = ax_gen.pie(
    gen_counts.values, labels=gen_counts.index,
    colors=[SECONDARY, ACCENT], autopct="%1.1f%%", startangle=90,
    pctdistance=0.75,
    wedgeprops={"edgecolor": "white", "linewidth": 2, "width": 0.55},
    textprops={"fontsize": 9, "color": TEXT_DARK}
)
for at in autos:
    at.set_fontsize(9)
    at.set_color("white")
    at.set_fontweight("bold")
ax_gen.set_title("Gender Distribution", fontsize=10, fontweight="bold",
                 color=TEXT_DARK, pad=8, loc="left", x=-0.15)

# ── Education level ───────────────────────────────────────────────────────────
ax_edu = fig2.add_axes([0.54, 0.61, 0.21, 0.28])
set_clean_ax(ax_edu, "Attrition by Education Level", grid_axis="y")
edu_att = df.groupby("Education_Level")["Attrition_Binary"].agg(["sum","count"])
edu_att["rate"] = edu_att["sum"] / edu_att["count"] * 100
edu_order = ["High School", "Bachelor's", "Master's", "PhD"]
edu_att = edu_att.reindex([e for e in edu_order if e in edu_att.index])
bars_edu = ax_edu.bar(range(len(edu_att)), edu_att["rate"],
                      color=DEPT_COLORS[:len(edu_att)], edgecolor="white")
ax_edu.set_xticks(range(len(edu_att)))
ax_edu.set_xticklabels(edu_att.index, fontsize=7)
for b in bars_edu:
    ax_edu.text(b.get_x() + b.get_width()/2, b.get_height() + 0.5,
                f"{b.get_height():.1f}%", ha="center", fontsize=8,
                fontweight="bold", color=TEXT_DARK)
ax_edu.set_ylabel("Attrition Rate %", fontsize=8, color=TEXT_MED)

# ── Marital Status ────────────────────────────────────────────────────────────
ax_mar = fig2.add_axes([0.78, 0.61, 0.20, 0.28])
set_clean_ax(ax_mar, "Attrition by Marital Status", grid_axis="y")
mar_att = df.groupby("Marital_Status")["Attrition_Binary"].agg(["sum","count"])
mar_att["rate"] = mar_att["sum"] / mar_att["count"] * 100
bars_mar = ax_mar.bar(mar_att.index, mar_att["rate"],
                      color=[DANGER, SECONDARY, WARNING], edgecolor="white")
for b in bars_mar:
    ax_mar.text(b.get_x() + b.get_width()/2, b.get_height() + 0.5,
                f"{b.get_height():.1f}%", ha="center", fontsize=9,
                fontweight="bold", color=TEXT_DARK)
ax_mar.set_ylabel("Attrition Rate %", fontsize=8, color=TEXT_MED)

# ── Department heatmap ─────────────────────────────────────────────────────────
ax_heat = fig2.add_axes([0.02, 0.26, 0.45, 0.28])
set_clean_ax(ax_heat, "Department Performance Heatmap", grid_axis="")
metrics = ["Attrition_Rate_%", "Avg_Satisfaction", "Avg_Engagement", "Avg_Tenure"]
heat_data = dept_df.set_index("Department")[metrics].astype(float)
heat_norm = (heat_data - heat_data.min()) / (heat_data.max() - heat_data.min())
im = ax_heat.imshow(heat_norm.values.T, cmap="RdYlGn_r", aspect="auto",
                    vmin=0, vmax=1)
ax_heat.set_xticks(range(len(heat_data.index)))
ax_heat.set_xticklabels(heat_data.index, fontsize=8)
ax_heat.set_yticks(range(len(metrics)))
ax_heat.set_yticklabels(["Attrition %", "Satisfaction", "Engagement", "Tenure"], fontsize=8)
for i in range(len(metrics)):
    for j in range(len(heat_data.index)):
        ax_heat.text(j, i, f"{heat_data.values[j][i]:.1f}",
                     ha="center", va="center", fontsize=8,
                     color="white", fontweight="bold")

# ── Salary by Department ──────────────────────────────────────────────────────
ax_sal = fig2.add_axes([0.53, 0.26, 0.45, 0.28])
set_clean_ax(ax_sal, "Average Monthly Income by Department ($)", grid_axis="y")
dept_sal = dept_df.sort_values("Avg_Salary", ascending=False)
bars_s = ax_sal.bar(dept_sal["Department"], dept_sal["Avg_Salary"],
                    color=DEPT_COLORS[:len(dept_sal)], edgecolor="white")
for b in bars_s:
    ax_sal.text(b.get_x() + b.get_width()/2, b.get_height() + 300,
                f"${b.get_height()/1000:.0f}K", ha="center", fontsize=8,
                fontweight="bold", color=TEXT_DARK)
ax_sal.set_ylabel("Monthly Income ($)", fontsize=8, color=TEXT_MED)

# ── Job Role attrition ─────────────────────────────────────────────────────────
ax_role = fig2.add_axes([0.02, 0.05, 0.45, 0.17])
set_clean_ax(ax_role, "Top 10 Job Roles by Attrition Count", grid_axis="x")
role_att = df[df["Attrition_Status"] == "Yes"]["Job_Role"].value_counts().head(10)
ax_role.barh(role_att.index, role_att.values,
             color=SECONDARY, edgecolor="white", height=0.6)
for i, v in enumerate(role_att.values):
    ax_role.text(v + 0.1, i, str(v), va="center", fontsize=8, fontweight="bold", color=TEXT_DARK)

# ── Performance vs Attrition ──────────────────────────────────────────────────
ax_perf = fig2.add_axes([0.53, 0.05, 0.45, 0.17])
set_clean_ax(ax_perf, "Performance Rating vs Attrition Rate (%)", grid_axis="y")
perf_att = df.groupby("Performance_Rating")["Attrition_Binary"].agg(["sum","count"])
perf_att["rate"] = perf_att["sum"] / perf_att["count"] * 100
ax_perf.bar(perf_att.index, perf_att["rate"],
            color=[DANGER, WARNING, SECONDARY, ACCENT, "#7B5EA7"],
            edgecolor="white", width=0.6)
for i, (idx, row) in enumerate(perf_att.iterrows()):
    ax_perf.text(idx, row["rate"] + 0.5, f"{row['rate']:.1f}%",
                 ha="center", fontsize=8, fontweight="bold", color=TEXT_DARK)
ax_perf.set_xlabel("Performance Rating (1–5)", fontsize=8, color=TEXT_MED)
ax_perf.set_ylabel("Attrition Rate %", fontsize=8, color=TEXT_MED)
ax_perf.set_xticks([1, 2, 3, 4, 5])

plt.savefig("outputs/dashboard/Page2_Demographics_Department.png",
            dpi=150, bbox_inches="tight", facecolor=LIGHT_BG)
plt.close(fig2)
print("✅ Page 2 saved: Demographics & Department Analysis")


# ══════════════════════════════════════════════════════════════════════════════
# PAGE 3 — ENGAGEMENT, SATISFACTION & RETENTION OPPORTUNITIES
# ══════════════════════════════════════════════════════════════════════════════
fig3 = plt.figure(figsize=(20, 13))
fig3.patch.set_facecolor(LIGHT_BG)

header3 = fig3.add_axes([0, 0.93, 1, 0.07])
header3.set_facecolor(PRIMARY)
header3.axis("off")
header3.text(0.03, 0.55, "ENGAGEMENT, SATISFACTION & RETENTION OPPORTUNITY ANALYSIS",
             ha="left", va="center", fontsize=18, fontweight="bold",
             color="white", transform=header3.transAxes)
header3.text(0.97, 0.55, "Employee Attrition & HR Analytics Dashboard | 2024",
             ha="right", va="center", fontsize=9, color="#B8D4F0",
             transform=header3.transAxes)

# ── Engagement Distribution ───────────────────────────────────────────────────
ax_eng = fig3.add_axes([0.02, 0.61, 0.28, 0.28])
set_clean_ax(ax_eng, "Engagement Score Distribution by Attrition", grid_axis="y")
for status, color in [("No", ACCENT), ("Yes", ATT_COLOR)]:
    sub = df[df["Attrition_Status"] == status]["Employee_Engagement_Score"]
    ax_eng.hist(sub, bins=12, alpha=0.65, color=color,
                label=f"Attrition={status}", edgecolor="white")
ax_eng.axvline(df["Employee_Engagement_Score"].mean(), color=TEXT_MED,
               linestyle="--", linewidth=1.5, label="Avg")
ax_eng.set_xlabel("Engagement Score", fontsize=8, color=TEXT_MED)
ax_eng.set_ylabel("# Employees", fontsize=8, color=TEXT_MED)
ax_eng.legend(fontsize=8)

# ── Satisfaction by Dept ──────────────────────────────────────────────────────
ax_sat = fig3.add_axes([0.34, 0.61, 0.28, 0.28])
set_clean_ax(ax_sat, "Avg Satisfaction & Engagement by Department", grid_axis="y")
x_pos = np.arange(len(dept_df))
w = 0.35
ax_sat.bar(x_pos - w/2, dept_df["Avg_Satisfaction"], w,
           label="Satisfaction", color=SECONDARY, edgecolor="white")
ax_sat.bar(x_pos + w/2, dept_df["Avg_Engagement"], w,
           label="Engagement", color=ACCENT, edgecolor="white")
ax_sat.set_xticks(x_pos)
ax_sat.set_xticklabels(dept_df["Department"], fontsize=7, rotation=30, ha="right")
ax_sat.legend(fontsize=8)
ax_sat.set_ylim(0, 12)
ax_sat.axhline(6, color=DANGER, linestyle="--", linewidth=1, alpha=0.7)
ax_sat.text(6.2, 6.1, "Threshold 6.0", fontsize=7, color=DANGER)

# ── Training hours vs attrition ───────────────────────────────────────────────
ax_trn = fig3.add_axes([0.66, 0.61, 0.32, 0.28])
set_clean_ax(ax_trn, "Training Hours vs Attrition Rate", grid_axis="both")
df["Training_Band"] = pd.cut(df["Training_Hours"], bins=[0,10,20,30,40],
                              labels=["1–10 Hrs","11–20 Hrs","21–30 Hrs","31–40 Hrs"])
trn_att = df.groupby("Training_Band", observed=True)["Attrition_Binary"].agg(["sum","count"])
trn_att["rate"] = trn_att["sum"] / trn_att["count"] * 100
ax_trn.bar(range(len(trn_att)), trn_att["rate"],
           color=[DANGER, WARNING, SECONDARY, ACCENT], edgecolor="white")
ax_trn.set_xticks(range(len(trn_att)))
ax_trn.set_xticklabels(trn_att.index, fontsize=8)
for i, v in enumerate(trn_att["rate"]):
    ax_trn.text(i, v + 0.5, f"{v:.1f}%", ha="center", fontsize=8,
                fontweight="bold", color=TEXT_DARK)
ax_trn.set_ylabel("Attrition Rate %", fontsize=8, color=TEXT_MED)

# ── Manager rating vs attrition ───────────────────────────────────────────────
ax_mgr = fig3.add_axes([0.02, 0.32, 0.28, 0.25])
set_clean_ax(ax_mgr, "Manager Rating vs Attrition Rate (%)", grid_axis="y")
mgr_att = df.groupby("Manager_Rating")["Attrition_Binary"].agg(["sum","count"])
mgr_att["rate"] = mgr_att["sum"] / mgr_att["count"] * 100
ax_mgr.plot(mgr_att.index, mgr_att["rate"], "o-",
            color=DANGER, linewidth=2.5, markersize=8)
ax_mgr.fill_between(mgr_att.index, mgr_att["rate"], alpha=0.15, color=DANGER)
for x, y in zip(mgr_att.index, mgr_att["rate"]):
    ax_mgr.text(x, y + 1.2, f"{y:.1f}%", ha="center", fontsize=8,
                fontweight="bold", color=DANGER)
ax_mgr.set_xlabel("Manager Rating (1–5)", fontsize=8, color=TEXT_MED)
ax_mgr.set_ylabel("Attrition Rate %", fontsize=8, color=TEXT_MED)

# ── WLB vs attrition ─────────────────────────────────────────────────────────
ax_wlb = fig3.add_axes([0.36, 0.32, 0.28, 0.25])
set_clean_ax(ax_wlb, "Work-Life Balance vs Attrition Rate (%)", grid_axis="y")
wlb_att = df.groupby("Work_Life_Balance_Score")["Attrition_Binary"].agg(["sum","count"])
wlb_att["rate"] = wlb_att["sum"] / wlb_att["count"] * 100
ax_wlb.bar(wlb_att.index, wlb_att["rate"],
           color=DEPT_COLORS[:len(wlb_att)], edgecolor="white")
ax_wlb.set_xlabel("Work-Life Balance Score (1–5)", fontsize=8, color=TEXT_MED)
ax_wlb.set_ylabel("Attrition Rate %", fontsize=8, color=TEXT_MED)
for i, (idx, row) in enumerate(wlb_att.iterrows()):
    ax_wlb.text(idx, row["rate"] + 0.5, f"{row['rate']:.1f}%",
                ha="center", fontsize=8, fontweight="bold", color=TEXT_DARK)

# ── Risk Distribution ─────────────────────────────────────────────────────────
ax_risk = fig3.add_axes([0.69, 0.32, 0.29, 0.25])
set_clean_ax(ax_risk, "Employee Risk Category Distribution", grid_axis="y")
risk_counts = df["Risk_Category"].value_counts()
bars_r = ax_risk.bar(risk_counts.index, risk_counts.values,
                     color=[ACCENT, WARNING, DANGER], edgecolor="white")
for b in bars_r:
    ax_risk.text(b.get_x() + b.get_width()/2, b.get_height() + 0.5,
                 str(int(b.get_height())), ha="center", fontsize=10,
                 fontweight="bold", color=TEXT_DARK)
ax_risk.set_ylabel("# Employees", fontsize=8, color=TEXT_MED)

# ── Retention Opportunity Summary ─────────────────────────────────────────────
ax_ret = fig3.add_axes([0.02, 0.05, 0.96, 0.22])
ax_ret.set_facecolor(CARD_BG)
ax_ret.axis("off")

# Title
ax_ret.text(0.01, 0.92, "RETENTION OPPORTUNITY SUMMARY",
            fontsize=12, fontweight="bold", color=PRIMARY,
            transform=ax_ret.transAxes)

recommendations = [
    ("1", "Work-Life Balance Programs",
     "59.1% of attrition linked to WLB issues. Implement flexible work schedules, "
     "remote options and workload management policies."),
    ("2", "Promotion & Growth Pathways",
     "25.0% left due to lack of growth. Introduce structured career tracks, "
     "mentorship programs and transparent promotion criteria."),
    ("3", "Manager Effectiveness Training",
     "11.4% cited manager conflict. Deploy 360° feedback programs and "
     "leadership coaching for all people-managers."),
    ("4", "Legal & Marketing Retention Focus",
     "Both departments show 50% attrition rate — highest in portfolio. "
     "Conduct stay interviews and revise compensation benchmarks."),
    ("5", "Overtime Reduction Initiative",
     f"{kpis['overtime_rate']}% of workforce on overtime. "
     "Identify chronic overtime roles and right-size workload through hiring or automation."),
]
for i, (num, title, text) in enumerate(recommendations):
    x = 0.01 + i * 0.20
    rect = FancyBboxPatch((x, 0.05), 0.185, 0.78,
                          boxstyle="round,pad=0.02",
                          linewidth=1.5, edgecolor=SECONDARY,
                          facecolor=LIGHT_BG, transform=ax_ret.transAxes)
    ax_ret.add_patch(rect)
    ax_ret.text(x + 0.013, 0.74, f"#{num}", fontsize=10,
                fontweight="bold", color=SECONDARY, transform=ax_ret.transAxes)
    ax_ret.text(x + 0.013, 0.60, title, fontsize=8.5,
                fontweight="bold", color=TEXT_DARK, transform=ax_ret.transAxes)
    # Wrap text manually
    words = text.split()
    lines, line = [], []
    for word in words:
        line.append(word)
        if len(" ".join(line)) > 32:
            lines.append(" ".join(line[:-1]))
            line = [word]
    if line:
        lines.append(" ".join(line))
    for j, ln in enumerate(lines[:4]):
        ax_ret.text(x + 0.013, 0.46 - j * 0.10, ln, fontsize=7.5,
                    color=TEXT_MED, transform=ax_ret.transAxes)

plt.savefig("outputs/dashboard/Page3_Engagement_Retention.png",
            dpi=150, bbox_inches="tight", facecolor=LIGHT_BG)
plt.close(fig3)
print("✅ Page 3 saved: Engagement, Satisfaction & Retention")
print()
print("🎉 Dashboard complete! Files saved in outputs/dashboard/")
