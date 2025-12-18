from flask import Flask, render_template, request, flash
import pandas as pd
from src.prediction import Predictor
from src.insights import Insights

app = Flask(__name__)
app.secret_key = 'supersecretkey' 
try:
    predictor = Predictor(model_path='src/models/completion_model.pkl')
    MODEL_LOADED = True
except Exception as e:
    print(f"Warning: Model not found. {e}")
    MODEL_LOADED = False

@app.route('/', methods=['GET', 'POST'])
def index():
    results = None
    
    if request.method == 'POST':
        
        if not MODEL_LOADED:
            flash("Error: Model not loaded. Please run train_model.py first.")
            return render_template('index.html', results=None)

        if 'file' not in request.files:
            flash('No file part')
            return render_template('index.html', results=None)
            
        file = request.files['file']
        if file.filename == '':
            flash('No selected file')
            return render_template('index.html', results=None)

        try:
            df = pd.read_csv(file)
            

            preds, probs = predictor.predict_completion(df)
            df['predicted_completion'] = preds
            df['completion_probability'] = probs
            

            insights = Insights()
            df = insights.generate_risk_flag(df)
            difficulty_df = insights.analyse_chapter_difficulty(df)

            completion_rate = round(df['predicted_completion'].mean() * 100, 1)

            high_risk_students = df[df['drop_chance'] == 'High'].sort_values('completion_probability')
            high_risk_count = len(high_risk_students)
            
            risk_table = high_risk_students[['student_id', 'quiz_score', 'time_spent_minutes', 'completion_probability']].head(10).to_dict(orient='records')

            diff_table = difficulty_df.to_dict(orient='records')

            results = {
                "completion_rate": completion_rate,
                "high_risk_count": high_risk_count,
                "total_students": len(df),
                "risk_table": risk_table,
                "diff_table": diff_table
            }

        except Exception as e:
            flash(f"Error processing file: {str(e)}")

    return render_template('index.html', results=results)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)