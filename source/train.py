import pandas as pd
import logging
from sklearn.model_selection import train_test_split, KFold, cross_val_score
from sklearn.metrics import accuracy_score

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
            kf = KFold(n_splits=5, shuffle=True, random_state=99)
        
            self.accurycy = accuracy_score(self.y_test, y_pred)
            
            self.kfold = cross_val_score(self.model, self.x, self.y, cv=kf)

            logger.info("Evaluation end")
            return self.accurycy, self.kfold, self.y_test, y_pred
        
        except Exception as e:
            logger.error(f"Error during evaluation {e}")
            raise e