from flask import Flask, request, render_template_string
import joblib
import numpy as np

app = Flask(__name__)

# Load model and scaler
model = joblib.load(r'Flask/flood_model.joblib')
scaler = joblib.load(r'Flask/flood_scaler.joblib')

# ---------------- HOME PAGE ----------------
HOME_HTML = r"""
<!DOCTYPE html>
<html>
<head>
    <title>Flood Prediction System</title>
    <style>
        body { 
            margin: 0; 
            font-family: Arial, sans-serif; 
            background: #f4f6f9;
        }

        /* Navbar */
        .navbar {
            background: black;
            padding: 15px 40px;
            display: flex;
            justify-content: space-between;
            align-items: center;
        }

        .navbar h1 { 
            color: #00ff00; 
            margin: 0; 
        }

        .navbar a {
            color: white;
            margin-left: 25px;
            text-decoration: none;
            font-weight: bold;
        }

        .navbar a:hover {
            color: #00ff00;
        }

        /* Hero Section */
        .hero {
            background: linear-gradient(rgba(0,0,0,0.6), rgba(0,0,0,0.6)),
                        url('/static/flood_bg.jpeg') no-repeat center center/cover;
            height: 500px;
            display: flex;
            justify-content: center;
            align-items: center;
            text-align: center;
            color: white;
        }

        .hero-content {
            max-width: 800px;
        }

        .hero h2 {
            font-size: 40px;
            margin-bottom: 20px;
            color: #00ff00;
        }

        .hero p {
            font-size: 18px;
            line-height: 1.6;
        }

        .cta-btn {
            margin-top: 30px;
            padding: 12px 30px;
            font-size: 16px;
            border: none;
            border-radius: 5px;
            background: #00ff00;
            color: black;
            cursor: pointer;
            font-weight: bold;
            text-decoration: none;
        }

        .cta-btn:hover {
            background: #00cc00;
        }

        /* Features Section */
        .features {
            padding: 60px 10%;
            text-align: center;
            background: white;
        }

        .features h3 {
            margin-bottom: 40px;
            font-size: 28px;
        }

        .feature-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
            gap: 30px;
        }

        .feature-box {
            padding: 25px;
            background: #f0f2f5;
            border-radius: 8px;
            box-shadow: 0 4px 8px rgba(0,0,0,0.1);
        }

        .feature-box h4 {
            color: #00aa00;
        }

        footer {
            background: black;
            color: white;
            text-align: center;
            padding: 15px;
        }
    </style>
</head>
<body>

<div class="navbar">
    <h1>Flood Prediction</h1>
    <div>
        <a href="/">Home</a>
        <a href="/predict">Predict</a>
    </div>
</div>

<div class="hero">
    <div class="hero-content">
        <h2>AI-Based Flood Prediction System</h2>
        <p>
            This system leverages Machine Learning algorithms to analyze rainfall patterns,
            cloud cover, and seasonal data to predict the possibility of severe flooding.
            Early predictions help in disaster preparedness and risk mitigation.
        </p>
        <a href="/predict" class="cta-btn">Start Prediction</a>
    </div>
</div>

<div class="features">
    <h3>System Features</h3>
    <div class="feature-grid">
        <div class="feature-box">
            <h4>Machine Learning Powered</h4>
            <p>Uses Random Forest model for accurate flood classification.</p>
        </div>
        <div class="feature-box">
            <h4>Real-Time Prediction</h4>
            <p>Instant flood risk analysis based on user inputs.</p>
        </div>
        <div class="feature-box">
            <h4>Disaster Prevention</h4>
            <p>Supports early warning and planning for flood-prone regions.</p>
        </div>
    </div>
</div>

<footer>
    © 2026 Flood Prediction System | AI & ML Project
</footer>

</body>
</html>
"""

# ---------------- PREDICT PAGE ----------------
PREDICT_HTML = """
<!DOCTYPE html>
<html>
<head>
    <title>Predict Flood</title>
    <style>
        body { 
            margin: 0; 
            font-family: Arial; 
            background: #e6e4dc; 
            display: flex;
            flex-direction: column;
            min-height: 100vh;
        }

        .navbar {
            background: black;
            padding: 15px 40px;
            display: flex;
            justify-content: space-between;
        }

        .navbar h1 { color: #00ff00; margin: 0; }
        .navbar a { color: white; text-decoration: none; }

        .container {
            flex: 1;
            display: flex;
            justify-content: center;
            align-items: center;
        }

        form {
            background: white;
            padding: 40px;
            border-radius: 10px;
            width: 400px;
            box-shadow: 0 5px 15px rgba(0,0,0,0.2);
        }

        label { margin-top: 15px; display: block; }

        input {
            width: 100%;
            padding: 10px;
            margin-top: 5px;
            border-radius: 5px;
            border: 1px solid #ccc;
        }

        button {
            width: 100%;
            margin-top: 25px;
            padding: 12px;
            border: none;
            background: #00ff00;
            font-weight: bold;
            cursor: pointer;
            border-radius: 5px;
        }

        button:hover {
            background: #00cc00;
        }
    </style>
</head>
<body>

<div class="navbar">
    <h1>Flood Prediction</h1>
    <a href="/">Home</a>
</div>

<div class="container">
<form method="POST">
    <label>Cloud Cover</label>
    <input name="cloud" required>

    <label>Annual Rain Fall</label>
    <input name="annual" required>

    <label>Jan-Feb Rainfall</label>
    <input name="janfeb" required>

    <label>March-May Rainfall</label>
    <input name="marmay" required>

    <label>June-September Rainfall</label>
    <input name="junsep" required>

    <button type="submit">Predict</button>
</form>
</div>

</body>
</html>
"""

# ---------------- RESULT PAGE ----------------
RESULT_HTML = """
<!DOCTYPE html>
<html>
<head>
    <title>Result</title>
    <style>
        body { margin: 0; font-family: Arial; background: #e6e4dc; }
        .navbar {
            background: black;
            padding: 15px 40px;
            display: flex;
            justify-content: space-between;
        }
        .navbar h1 { color: #00ff00; margin: 0; }
        .navbar a { color: white; text-decoration: none; margin-left: 20px; }

        .result {
            text-align: center;
            margin-top: 120px;
            font-size: 26px;
            font-weight: bold;
        }

        .danger { color: red; }
        .safe { color: green; }
    </style>
</head>
<body>

<div class="navbar">
    <h1>Flood Prediction</h1>
    <div>
        <a href="/">Home</a>
        <a href="/predict">Predict</a>
    </div>
</div>

<div class="result">
    <p class="{{ 'danger' if 'Severe' in message else 'safe' }}">
        {{ message }}
    </p>
</div>

</body>
</html>
"""

# ---------------- ROUTES ----------------
@app.route('/')
def home():
    return render_template_string(HOME_HTML)

@app.route('/predict', methods=['GET', 'POST'])
def predict():
    if request.method == 'POST':
        data = [
            float(request.form['cloud']),
            float(request.form['annual']),
            float(request.form['janfeb']),
            float(request.form['marmay']),
            float(request.form['junsep'])
        ]

        data = scaler.transform([data])
        prediction = model.predict(data)[0]

        message = "Possibility of Severe Flood" if prediction == 1 else "No Severe Flood Expected"
        return render_template_string(RESULT_HTML, message=message)

    return render_template_string(PREDICT_HTML)

if __name__ == '__main__':
    app.run(debug=True)