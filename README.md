# 🚲 Bike Count Prediction (ML Project)

## 📌 Overview

This project predicts bike rental demand using historical data and machine learning.
It is designed with a production-oriented approach using pipelines, containerization, and a simple dashboard for visualization.

---

## ⚙️ Tech Stack

* Python (Pandas, Scikit-learn)
* **Kedro** – pipeline orchestration
* **Docker** – containerization
* **Dash** – dashboard UI
* Git & GitHub – version control

---

## 🏗️ Project Architecture

```
Data → Kedro Pipelines → Model Training → Model Inference → Dash Dashboard
```

* Modular pipelines for data preprocessing, training, and inference
* Reproducible workflows using Kedro
* Containerized setup using Docker

---

## 🔄 Pipelines

* **Data Pipeline** → Data cleaning & feature engineering
* **Training Pipeline** → Model training & evaluation
* **Inference Pipeline** → Predictions on new data

---

## 🚀 How to Run

### 1. Clone repo

```
git clone <your-repo-link>
cd bike-count-prediction
```

### 2. Run with Docker

```
docker compose up --build
```

### 3. Run pipelines manually (optional)

```
kedro run
```

---

## 📊 Dashboard

* Built using Dash
* Displays predictions and trends interactively

---

## 🎯 Key Highlights

* End-to-end ML pipeline (data → model → UI)
* Production-style structure using Kedro
* Dockerized for reproducibility
* Clean project organization

---

## 📌 Future Improvements

* Model optimization & hyperparameter tuning
* Deploy on cloud (GCP/AWS)
* Add real-time data ingestion

---

## 👤 Author

Nima
