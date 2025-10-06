import pandas as pd
class DataLoader:
    def __init__(self, path):
        self.path = path

    def load_data(self):
        
        try:
            df = pd.read_csv(self.path)
            print(f"Dataset  yuklandi: {self.path}")
            return df
        except Exception as e:
            print(f"Dataset yuklanmadi: {e}")
            return None
        