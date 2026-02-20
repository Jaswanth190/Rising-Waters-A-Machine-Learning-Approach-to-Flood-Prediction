# 🌊 Rising Waters: A Machine Learning Approach to Flood Prediction

## 📌 Project Overview

**Rising Waters** is a machine learning-based flood prediction system that analyzes environmental factors such as rainfall distribution and cloud cover to estimate the possibility of severe flooding.

The project follows a structured ML workflow implemented across modular Python scripts and integrates the trained model into a Flask web application for real-time prediction.

The system architecture includes:

* Dataset Collection
* Exploratory Data Analysis (EDA)
* Data Preprocessing
* Feature Scaling
* Train-Test Splitting
* Model Training (Multiple Regressors)
* Model Saving
* Flask-Based Deployment

---

# 🎯 Project Objectives

* Build a supervised ML-based flood prediction system.
* Perform structured exploratory data analysis.
* Preprocess and scale numerical environmental features.
* Train multiple regression models.
* Compare model performance.
* Deploy the trained model using Flask.
* Enable real-time prediction via web interface.

---

# 🏗️ Technical Architecture

## Machine Learning Pipeline

1. Dataset Loading (Excel format)
2. Descriptive Analysis
3. Univariate & Multivariate Analysis
4. Missing Value Handling
5. Feature Selection
6. Feature Scaling (StandardScaler)
7. Train-Test Split
8. Model Training (4 Regressors)
9. Model Saving using Joblib
10. Flask Deployment

---

# 📂 Project Structure

```
FLOOD PROJECT
│
├── dataset/
│   └── flood dataset.xlsx
│
├── datapreprocessing/
│   ├── datapreprocessing.py
│   ├── feature_scaling.py
│   ├── split_dataset.py
│   └── train nd test.py
│
├── v and a/
│   ├── descriptive analysis.py
│   ├── v and a.py
│   ├── h.py
│   ├── heatmap.png
│   ├── temperature.png
│   ├── temp boxplot.png
│   └── Figure_1.png
│
├── model training/
│   ├── flood.ipynb
│   └── flood.save
│
├── flask/
│   ├── static/
│   │   └── flood_bg.jpeg
│   ├── app.py
│   ├── flood_model.joblib
│   ├── flood_scaler.joblib
│   ├── flood.save
│   └── transform.save
│
└── .venv / .vscode
```

---

# 🧰 Prerequisites

## Software Required

* Python 3.x
* VS Code / PyCharm

## Required Python Packages

```bash
pip install numpy
pip install pandas
pip install scikit-learn
pip install matplotlib
pip install seaborn
pip install flask
pip install joblib
pip install xgboost
```

---

# 📊 Dataset

* Dataset: `flood dataset.xlsx`
* Format: Excel
* Features extracted using:

```python
dataset.iloc[:, 2:7]
```

* Target variable extracted using:

```python
dataset.iloc[:, 10]
```

The dataset includes rainfall distribution, cloud cover, and flood indicator features.

---

# 📈 Milestone 1: Exploratory Data Analysis (EDA)

EDA is implemented inside:

```
v and a/
```

### Performed Analysis:

* Dataset summary (`info()`, `describe()`)
* Null value checking
* Histogram plots
* Boxplots
* Correlation heatmap

Libraries used:

* Pandas
* NumPy
* Matplotlib
* Seaborn

---

# 🧹 Milestone 2: Data Preprocessing

Implemented inside:

```
datapreprocessing/
```

### Steps Performed:

* Handling missing values using:

  ```python
  dataset.fillna(dataset.mean(), inplace=True)
  ```
* Feature selection (`X = dataset.iloc[:,2:7]`)
* Target extraction
* Feature scaling using `StandardScaler`
* Train-test split using:

  ```python
  train_test_split(test_size=0.2, random_state=0)
  ```

Scaler saved using:

```python
dump(sc, "transform.save")
```

---

# 🤖 Milestone 3: Model Building

Implemented inside:

```
train nd test.py
```

### Models Used (Regression-Based)

* DecisionTreeRegressor
* RandomForestRegressor
* KNeighborsRegressor
* XGBRegressor (XGBoost)

All models were trained on scaled features.

Example:

```python
dtree.fit(X_train, y_train)
Rf.fit(X_train, y_train)
knn.fit(X_train, y_train)
xgb_model.fit(X_train, y_train)
```

---

# 💾 Model Saving

Final trained model saved as:

```
flood_model.joblib
```

Scaler saved as:

```
flood_scaler.joblib
```

These are stored inside:

```
flask/
```

---

# 🌐 Flask Web Application

Location:

```
flask/app.py
```

The application uses:

* `Flask`
* `joblib`
* `StandardScaler`
* `render_template_string` (inline HTML)

---

## 🔹 Key Functionalities

* Load trained model (`flood_model.joblib`)
* Load trained scaler (`flood_scaler.joblib`)
* Accept user inputs via POST
* Scale input values
* Perform prediction
* Display dynamic result

---

## 🔹 Input Features in Web App

Users enter:

* Cloud Cover
* Annual Rainfall
* Jan–Feb Rainfall
* Mar–May Rainfall
* Jun–Sep Rainfall

Prediction flow:

```
User Input
    ↓
Convert to float
    ↓
Scaler.transform()
    ↓
Model.predict()
    ↓
Display Result
```

If model output indicates flood risk:

* "Possibility of Severe Flood"

Else:

* "No Severe Flood Expected"

---

# 🚀 Running the Application

1. Open terminal
2. Navigate to:

```
flask/
```

3. Run:

```bash
python app.py
```

4. Open:

```
http://127.0.0.1:5000/
```

---

# 🧠 Technologies Used

### Programming

* Python

### Data Handling

* Pandas
* NumPy

### Visualization

* Matplotlib
* Seaborn

### Machine Learning

* Scikit-learn
* XGBoost
* StandardScaler
* train_test_split

### Model Serialization

* Joblib

### Deployment

* Flask
* HTML + CSS (inline inside Python)

---

# 🔮 Future Enhancements

* Convert regression output into flood risk probability score
* Move inline HTML into `templates/` folder
* Add performance comparison dashboard
* Deploy on cloud platform
* Add real-time rainfall API integration
* Implement alert notification system

---

# 📌 Conclusion

This project implements a complete end-to-end machine learning pipeline:

* Data Exploration
* Data Cleaning
* Feature Scaling
* Regression Model Training
* Model Saving
* Web Deployment

The system demonstrates practical integration of machine learning and web development to build a functional flood risk prediction prototype.

---
