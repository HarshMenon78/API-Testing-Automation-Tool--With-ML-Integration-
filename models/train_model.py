import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
import joblib

# Step 1: Load your dataset
df = pd.read_csv('models/training_data.csv')

# Step 2: Split features (X) and target (y)
X = df.drop('target', axis=1)  # All columns except target
y = df['target']               # The target column (labels)

# Step 3: Train/test split to evaluate performance
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Step 4: Initialize model (Logistic Regression)
model = LogisticRegression(max_iter=1000)  # max_iter increased for convergence

# Step 5: Train model
model.fit(X_train, y_train)

# Step 6: Test model
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print(f"📊 Model Accuracy: {accuracy:.2%}")

# Step 7: Save model if accuracy is acceptable
if accuracy >= 0.80:
    joblib.dump(model, 'trained_model.pkl')
    print("✅ Model trained and saved as trained_model.pkl")
else:
    print("⚠️ Accuracy below 80%. Model not saved.")