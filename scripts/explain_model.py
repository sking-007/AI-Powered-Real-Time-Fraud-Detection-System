import shap
import xgboost as xgb
import pandas as pd

df = pd.read_csv("data/processed_transactions.csv")

X = df.drop(columns=['is_fraud'])
model = xgb.Booster()
model.load_model("models/fraud_model.json")

explainer = shap.Explainer(model)
shap_values = explainer(X)

shap.summary_plot(shap_values, X)
