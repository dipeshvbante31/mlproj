# 🔥 Algerian Forest Fire - FWI Prediction Web Application

A Machine Learning web application built using **Flask** that predicts the **Fire Weather Index (FWI)** based on weather conditions using a trained **Ridge Regression** model.

---

# 📌 Project Overview

This project deploys a trained Machine Learning model as a web application. Users can enter weather-related parameters through a simple HTML interface, and the application predicts the **Fire Weather Index (FWI)** in real time.

The project demonstrates the complete deployment workflow of a regression model, including model serialization, data preprocessing, Flask integration, and frontend development.

---

# 🚀 Features

- Predict Fire Weather Index (FWI)
- User-friendly web interface
- Machine Learning model deployment using Flask
- Data preprocessing with StandardScaler
- Ridge Regression prediction model
- Fast and lightweight application

---

# 📊 Input Features

The model uses the following input parameters:

| Feature | Description |
|----------|-------------|
| Temperature | Air Temperature |
| RH | Relative Humidity (%) |
| WS | Wind Speed |
| Rain | Rainfall |
| FFMC | Fine Fuel Moisture Code |
| DMC | Duff Moisture Code |
| ISI | Initial Spread Index |
| Classes | Fire / Not Fire |
| Region | Bejaia or Sidi-Bel Abbes |

---

# 🤖 Machine Learning Workflow

The project follows these steps:

1. Data Collection
2. Data Cleaning
3. Exploratory Data Analysis (EDA)
4. Feature Engineering
5. Feature Selection
6. Data Scaling using StandardScaler
7. Ridge Regression Model Training
8. Model Serialization using Pickle
9. Flask Deployment
10. Prediction through Web Interface

---

# 🛠️ Technologies Used

- Python
- Flask
- NumPy
- Pandas
- Scikit-learn
- Pickle
- HTML5
- CSS (Optional)

---

# 📂 Project Structure

```
Algerian-Forest-Fire/
│
├── app.py
├── requirements.txt
│
├── models/
│   ├── ridge.pkl
│   └── scaler.pkl
│
├── templates/
│   ├── index.html
│   └── home.html
│
├── static/
│
└── README.md
```

---

# ⚙️ Installation

Clone the repository

```bash
git clone https://github.com/your-username/Algerian-Forest-Fire.git
```

Move into the project directory

```bash
cd Algerian-Forest-Fire
```

Create a virtual environment

```bash
python -m venv venv
```

Activate the environment

### Windows

```bash
venv\Scripts\activate
```

### Linux / Mac

```bash
source venv/bin/activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

---

# ▶️ Run the Application

```bash
python app.py
```

Open your browser and visit

```
http://127.0.0.1:5000
```

---

# 📈 Prediction Workflow

```
User Input
      │
      ▼
HTML Form
      │
      ▼
Flask Application
      │
      ▼
StandardScaler
      │
      ▼
Ridge Regression Model
      │
      ▼
Predicted Fire Weather Index (FWI)
```

---

# 📊 Model Information

- Algorithm: Ridge Regression
- Problem Type: Regression
- Target Variable: Fire Weather Index (FWI)
- Preprocessing: StandardScaler
- Model Serialization: Pickle

---

# 💻 Example Inputs

| Feature | Example |
|----------|---------|
| Temperature | 30 |
| RH | 57 |
| WS | 18 |
| Rain | 0 |
| FFMC | 86.2 |
| DMC | 26.2 |
| ISI | 5.1 |
| Classes | 1 |
| Region | 0 |

Example Prediction

```
Predicted Fire Weather Index = 12.85
```

---

# 📦 Libraries Used

```python
Flask
NumPy
Pandas
Scikit-learn
Pickle
```

---

# 🔮 Future Improvements

- Responsive UI with Bootstrap
- Docker Deployment
- Cloud Deployment (Render / Railway / AWS)
- REST API Support
- Model Monitoring
- Multiple ML Model Comparison
- Input Validation
- Interactive Visualizations

---

# 👨‍💻 Author

**Dipesh Vishnu Bante**

📧 Email: **dipeshbante611@gmail.com**

GitHub: https://github.com/your-github-username

---

# 📄 License

This project is created for educational and learning purposes.

© 2026 Dipesh Vishnu Bante. All rights reserved.

---

# ⭐ If you found this project useful, don't forget to Star the repository!