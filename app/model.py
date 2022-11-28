import os
from typing import List

import joblib
from pandas import DataFrame
from sklearn.ensemble import RandomForestClassifier


class Classifier:
    filepath = os.path.join("app", "saved_model", "model.joblib")

    def __init__(self, features: DataFrame, targets: List):
        # Todo: Add train/test split
        # Todo: Add RandomSearchCV pipeline
        # Todo: Encode features if needed
        self.model = RandomForestClassifier()
        self.model.fit(features, targets)

    def __call__(self, basis: DataFrame):
        return self.model.predict(basis)

    def __str__(self):
        return "\n".join(f"{k}: {v}" for k, v in vars(self).items())

    def save(self):
        joblib.dump(self, self.filepath)

    @classmethod
    def open(cls):
        return joblib.load(cls.filepath)
