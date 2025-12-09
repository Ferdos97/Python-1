# Data Analyses, ml, dl, ai
# numpy, pandas

import numpy as np
import pandas as pd

ar = np.array([[1, 2], [3, 4]])
# print(ar)


df = pd.DataFrame({
    'name': ['ali', 'reza', 'sara'],
    'age': [23, 24, 25],
    'weight': [75, 80, 90],
    'height': [180, 170, 165],
    'car': ['sia', '206', 'x']
})

print(df['height']/df['weight'])
print(df)
df.to_csv('students_data.csv')