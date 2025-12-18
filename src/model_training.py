import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import joblib
import os

def generate_data(n_samples=10000000):
    np.random.seed(42)
    data = {
        'student_id': [f'S{i:04d}' for i in range(n_samples)],
        'course_id': np.random.choice(['C101', 'C102', 'C103'], n_samples),
        'chapter_order': np.random.randint(1, 11, n_samples),
        'time_spent_minutes': np.random.normal(45, 15, n_samples),  # Normal dist around 45 mins
        'quiz_score': np.random.randint(0, 100, n_samples),
    }
    df = pd.DataFrame(data)
    df['completion_status'] = np.where(
        (df['quiz_score'] > 60) & (df['time_spent_minutes'] > 20), 
        1, 0
    )
    return df


def train():
    print("Generating synthetic data...")
    df = generate_data()

    os.makedirs('data', exist_ok=True)
    df.to_csv('data/synthetic_data.csv', index=False)

    X = df[['chapter_order', 'time_spent_minutes', 'quiz_score']]
    y = df['completion_status']

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
   
    print("Training Random Forest model...")
    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)

    acc = accuracy_score(y_test, model.predict(X_test))
    print(f"Model Accuracy: {acc:.2f}")

    os.makedirs('models', exist_ok=True)
    joblib.dump(model, 'models/completion_model.pkl')
    print("Model saved to models/completion_model.pkl")

if __name__ == "__main__":
    train()