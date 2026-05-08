import pandas as pd
from features.build_features import build_features
from models.predict_model import predict

def run():

    df = pd.read_csv("Data/processed/fraudTest.csv")

    df = build_features(df)

    df = df.drop(columns=["is_fraud"], errors="ignore")

    df = predict(df)

    df.to_csv("Data/predictions/fraud_predictions.csv", index=False)

if __name__ == "__main__":
    run()