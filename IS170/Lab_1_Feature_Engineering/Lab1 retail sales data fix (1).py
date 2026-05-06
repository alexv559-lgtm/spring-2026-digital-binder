import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder
df= pd.read_csv("retailsales.csv")
df1=df.copy()
df1.dropna(inplace=True)
le= LabelEncoder()
label = le.fit_transform(df1['Discount Applied'])
df1.drop('Discount Applied', axis=1, inplace=True)
df1['Discount Applied'] =label
print(df1)

