import pandas as pd
import joblib

def predict(df: pd.DataFrame):

    model = joblib.load("models/artifacts/random_forest.pkl")
    columns = joblib.load("models/artifacts/columns.pkl")

    # Alinear columnas
    df = df.reindex(columns=columns, fill_value=0)

    preds = model.predict(df)
    probs = model.predict_proba(df)[:, 1]
    

    df["prediction"] = preds
    df["fraud_probability"] = probs

    return df