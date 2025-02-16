# Fraud Detection System - Real-Time Machine Learning Deployment 🚀

## 📌 Project Overview
This project builds a **real-time fraud detection system** using **Kafka, Apache Spark, XGBoost, SHAP, FastAPI, and Kubernetes**. The system processes transaction data, predicts fraudulent activities, and deploys the model via **Docker & Kubernetes**.

---

## 📂 Folder Structure
```
fraud_detection_project/
│── dags/                 # Apache Airflow DAGs for automation
│── data/                 # Raw and processed datasets
│── models/               # Trained ML models
│── scripts/              # ETL & ML scripts
│   ├── extract.py        # Data ingestion from Kafka
│   ├── transform.py      # Data processing with Spark
│   ├── train_model.py    # Train XGBoost model
│   ├── explain_model.py  # Model explainability with SHAP
│   ├── deploy_model.py   # Deploy model via FastAPI
│── api/                  # FastAPI service for fraud predictions
│── deployment/           # Kubernetes deployment files
│── config/               # Config files for DB & AWS credentials
│── README.md             # Documentation
```

---

## 🔧 Setup Instructions
### **1️⃣ Install Dependencies**
```bash
pip install pandas numpy pyspark kafka-python xgboost shap fastapi uvicorn boto3
```

### **2️⃣ Run Kafka Producer (Simulated Transactions)**
```bash
python scripts/stream_data.py
```

### **3️⃣ Extract & Process Data**
```bash
python scripts/extract.py
python scripts/transform.py
```

### **4️⃣ Train Model**
```bash
python scripts/train_model.py
```

### **5️⃣ Explain Predictions**
```bash
python scripts/explain_model.py
```

### **6️⃣ Deploy API Locally**
```bash
uvicorn deploy_model:app --host 0.0.0.0 --port 8000
```

---

## 🚀 Deploying on Kubernetes
### **1️⃣ Build & Push Docker Image**
```bash
docker build -t fraud-api .
docker tag fraud-api your-dockerhub-username/fraud-api:latest
docker push your-dockerhub-username/fraud-api:latest
```

### **2️⃣ Apply Kubernetes Deployment**
```bash
kubectl apply -f deployment/k8s-deployment.yaml
kubectl apply -f deployment/k8s-service.yaml
kubectl get services
```

---

## 📊 Key Technologies Used
- **Kafka** → Real-time transaction streaming
- **Apache Spark** → Big data processing
- **XGBoost** → Fraud classification model
- **SHAP** → Explainable AI for fraud detection
- **FastAPI** → Serve fraud detection API
- **Docker & Kubernetes** → Model deployment & scaling

---

 

---

**Author:** Umair khalid
**Contact:** sking3061@gmail.com
