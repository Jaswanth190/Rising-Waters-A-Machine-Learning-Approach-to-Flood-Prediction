import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


dataset = pd.read_excel(
    r"C:\Users\jaswa\OneDrive\Desktop\flood project\dataset\flood dataset.xlsx"
)

fig=plt.gcf()

fig.set_size_inches(15,15)

fig=sns.heatmap(dataset.corr(), annot=True, cmap='summer',linewidths=1,linecolor='k', square=True,mask=False, vmin=-1, vmax=1,cbar_kws={"orientation": "vertical"}, cbar=True)
plt.show()
plt.savefig('heatmap.png', dpi=300)