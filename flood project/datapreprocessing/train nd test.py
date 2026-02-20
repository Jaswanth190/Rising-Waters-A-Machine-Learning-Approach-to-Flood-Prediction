import pandas as pd
import numpy as np
try:
    import matplotlib.pyplot as plt
except ImportError:
    print("matplotlib not installed. Install with: pip install matplotlib")
    plt = None
from sklearn.model_selection import train_test_split


dataset = pd.read_excel(
    r"C:\Users\jaswa\OneDrive\Desktop\flood project\dataset\flood dataset.xlsx"
)
x=dataset.iloc[:,2:7].values
y=dataset.iloc[:,10:].values
x_train, x_test, y_train, y_test = train_test_split(x,y,test_size=0.2,random_state=0)
targetvariablename=dataset['flood']
print(targetvariablename)
print(x_train)
print(x_test)
print(y_train)
print(y_test)