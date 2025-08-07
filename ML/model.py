import numpy as np
from sklearn.ensemble import IsolationForest
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
import joblib

# =============================
# Anomaly Detection Model
# =============================

class AnomalyDetector:
    def __init__(self):
        self.model = IsolationForest(n_estimators=100, contamination=0.1, random_state=42)
        self.scaler = StandardScaler()

    def train(self, X):
        X_scaled = self.scaler.fit_transform(X)
        self.model.fit(X_scaled)
        print("[INFO] Anomaly Detector trained successfully.")

    def predict(self, X):
        X_scaled = self.scaler.transform(X)
        return self.model.predict(X_scaled)  # -1: anomaly, 1: normal

    def save_model(self, path='models/anomaly_model.pkl'):
        joblib.dump((self.model, self.scaler), path)

    def load_model(self, path='models/anomaly_model.pkl'):
        self.model, self.scaler = joblib.load(path)