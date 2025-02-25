# 🚀 Logic Depth Prediction using XGBoost

## 📌 Overview
This project predicts **combinational logic depth** based on **circuit parameters** using **Machine Learning (XGBoost)**.  
It uses circuit features like **Fan-In, Fan-Out, Gate Count, Path Delay, Netlist Depth, Critical Path Length, and Average Load** to make accurate predictions.

---

## 📂 Project Structure
```
google_girl/
│── data/
│   ├── features.csv               # Dataset with logic circuit features
│   ├── prediction_results.txt      # Predictions on test data
│   ├── feature_importance.png      # Feature importance visualization
│── models/
│   ├── logic_depth_predictor.pkl   # Trained ML model
│── src/
│   ├── train_model.py              # Training script
│── README.md                      # Project documentation
```

---

## 🔧 Installation & Usage

### 📥 1. Clone the Repository

### 🚀 2. Install Required Libraries

### 📊 3. Train the Model
Run the training script to build the model:

### 📈 4. Generate Predictions
Run the script to predict logic depth on new circuit data:

---

## 📊 Feature Importance
The model evaluates the importance of different circuit parameters. The feature importance plot below shows the most significant factors affecting **logic depth**.



---

## 📜 Dataset
The dataset (`features.csv`) contains logic circuit parameters and their corresponding **logic depth** values.  
Example:

---

## 🏆 Model Performance
The XGBoost model was trained using **GridSearchCV** to find the best hyperparameters.  
### **📊 Model Evaluation Results:**
- **Training Samples:** 19
- **Testing Samples:** 5
- **Best Hyperparameters:** {'learning_rate': 0.1, 'max_depth': 3, 'n_estimators': 100}
- **Mean Absolute Error:** 0.320
- **R² Score:** 0.960
