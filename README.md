🚀 Face Recognition-Based Attendance Management System
🧠 AI + Computer Vision | 🎓 Smart Attendance | 📸 Real-time Recognition
<p align="center"> <img src="https://img.shields.io/badge/AI-Powered-blue?style=for-the-badge"/> <img src="https://img.shields.io/badge/OpenCV-4.9.0-green?style=for-the-badge"/> <img src="https://img.shields.io/badge/Python-3.10+-yellow?style=for-the-badge"/> <img src="https://img.shields.io/badge/Status-Active-success?style=for-the-badge"/> </p>

📌 Overview

A smart, fully automated Attendance Management System using Face Recognition.
Students simply look at the camera — the system verifies identity, marks attendance,
and stores data securely in the database.

✨ No more proxy attendance | ✨ No more manual roll calls

| Category                | What You Get                                |
| ----------------------- | ------------------------------------------- |
| 🔍 Face Recognition     | Real-time detection using **OpenCV + LBPH** |
| 🛂 Authentication       | Role-based **Admin / Faculty** login        |
| 🗂️ Database            | MySQL / CSV based attendance storage        |
| 📝 Attendance           | Auto-marking with **time & date**           |
| 📊 Dashboard            | Attendance statistics & charts              |
| 🧾 Reporting            | Export reports as **PDF / Excel**           |
| 📸 Face Dataset Builder | Capture training images per student         |
| 🎨 UI/UX                | Modern Tkinter GUI                          |
| 🔁 Model Training       | Face encoding retraining mechanism          |

UML DIAGRAM-

<p align="left"> <img width="600" src="https://github.com/user-attachments/assets/e1f22638-9c79-4042-a1fb-4a9a44b47b3a"> <br><br> <img width="600" src="https://github.com/user-attachments/assets/96c00583-ff3e-415d-8ab9-f3859b12ac31"> <br><br> <img width="600" src="https://github.com/user-attachments/assets/b152d6f1-6ffd-447f-8a13-28583f984c72"> </p>

🧩 System Architecture
Camera → Face Detector → Feature Extraction → Face Recognition
       → Attendance Marking → Database → Reports/Analytics

🛠️ Tech Stack

Component	Technology
Language	Python
AI Model	LBPH Face Recognizer
GUI	Tkinter
Database	MySQL (or CSV)
Visualization	Matplotlib
Camera API	OpenCV 

📦 Installation & Setup
1️⃣ Clone the Repository
git clone https://github.com/shivamyadav039/AttendanceManagementSystemFRS.git
cd AttendanceManagementSystemFRS

2️⃣ Create Virtual Environment
python3 -m venv .venv
3️⃣ Activate Virtual Environment
OS	Command
Windows	.venv\Scripts\activate
Mac/Linux	source .venv/bin/activate
4️⃣ Install Dependencies
pip install -r requirements.txt

5️⃣ Create Training Directory
mkdir TrainingImage

6️⃣ Run the Application
python attendance.py

📂 Project Folder Structure

├── attendance.py
├── TrainingImage/
├── AttendaceRecords/
├── requirements.txt
└── README.md

📈 Future Enhancements 🧩

✔ Cloud-based attendance storage
✔ Deep Learning-based recognition (FaceNet / Dlib)
✔ Mobile app for attendance lookup
✔ Multi-camera classroom support
✔ RFID + Face multi-factor authentication

🔒 License

📜 This project is licensed under the MIT License.

👨‍💻 Developer

Shivam Yadav
B.Tech CSE (AI & ML), Lovely Professional University
📧 Email: shivamyadav7745@gmail.com

🌍 LinkedIn https://www.linkedin.com/in/shivam-yadav39/
