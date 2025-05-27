 AI-Powered Student Performance Predictor
A machine learning web app that predicts whether a student is likely to pass or fail based on academic and demographic data. Built using Python, Scikit-learn, Pandas, and deployed with Flask.

🚀 Demo
🔗 [Live Demo Coming Soon...]

📌 Features
Predicts student performance using gender and test preparation status
Achieves 86.5% accuracy with Random Forest Classifier
Real-time predictions via a simple Flask-based web UI
User-friendly dropdown inputs
Model training script included
🛠️ Tech Stack
Backend: Python, Flask, Scikit-learn, Pandas
Frontend: HTML, CSS
Model: RandomForestClassifier
🧪 How It Works
The model is trained on a dataset of student performances.
It learns patterns based on features like gender and test preparation course.
Flask exposes a web interface to accept inputs and return predictions in real time.
🖥️ Local Setup Instructions
# 1. Clone the repo
git clone https://github.com/yourusername/student-performance-predictor.git
cd student-performance-predictor

# 2. Install dependencies
pip install -r requirements.txt

# 3. Train the model (generates model.pkl)
python train_model.py

# 4. Launch the web app
python app.py

File structure:

├── app.py              # Flask web server
├── train_model.py      # Trains and saves the ML model
├── model.pkl           # Trained model (generated after running train_model.py)
├── templates/
│   └── index.html      # Frontend HTML page
├── static/
│   └── style.css       # CSS styles (optional)
├── StudentsPerformance.csv  # Dataset
├── requirements.txt    # Python dependencies

Accuracy
Final model accuracy: 86.5%

Evaluated using a train/test split

Trained with just two features to demonstrate minimalistic predictive modeling

Future Improvements
Add more input features (math score, parental education)

Improve UI styling

Deploy live on Render, Replit, or HuggingFace Spaces
