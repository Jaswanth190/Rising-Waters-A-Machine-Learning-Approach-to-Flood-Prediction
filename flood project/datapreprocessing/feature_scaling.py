
import numpy as np
import pandas as pd
from sklearn import neighbors, tree, ensemble
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
import xgboost as xgb

# Load dataset
dataset = pd.read_excel(
    r"C:\Users\jaswa\OneDrive\Desktop\flood project\dataset\flood dataset.xlsx"
)

# Handle missing values
dataset.fillna(dataset.mean(numeric_only=True), inplace=True)

# Feature & target selection
X = dataset.iloc[:, 2:7].values
y = dataset.iloc[:, 10].values

# Feature scaling
scaler = StandardScaler()
X = scaler.fit_transform(X)

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=0
)

# Models
dtree = tree.DecisionTreeRegressor(random_state=0)
Rf = ensemble.RandomForestRegressor(n_estimators=100, random_state=0)
knn = neighbors.KNeighborsRegressor(n_neighbors=5)
xgb_model = xgb.XGBRegressor(use_label_encoder=False, eval_metric='logloss')

# Training
dtree.fit(X_train, y_train)
Rf.fit(X_train, y_train)
knn.fit(X_train, y_train)
xgb_model.fit(X_train, y_train)