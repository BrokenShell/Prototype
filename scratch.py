""" Testing the serializer """
from string import ascii_lowercase
from pandas import DataFrame
from app.model import Classifier


""" Training configuration """
n_cols = 5
n_rows = 1000
n_features = n_cols - 1
n_predictions = 5


""" Training Data - deterministic fake data """
df = DataFrame([{
    k: v for k, v in zip(ascii_lowercase[:n_cols], range(n_cols))
} for _ in range(n_rows)])
print(f"\nTraining Sample:\n{df.sample(5, ignore_index=True)}\n")


""" Training features 'X_train' """
feature_cols = df.columns[:-1].tolist()
features = df[feature_cols]
print(f"Feature Names: {feature_cols}")


""" Training target 'y_train' """
target_col = df.columns[-1]
targets = df[target_col]
print(f"Target Name: {target_col}\n")


""" Training and saving the model to disk """
Classifier(features, targets).save()


""" Opening the saved model from disk """
model = Classifier.open()


""" Prediction input data """
basis = DataFrame([{
    k: v for k, v in zip(ascii_lowercase[:n_features], range(n_features))
} for _ in range(n_predictions)])
print(f"Prediction Basis:\n{basis}\n")
print(f"Predictions: {model(basis)}")
