# ASSIGNMENT 1: Student Performance Report

import pandas as pd
import numpy as np

# 1. Read the file "students.csv" into a DataFrame

df = pd.read_csv("students.csv")
print(df)

# 2. Add a new column "grade" based on marks

conditions = [
    df["marks"] >= 90,
    df["marks"] >= 80,
    df["marks"] >= 70,
]
choices = ["A", "B", "C"]
df["grade"] = np.select(conditions, choices, default="D")

print(df)

# 3. Filter: Delhi students with marks > 75

delhi_top = df[(df["city"] == "Delhi") & (df["marks"] > 75)]
print(delhi_top)

# 4. Statistical summary for "marks" column

print(df["marks"].describe())

# 5. Count of students in each grade

print(df["grade"].value_counts())
