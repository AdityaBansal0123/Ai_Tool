import joblib 
import pandas as pd

class Predictor:
    def __init__(self,model_path='models/completion_model.pkl'):
        self.model = joblib.load(model_path)

    def predict_completion(self,data:pd.DataFrame):
        features = data[['chapter_order','time_spent_minutes','quiz_score']]
        predictions = self.model.predict(features)
        proba = self.model.predict_proba(features)[:,1]
        return predictions,proba
    