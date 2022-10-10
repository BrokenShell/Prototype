import os

import joblib


class Classifier:
    filepath = os.path.join("app", "saved_model", "model.joblib")

    def __init__(self, name):
        self.name = name
        self.level = 100

    def __str__(self):
        return "\n".join(f"{k}: {v}" for k, v in vars(self).items())

    def save(self):
        joblib.dump(self, self.filepath)

    @classmethod
    def open(cls):
        return joblib.load(cls.filepath)
