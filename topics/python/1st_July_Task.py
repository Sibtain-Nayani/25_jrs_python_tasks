import numpy as np
import pandas as pd
import random


### NUMPY:
print("##NUMPY##\n")

#Q1: Given a 2D NumPy array A of shape (5, 5), subtract the mean of each row from every element in that row without using a loop.

print("QUE 1:\n")

arr1 = np.arange(1,26).reshape(5,5)
print(arr1)
arr1 = arr1 - arr1.mean(axis=1, keepdims=True)
print(arr1,"\n") 

#Q2: You have a NumPy array of integers from 1 to 1000. Return a new array containing only the numbers that are divisible by both 3 and 7 but not by 5.

print("QUE 2:\n")

arr1000 = np.arange(1,1001)
arr37 = arr1000[(arr1000 %3 == 0) & (arr1000 %7 == 0) & (arr1000 %5!= 0)]

print(arr37,"\n")

#Q3: Create an 8x8 NumPy array with a chessboard pattern (alternating 0s and 1s), where the top-left element is 0.

print("QUE 3:\n")

arr88 = np.arange(0,64).reshape(8,8)
for i in arr88:
    for j in range(0,8):
        if(i[j]%2==0):
            i[j]=0
        else:
            i[j]=1
print(arr88,"\n")


### PANDAS:(Create a DataFrame with the specified columns and perform the operations)
print("##PANDAS##\n")

# Q1: Given a DataFrame df with columns: ["department", "employee", "salary"], normalize the salary within each department (i.e., for each department, subtract the mean and divide by the std of that department).

print("QUE 1:\n")

dataq1 = {
    "department":["IT","IT","IT","COMMS","COMMS"],
    "employee":["Raj","Rakesh","Siddhant","Pawar","Alex"],
    "salary":[30000,55000,42000,29000,34000]
    }

dfans1 = pd.DataFrame(dataq1)

dfans1["salary_Normal"] = dfans1.groupby("department")["salary"].transform(
    lambda x: (x - x.mean()) / x.std()
)

print(dfans1,"\n")


# Q2: Given a DataFrame with columns ["timestamp", "user_id", "action"], where timestamp is in string format, find the average number of actions per user per day.

print("QUE 2:\n")
dfans2 = pd.DataFrame({
    'timestamp': ['2025-07-01 10:00:00', '2025-07-01 11:00:00', '2025-07-01 12:00:00',
                  '2025-07-02 09:00:00', '2025-07-02 10:30:00'],
    'user_id': [1, 1, 2, 1, 2],
    'action': ['click', 'scroll', 'click', 'click', 'scroll']
})

dfans2['date'] = pd.to_datetime(dfans2['timestamp']).dt.date

apud = dfans2.groupby(['user_id', 'date']).size().reset_index(name='action_count')

avgapud = apud.groupby('user_id')['action_count'].mean().reset_index(name='avg_actions_per_day')
print(dfans2,"\n")
print(avgapud,"\n")


# Q3: You have a DataFrame with columns: ["user_id", "product", "price", "quantity", "date"]. Calculate the total amount spent by each user on "Laptop" purchases only, and return the result as a new DataFrame with columns: ["user_id", "total_spent_on_laptops"].

print("QUE 3:\n")

dfans3 = pd.DataFrame({
    'user_id': [1, 1, 2, 2, 3],
    'product': ['Laptop', 'Mouse', 'Laptop', 'Laptop', 'Keyboard'],
    'price': [50000, 800, 42000, 51000, 1300],
    'quantity': [1, 2, 1, 2, 1],
    'date': ['2025-07-01', '2025-07-01', '2025-07-01', '2025-07-02', '2025-07-02']
})

print(dfans3,"\n")

df_lap = dfans3[dfans3['product'] == 'Laptop'].copy()

df_lap['total_spent'] = df_lap['price'] * df_lap['quantity']

result = df_lap.groupby('user_id')['total_spent'].sum().reset_index()

result.rename(columns={'total_spent': 'total_spent_on_laptops'}, inplace=True)

print(result)

