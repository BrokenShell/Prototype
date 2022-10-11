from string import ascii_lowercase

from pandas import DataFrame

from app.model import Classifier


n_cols = 5
n_rows = 1000
n_features = n_cols - 1
n_predictions = 5

df = DataFrame([{
    k: v for k, v in zip(ascii_lowercase[:n_cols], range(n_cols))
} for _ in range(n_rows)])

feature_cols = df.columns[:-1].tolist()
features = df[feature_cols]

target_col = df.columns[-1]
targets = df[target_col]

# ---------------------- #

Classifier(features, targets).save()

model = Classifier.open()

basis = DataFrame([{
    k: v for k, v in zip(ascii_lowercase[:n_features], range(n_features))
} for _ in range(n_predictions)])

print(model(basis))
