import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import StandardScaler
from joblib import dump

dataset = pd.read_excel(
    r"C:\Users\jaswa\OneDrive\Desktop\flood project\dataset\flood dataset.xlsx"
)

x=dataset.iloc[:,2:7].values
y=dataset.iloc[:,10:].values
print(x)
print(y)
sc=StandardScaler()
x_train=sc.fit_transform(x)
x_test=sc.fit_transform(y)
dump(sc,"transform.save")
print(x_train)
print(x_test)