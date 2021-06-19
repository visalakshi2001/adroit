import joblib
from sklearn.ensemble import RandomForestClassifier


rf = joblib.load('/model.joblib')



def predict(attributes):
    pass