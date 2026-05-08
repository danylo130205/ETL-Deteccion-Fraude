import pandas as pd
import joblib
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report

def train(df: pd.DataFrame):

    X = df.drop(columns=["is_fraud"])
    y = df["is_fraud"]

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    model = RandomForestClassifier(
        n_estimators=100,
        max_depth=10,
        class_weight="balanced",
        random_state=42,
        n_jobs=-1
    )

    model.fit(X_train, y_train)

    y_probs = model.predict_proba(X_test)[:, 1]

    y_pred = (y_probs > 0.7).astype(int)

    print(classification_report(y_test, y_pred))

    # Guardar modelo
    joblib.dump(model, "models/artifacts/random_forest.pkl")

    # Guardar columnas
    joblib.dump(X_train.columns, "models/artifacts/columns.pkl")

    return model