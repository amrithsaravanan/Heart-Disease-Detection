# ❤️ Heart Disease Prediction using K-Nearest Neighbors (KNN)

A machine learning web application that predicts whether a patient is likely to have heart disease based on clinical parameters. The project uses the **K-Nearest Neighbors (KNN)** classification algorithm and is built with **Streamlit** for an interactive and user-friendly interface.

---

## 📌 Project Overview

Heart disease is one of the leading causes of death worldwide. Early prediction can help healthcare professionals identify high-risk patients and support timely medical intervention.

This project uses the **K-Nearest Neighbors (KNN)** algorithm to classify patients into one of two categories:

- ❤️ Heart Disease Detected
- 💚 No Heart Disease

The application accepts patient health information and provides an instant prediction.

---

## ✨ Features

- Interactive Streamlit web application
- K-Nearest Neighbors (KNN) classification model
- Data preprocessing using StandardScaler
- Model saved using Pickle
- Real-time prediction
- User-friendly input form
- Clean and organized project structure

---

## 🛠️ Technologies Used

- Python
- Streamlit
- Pandas
- NumPy
- Scikit-learn
- Matplotlib
- Pickle

---

## 📂 Project Structure

```text
HeartDiseasePrediction/
│
├── app.py
├── requirements.txt
├── README.md
├── LICENSE
├── .gitignore
│
├── data/
│   └── heart.csv
│
├── models/
│   ├── knn_model.pkl
│   └── scaler.pkl
│
└── notebooks/
    └── Heart_Disease_KNN.ipynb
```

---

## 📊 Dataset

The project uses the **Heart Disease Dataset**, which contains patient medical information used to predict the presence of heart disease.

### Features

| Feature | Description |
|---------|-------------|
| age | Age |
| sex | Gender |
| cp | Chest Pain Type |
| trestbps | Resting Blood Pressure |
| chol | Serum Cholesterol |
| fbs | Fasting Blood Sugar |
| restecg | Resting ECG Result |
| thalach | Maximum Heart Rate Achieved |
| exang | Exercise-Induced Angina |
| oldpeak | ST Depression |
| slope | Slope of Peak Exercise ST Segment |
| ca | Number of Major Vessels |
| thal | Thalassemia |
| target | Heart Disease (0 = No, 1 = Yes) |

---

## 🤖 Machine Learning Workflow

```
Heart Disease Dataset
        │
        ▼
Data Preprocessing
        │
        ▼
Feature Scaling
        │
        ▼
Train-Test Split
        │
        ▼
KNN Model Training
        │
        ▼
Model Evaluation
        │
        ▼
Save Model (.pkl)
        │
        ▼
Streamlit Web Application
```

---

## 📈 Model Evaluation

The model is evaluated using:

- Accuracy
- Precision
- Recall
- F1-Score
- Confusion Matrix
- ROC Curve

---

## ⚙️ Installation

### 1. Clone the Repository

```bash
git clone https://github.com/amrithsaravanan/Heart-Disease-Detection.git

cd Heart-Disease-Detection
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Train the Model

Open and run:

```text
notebooks/Heart_Disease_KNN.ipynb
```

This generates:

```text
models/
├── knn_model.pkl
└── scaler.pkl
```

### 4. Run the Application

```bash
streamlit run app.py
```

Open your browser:

```text
http://localhost:8501
```

---

## 📁 Requirements

```text
streamlit
pandas
numpy
scikit-learn
matplotlib
joblib
```

---

## 🚀 Future Enhancements

- Compare KNN with other machine learning algorithms
- Hyperparameter tuning
- Model explainability
- Cloud deployment
- User authentication
- Patient report generation
- Enhanced dashboard and analytics

---

## 👨‍💻 Author

Amrith SS

GitHub: https://github.com/amrithsaravanan

---

## 🤝 Contributing

Contributions, suggestions, and improvements are welcome. Feel free to fork the repository and submit a pull request.

---

## ⭐ Support

If you found this project useful, please consider:

- ⭐ Starring this repository
- 🍴 Forking this repository
- 🛠️ Contributing to the project
