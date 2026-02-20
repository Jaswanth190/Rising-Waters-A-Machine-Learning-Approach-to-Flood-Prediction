import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
dataset = pd.read_excel(r"C:\Users\jaswa\OneDrive\Desktop\flood project\dataset\flood dataset.xlsx")
print(dataset.head())
print(dataset.info())
print(dataset.describe().T)