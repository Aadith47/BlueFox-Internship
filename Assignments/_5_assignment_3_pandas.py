# ASSIGNMENT 3: Employee & Department Merge

import pandas as pd

# Create the two DataFrames

employees = pd.DataFrame({
    "emp_id": [101, 102, 103, 104, 105],
    "name": ["Ravi", "Anita", "Kiran", "Meera", "Arjun"],
    "dept_id": [1, 2, 1, 3, 2],
    },index = ["employee 1", "employee 2", "employee 3"])

departments = pd.DataFrame({
    "dept_id": [1, 2, 3, 4],
    "dept_name": ["IT", "HR", "Finance", "Marketing"],
    "location": ["Delhi", "Mumbai", "Chennai", "Bangalore"],
})

print(employees)
print(departments)

# # 1. LEFT join on employees and departments

# left_merged = pd.merge(employees, departments, on="dept_id", how="left")
# print(left_merged)

# # 2. OUTER join — identify unmatched rows

# outer_merged = pd.merge(employees, departments, on="dept_id", how="outer")
# print(outer_merged)

# # Employees with no matching department (name exists but dept_name is NaN)

# no_dept = outer_merged[outer_merged["dept_name"].isna()]

# if no_dept.empty:
#     print("All employees have a matching department.")

# else:
#     print("Employee(s) with no matching department:")
#     print(no_dept[["emp_id", "name"]])


# # Departments with no employees (dept_name exists but name is NaN)

# no_emp = outer_merged[outer_merged["name"].isna()]

# if no_emp.empty:
#     print("All departments have at least one employee.")

# else:
#     print("Department(s) with no employees:")
#     print(no_emp[["dept_id", "dept_name", "location"]])

# # 3. Fill missing department names with "Unknown"

# outer_filled = outer_merged.copy()
# outer_filled["dept_name"] = outer_filled["dept_name"].fillna("Unknown")
# print(outer_filled)


# #4. Count employees in each department (matched records only)

# emp_per_dept = left_merged.groupby("dept_name")["emp_id"].count()
# print(emp_per_dept)
