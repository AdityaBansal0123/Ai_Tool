🎓 AI Learning Intelligence Tool
A production-grade MLOps platform that uses Machine Learning to predict student dropout risks and analyze course difficulty. Designed for high-performance engineering, this tool has been successfully stress-tested on synthetic datasets of 10 million records.

🚀 How to Run Locally
Option 1: The "Zero-Setup" Docker Way (Recommended)
This tool is fully containerized and hosted on Docker Hub. You can run it instantly without even cloning this repository:

Run the image:

Bash

docker run -p 5000:5000 adityabansal480/ai-learning-tool:latest
Access the app: Open your browser to http://localhost:5000.

Option 2: Manual Development Setup
Clone the repo: git clone https://github.com/AdityaBansal0123/Ai_Tool.git

Install dependencies: pip install -r requirements.txt

Train the AI: python src/model_training.py

Start the server: python app.py

📊 My AI Tool Design & Usage
What the AI Tool Does
This tool acts as a predictive dashboard for educators to improve student retention. It transforms raw engagement data into two actionable insights:

Student Risk Flags: Highlights students falling behind based on a combination of low quiz scores and low time engagement.

Chapter Difficulty Mapping: Automatically ranks course content by difficulty, helping instructors identify which lessons need revision.

AI Model and Feature Choices
Model: Random Forest Classifier (via Scikit-Learn) was selected for its robustness against outliers and its ability to handle non-linear relationships in student behavior data.

Features:

quiz_score: The primary indicator of content mastery.

time_spent_minutes: Used to distinguish between a "stuck" student (high time, low score) vs. a "disengaged" student (low time, low score).

Engineering Quality: The app utilizes a Gunicorn production server with a 600-second (10-minute) timeout to ensure large-scale CSV processing (up to 10M rows) does not cause worker timeouts.

Input and Output Format
Input: A CSV file with columns: student_id, quiz_score, time_spent_minutes, chapter_order.

Output: A web-based dashboard displaying "High Risk" counts, individual completion probabilities, and visual chapter difficulty rankings.

🛡️ AI Usage Disclosure
In compliance with the AI Usage Policy, the following disclosures are made:

AI Assistance: I utilized Gemini (AI Assistant) as a technical thought partner throughout development.

Usage Areas:

Infrastructure: Assisting with Dockerfile configuration and resolving Python 3.10/Scikit-learn 1.7.2 version compatibility issues.

Frontend Logic: Refining Jinja2 template rendering to ensure dictionary-based data displayed correctly in the UI.

How Outputs Were Verified:

Stress Test: I verified the model by processing a 10 million-row dataset, confirming the system handled the load and produced feasible results (e.g., extremely low completion chance for students with scores < 10).

Reproducibility: I verified the Docker Hub image by deleting all local images and performing a clean docker pull from the registry to ensure it runs on any machine.

Independent Logic: I independently defined the business logic for "High Risk" thresholds (Score < 50 or Time < 15 mins) and designed the project's modular directory structure (separating src, templates, and models).


SAMPLE_INPUT:-
student_id,quiz_score,time_spent_minutes,chapter_order
S001,85,45,1
S002,12,58,1
S003,92,60,2
S004,35,21,2
S005,48,12,3
S006,77,40,3
S007,18,51,4
S008,95,55,4
S009,5,47,5
S010,42,14,5

SAMPLE__OUTPUT:-

Student Risk Analysis:-
Student ID,Quiz Score,Time (Min),Completion Prob.,Risk Level
S009,5,47,8.2%,🔴 High Risk
S002,12,58,14.5%,🔴 High Risk
S005,48,12,32.1%,🔴 High Risk
S001,85,45,94.8%,🟢 Safe

Course Difficulty Ranking:-
Chapter,Avg. Score,Difficulty Rating,Status
Chapter 5,23.5,76.5,⚠️ High Difficulty (Bottleneck)
Chapter 1,48.5,51.5,Moderate
Chapter 4,56.5,43.5,Balanced
