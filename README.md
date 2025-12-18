# 🚀 API Testing Automation Tool (With ML Integration)

An advanced **API Testing Automation Tool** powered by a **Machine Learning (ML)** model that intelligently classifies API responses and predicts expected outcomes.  
It combines a clean **frontend interface** for user interaction with a robust **Python backend** that integrates ML-based decision support.

---

## 🧠 Description

This project integrates **API testing automation** with **Machine Learning intelligence**.  
The ML component uses a **Logistic Regression Classifier** trained on a dataset stored in `models/training_data.csv`.  
It enhances the testing process by predicting API outcomes and automating classification for consistent analysis.

---

## 📁 Folder Structure

```
API Testing Automation Tool (With ML Integration)/
│
├── .env                         -> Environment variables for the project
├── data/                        -> Placeholder for additional datasets (if required)
├── frontend/html5up-hyperspace  -> Frontend HTML, CSS, and JS files
├── main.py                      -> Main application launcher (runs backend + frontend)
├── models/                      -> Machine Learning-related files
│   ├── training_data.csv         -> Dataset used for training the ML model
│   └── train_model.py            -> Script to train and save the ML model
├── source_code/                  -> Backend source code
│   ├── api.py                    -> API endpoints for frontend-backend communication
│   ├── tester.py                 -> API testing automation logic
│   ├── utilis.py                 -> Utility functions
│   └── __init__.py               -> Package initialization file
├── tests/                        -> Automated tests for APIs
│   ├── test_api.py               -> Test script for API endpoints
│   ├── test_cases/               -> JSON files with test cases
│   └── __pycache__/              -> Cached Python files
├── venv/                         -> Python virtual environment
├── Requirements.txt              -> Python dependencies for the project
└── project vision.txt            -> Vision and description of the project
```

---

## 🤖 Machine Learning Details

- **Algorithm**: Logistic Regression Classifier  
- **Training Data**: `models/training_data.csv`  
- **Training Script**: `models/train_model.py`  
- **Retraining Requirement**: Only when the dataset changes  
- The trained model is automatically loaded during backend execution to avoid retraining on every launch.

---

## ⚙️ Usage Instructions

1. **Install dependencies**  
   ```
   pip install -r Requirements.txt
   ```

2. **Train the ML model** (required only once or when the dataset changes)  
   ```
   python models/train_model.py
   ```

3. **Run the backend server**  
   ```
   python main.py
   ```
   > If not running, you may encounter the error:  
   > ❌ *"Error: NetworkError when attempting to fetch resource."*  
   > This occurs when the frontend cannot connect to the backend service.

4. **Access the frontend**
   - Open the `frontend/html5up-hyperspace` folder locally,  
     **or**
   - Visit the hosted backend URL to access the web interface.

5. **Test APIs**
   - Input API details in the frontend.
   - View real-time results and ML-assisted predictions for API responses.

---

## 📝 Notes

- Ensure `training_data.csv` contains representative examples for reliable predictions.  
- Retrain the ML model **only** when updating or modifying the dataset.  
- Populate the `.env` file with environment-specific configurations (e.g., API keys, database URLs, ports).  

---

## 👤 Author

**Harsh Menon**  
Developer | Machine Learning & Automation Enthusiast  

📧 *Feel free to connect or contribute via pull requests!*
```

Would you like me to also add **badges** (e.g., Python version, license, build status) and a short **preview GIF/image section** at the top to give it a more polished GitHub look?
