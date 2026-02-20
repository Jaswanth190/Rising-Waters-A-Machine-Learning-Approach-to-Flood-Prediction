import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


dataset = pd.read_excel(
    r"C:\Users\jaswa\OneDrive\Desktop\flood project\dataset\flood dataset.xlsx"
)

sns.histplot(dataset['Temp'], kde=True)
plt.title("Temperature Distribution")
plt.show()
print(sns.boxplot(dataset["Temp"]))
plt.title("Temperature Boxplot")
plt.show()