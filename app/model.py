import os
from typing import List

import joblib
from pandas import DataFrame
from sklearn.ensemble import RandomForestClassifier


class Serializer:
    filepath = ""

    def save(self):
        joblib.dump(self, self.filepath)

    @classmethod
    def open(cls):
        return joblib.load(cls.filepath)


class Classifier(Serializer):
    filepath = os.path.join("app", "saved_model", "model.joblib")

    def __init__(self, features: DataFrame, targets: List):
        self.model = RandomForestClassifier()
        self.model.fit(features, targets)

    def __call__(self, basis: DataFrame):
        return self.model.predict(basis)

    def __str__(self):
        return "\n".join(f"{k}: {v}" for k, v in vars(self).items())
