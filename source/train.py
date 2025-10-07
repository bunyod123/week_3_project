import pandas as pd
import logging
from sklearn.model_selection import train_test_split, KFold, cross_val_score
from sklearn.metrics import r2_score, mean_absolute_error

logger = logging.getLogger(__name__)

class Training:
    def __init__(self, model, x, y):
        self.model = model
        self.x = x
        self.y = y
        logger.info(f"Trainer initialized for model with shape: {x.shape}")

    def train(self):
        try:
            self.x_train, self.x_test, self.y_train, self.y_test = train_test_split(self.x, self.y, test_size=0.2, random_state=42)
            self.model.fit(self.x_train, self.y_train)
            logger.info("Model trained successfully.")
            return self
        except Exception as e:
            logger.error("Error during training {e}")
            raise e


    def evaluate(self):
        try:
            y_pred = self.model.predict(self.x_test)
            kf = KFold(n_splits=5, shuffle=True, random_state=42)
        
            self.r2 = r2_score(self.y_test, y_pred)
            self.mae = mean_absolute_error(self.y_test, y_pred)
            self.kfold = cross_val_score(self.model, self.x, self.y, cv=kf, scoring='r2')

            logger.info(
                "Evaluation done for model %s: r2=%.6f, mae=%.6f, kfold_mean=%.6f, kfold_std=%.6f",
                type(self.model).__name__, self.r2, self.mae, self.kfold.mean(), self.kfold.std()
            )
            return self.r2, self.mae, self.kfold, self.y_test, y_pred
        except Exception as e:
            logger.error("Error during evaluation: %s", str(e))
            raise e