# Q1. Sales Data Analysis (2D Arrays + Properties + Filtering)
# --------------------------------
# A store recorded weekly sales (in thousands) for 4 products over 5 weeks:

#     Week1  Week2  Week3  Week4  Week5
# P1    12     15     11     18     14
# P2     9     10     13     12     16
# P3    20     18     22     19     21
# P4     7      8      6     10      9

import numpy as np

# 1. Create a 2D NumPy array named sales with the data above.

sales = np.array([
        [12, 15, 11, 18, 14],
        [9, 10, 13, 12, 16],
        [20, 18, 22, 19, 21],
        [7, 8, 6, 10, 9]
])

# 2. Print the shape, number of dimensions (ndim), and total number of elements (size).

print(f"Shape of array\n{sales.shape}")
print(f"Dimension of the array\n{sales.ndim}")
print(f"Size of the array\n{sales.size}")

# 3. Print the sales of Product 3 for all weeks.

print(f"Sales of Product 3 for all weeks\n{sales[3]}")

# Print the sales of all products in Week 4.

print(f"sales of all products in Week 4\n{sales[:, 4]}")

# 5. Find and print all sales values that are greater than 15.

print(f" All sales values that are greater than 15\n{sales[sales > 15]}")

# 6. Find and print the total sales and average sales of the entire store.

print(f"Total sales\n{np.sum(sales)}")
print(f"Average sales\n{np.mean(sales)}")


# Q2. Temperature Records (Slicing + Arithmetic + Functions)
# --------------------------------
# Daily temperatures (in °C) for 14 days are:

#     [28, 30, 29, 31, 33, 32, 30, 29, 27, 26, 28, 31, 34, 33]


import numpy as np 

temps = np.array([28, 30, 29, 31, 33, 32, 30, 29, 27, 26, 28, 31, 34, 33])

# 1. Create a 1D NumPy array named temps.

print(f"1D array\n{temps}")

# temperatures of the first week (first 7 days)

print(f"Temprature of first 7 days\n{temps[0:7]}")

# temperatures of the second week (last 7 days)

print(f"Temprature of last 7 days\n{temps[7::]}")

# every alternate day temperature (starting from day 1)

print(f"Tempratures of alternate days \n{temps[0::2]}")

# 3. Convert all temperatures from Celsius to Fahrenheit using the formula:

fahrenheit = np.array([])

fahrenheit = (temps * 9/5) + 32

print(f"Temprature in fahrenheit \n{fahrenheit}")

# 4. Print the highest, lowest, and average temperature in Celsius.

print(f"Highest Temprature \n{np.max(temps)}\nLowest Temprature \n{np.min(temps)}\nAverage Temprature  \n{np.mean(temps)}")

# 5. Print how many days had temperature above the average.

print(f"Above average temprature recorded  \n{temps[np.mean(temps)>temps]}")




# Q3. Matrix Operations (Element-wise vs Matrix Multiplication)
# --------------------------------
# Given:

#     A = [[2, 4],
#          [1, 3]]

#     B = [[5, 1],
#          [2, 6]]

import numpy as np

# 1. Create NumPy arrays A and B.

matrix_a = np.array([
    [2, 4],
    [1, 3]
])

matrix_b = np.array([
    [5, 1],
    [2, 6]
])

# 2. Print the element-wise multiplication of A and B (use *).

print(f"Element wise multiplication \n{matrix_a * matrix_b}")

# 3. Print the matrix multiplication of A and B (using @).

print(f"Matrix multiplication using @ \n{matrix_a @ matrix_b}")

# 3. Print the matrix multiplication of A and B (using np.dot).

print(f"Matrix multiplication using np.dot\n{np.dot(matrix_a, matrix_b)}")        # I see no differnce in results

# 5. Create a 1D array x = [2, 3, 4] and y = [1, 0, 2].

x = np.array([2, 3, 4])  

y = np.array([1, 0, 2])

# - x * y

print(f"x * y\n{x * y}")

# - np.dot(x, y)

print(f"Matrix multiplications\n{np.dot(x, y)}")       #matrix multiplication