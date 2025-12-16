🤖 Smart Attendance System

Face Recognition Based Attendance Management System

A full-stack AI-powered Smart Attendance System that uses computer vision to automatically recognize faces and mark attendance in real time.
Built with OpenCV, SQLite, and Streamlit, this project demonstrates practical application of Machine Learning + Database + UI/UX in a real-world scenario.

🚀 Features
🎥 Face Recognition Attendance

Real-time face detection & recognition using webcam

Automatically marks attendance with timestamp

Prevents duplicate attendance entries for the same user

➕ User Registration

Register new users directly from the UI

Captures multiple face samples via camera

Automatically retrains the recognition model

Stores user data securely in database

📊 Attendance Dashboard

Total users count

Present today count

Total attendance records

Clean, modern dashboard UI

📋 Attendance Records

View all attendance logs

Filter by:

Date

Today only

User name

Export filtered data as CSV

🧹 Admin Controls

Reset all attendance records with one click

Safe database operations

Clear feedback using spinners & alerts

🛠️ Tech Stack
Layer	Technology
Programming	Python
Computer Vision	OpenCV
Face Recognition	LBPH Face Recognizer
Database	SQLite
Backend	Python
Frontend / UI	Streamlit
Data Handling	Pandas
Deployment Ready	Streamlit Cloud
📂 Project Structure
Smart_Attendance_System/
│
├── app.py                  # Streamlit dashboard
├── main.py                 # Face recognition & attendance marking
├── register.py             # User registration & face capture
├── train_model.py          # Model training
├── db_init.py              # Database initialization
├── db.py                   # Database helper functions
│
├── database/
│   └── attendance.db       # SQLite database
│
├── dataset/                # Face image samples
├── models/                 # Trained model files
│
├── haarcascade_frontalface_default.xml
├── requirements.txt
├── README.md
└── .gitignore

🧠 How It Works

User Registration

Admin enters user name

Camera captures face samples

Images stored in dataset

Model retrained automatically

User added to database

Attendance Marking

Camera detects faces

ML model predicts user ID

Name fetched from database (metadata)

Attendance saved with timestamp

Dashboard

Streamlit UI fetches data from SQLite

Displays real-time statistics

Allows filtering & exporting records

🗄️ Database Schema (SQLite)
users table
Column	Type
id	INTEGER (Primary Key)
name	TEXT
active	INTEGER
attendance table
Column	Type
id	INTEGER
user_id	INTEGER (Foreign Key)
timestamp	TEXT
⚙️ Installation & Setup
1️⃣ Clone the repository
git clone https://github.com/your-username/smart-attendance-system.git
cd smart-attendance-system

2️⃣ Install dependencies
pip install -r requirements.txt

3️⃣ Initialize database
python db_init.py

4️⃣ Run the application
streamlit run app.py

📸 Demo Capabilities

Live face recognition via webcam

Register new users dynamically

Attendance marked automatically

Admin dashboard with filters

CSV export for reports

🎯 Use Cases

Colleges & schools

Office attendance systems

Labs & training centers

Secure entry logging

AI/ML academic projects

💡 Why This Project Matters

Demonstrates end-to-end ML pipeline

Combines AI + Database + UI

Shows real-world problem solving

Deployment-ready architecture

Interview-grade project (not a toy demo)

📈 Future Enhancements

Role-based login (Admin / User)

Cloud database (PostgreSQL / MySQL)

Face anti-spoofing

Multi-camera support

Attendance analytics & charts

Dockerized deployment

👨‍💻 Author

Aryan Upadhyay
B.Tech CSE
Passionate about AI, ML & System Design

⭐ If you like this project

Give it a ⭐ on GitHub — it motivates continuous improvement!