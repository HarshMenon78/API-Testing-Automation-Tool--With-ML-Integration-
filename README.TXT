API Testing Automation Tool (With ML Integration)
=================================================

Description:
------------
This project is an **API Testing Automation Tool** enhanced with a **Machine Learning model** to classify API responses or predict expected outcomes. 
It provides a frontend interface for users to test APIs, while the backend integrates a trained ML model for intelligent decision-making.

The ML model used is a **Logistic Regression Classifier**, trained on a dataset located in `models/training_data.csv`.

Folder Structure:
-----------------
API Testing Automation Tool (With ML Integration)/
│
├── .env                        -> Environment variables for the project
├── data/                       -> Placeholder for additional datasets (if required)
├── frontend/html5up-hyperspace -> Frontend HTML, CSS, and JS files
├── main.py                     -> Main application launcher (runs the backend + frontend)
├── models/                     -> Machine Learning-related files
│   ├── training_data.csv        -> Dataset used for training the ML model
│   └── train_model.py           -> Script to train and save the ML model
├── source_code/                 -> Backend source code
│   ├── api.py                   -> API endpoints for frontend-backend communication
│   ├── tester.py                -> API testing automation logic
│   ├── utilis.py                -> Utility functions
│   └── __init__.py              -> Package initialization file
├── tests/                       -> Automated tests for APIs
│   ├── test_api.py               -> Test script for API endpoints
│   ├── test_cases/               -> JSON files with test cases
│   └── __pycache__/              -> Cached Python files
├── venv/                         -> Python virtual environment
├── Requirements.txt              -> Python dependencies for the project
└── project vision.txt            -> Vision and description of the project

Machine Learning Details:
-------------------------
- **Algorithm**: Logistic Regression Classifier
- **Training Data**: Located at `models/training_data.csv`
- **Training Script**: `train_model.py`
- The model needs to be trained **once** (unless you change the dataset).
- The trained model can then be loaded during backend execution without retraining.

Usage Instructions:
-------------------
1. **Install dependencies**: (pip install -r Requirements.txt)

2. **Train the ML model** (only needed once or when dataset changes) using :- python models/train_model.py

3. **Run the backend server**: python main.py (if not done , will show "❌ Error: NetworkError when attempting to fetch resource." , while trying to test the input json file test case)

4. **Open the frontend**:
- Navigate to the frontend folder or access via the backend's hosted URL.

5. **Test APIs**:
- Input API details in the frontend and view results.
- The ML model will assist in predicting expected outcomes.

Notes:
------
- Ensure that `training_data.csv` has enough representative examples for accurate predictions.
- The ML model does not require retraining every time the app starts, only when the dataset is updated.
- The `.env` file should contain any environment-specific configuration such as API keys, database URLs, etc.

Author:
-------
Harsh Menon

