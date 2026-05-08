import pandas as pd
from features.build_features import build_features
from models.train_model import train

def run():

    df = pd.read_csv("Data/processed/fraudTrain.csv")

    df = build_features(df)

    train(df)

if __name__ == "__main__":
    run()