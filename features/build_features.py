import pandas as pd
from features.haversine import haversine

def build_features(df: pd.DataFrame) -> pd.DataFrame:

    
    # Riesgo
    df["is_high_amount"] = (df["amt"] > 1000).astype(int)
    # Distancia
    df["distance_km"] = haversine(
        df["lat"],
        df["long"],
        df["merch_lat"],
        df["merch_long"]
    )
    # Calcular el promedio de monto por cliente
    df["avg_amt_client"] = df.groupby("cc_num")["amt"].transform("mean")
    # Calcular el promedio de transacciones por cliente al día
    df["transactions_per_day"] = df.groupby(["cc_num","trans_date"])["amt"].transform("count")
    # Categóricas
    df = pd.get_dummies(df, columns=['category'], drop_first=True)
    df = df.drop(columns=[
        "trans_date_trans_time",
        "cc_num",
        "trans_num",
        'merchant',
        'dob',
        'trans_date'
    ], errors="ignore")
    return df