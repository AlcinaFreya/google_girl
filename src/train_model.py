import pandas as pd
import xgboost as xgb
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.metrics import mean_absolute_error, r2_score
import joblib

df = pd.read_csv("features.csv")
X = df.drop(columns=['Logic Depth'])
y = df['Logic Depth']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
model = xgb.XGBRegressor(objective='reg:squarederror', n_estimators=100, learning_rate=0.1, max_depth=3)
model.fit(X_train, y_train)
joblib.dump(model, "logic_depth_predictor.pkl")
