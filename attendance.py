# import tkinter as tk
# from tkinter import *
# import os, cv2
# import shutil
# import csv
# import numpy as np
# from PIL import ImageTk, Image
# import pandas as pd
# import datetime
# import time
# import tkinter.font as font
# import pyttsx3
# # project module
# import show_attendance
# import takeImage
# import trainImage
# import automaticAttedance

# def text_to_speech(user_text):
#     engine = pyttsx3.init()
#     engine.say(user_text)
#     engine.runAndWait()

# haarcasecade_path = "haarcascade_frontalface_default.xml"
# trainimagelabel_path = (
#     "TrainingImageLabel/Trainner.yml"
# )
# trainimage_path = "TrainingImage"
# if not os.path.exists(trainimage_path):
#     os.makedirs(trainimage_path)

# studentdetail_path = (
#     "/StudentDetails/studentdetails.csv"
# )
# attendance_path = "Attendance"

# window = Tk()
# window.title("Face recognizer")
# window.geometry("1280x720")
# dialog_title = "QUIT"
# dialog_text = "Are you sure want to close?"
# window.configure(background="black")

# # to destroy screen
# def del_sc1():
#     sc1.destroy()

# # error message for name and no
# def err_screen():
#     global sc1
#     sc1 = tk.Tk()
#     sc1.geometry("400x110")
#     sc1.iconbitmap("AMS.ico")
#     sc1.title("Warning!!")
#     sc1.configure(background="black")
#     sc1.resizable(0, 0)
#     tk.Label(
#         sc1,
#         text="Enrollment & Name required!!!",
#         fg="yellow",
#         bg="black",
#         font=("times", 20, " bold "),
#     ).pack()
#     tk.Button(
#         sc1,
#         text="OK",
#         command=del_sc1,
#         fg="yellow",
#         bg="black",
#         width=9,
#         height=1,
#         activebackground="Red",
#         font=("times", 20, " bold "),
#     ).place(x=110, y=50)

# def testVal(inStr, acttyp):
#     if acttyp == "1":  # insert
#         if not inStr.isdigit():
#             return False
#     return True

# logo = Image.open("UI_Image/0001.png")
# logo = logo.resize((50, 47), Image.Resampling.LANCZOS)
# logo1 = ImageTk.PhotoImage(logo)
# titl = tk.Label(window, bg="black", relief=RIDGE, bd=10, font=("arial", 35))
# titl.pack(fill=X)
# l1 = tk.Label(window, image=logo1, bg="black",)
# l1.place(x=470, y=10)

# titl = tk.Label(
#     window, text="Smart College!!", bg="black", fg="green", font=("arial", 27),
# )
# titl.place(x=525, y=12)

# a = tk.Label(
#     window,
#     text="Welcome to the Face Recognition Based\nAttendance Management System",
#     bg="black",
#     fg="yellow",
#     bd=10,
#     font=("arial", 35),
# )
# a.pack()

# ri = Image.open("UI_Image/register.png")
# r = ImageTk.PhotoImage(ri)
# label1 = Label(window, image=r)
# label1.image = r
# label1.place(x=100, y=270)

# ai = Image.open("UI_Image/attendance.png")
# a = ImageTk.PhotoImage(ai)
# label2 = Label(window, image=a)
# label2.image = a
# label2.place(x=980, y=270)

# vi = Image.open("UI_Image/verifyy.png")
# v = ImageTk.PhotoImage(vi)
# label3 = Label(window, image=v)
# label3.image = v
# label3.place(x=600, y=270)

# def TakeImageUI():
#     ImageUI = Tk()
#     ImageUI.title("Take Student Image..")
#     ImageUI.geometry("780x480")
#     ImageUI.configure(background="black")
#     ImageUI.resizable(0, 0)
#     titl = tk.Label(ImageUI, bg="black", relief=RIDGE, bd=10, font=("arial", 35))
#     titl.pack(fill=X)
#     # image and title
#     titl = tk.Label(
#         ImageUI, text="Register Your Face", bg="black", fg="green", font=("arial", 30),
#     )
#     titl.place(x=270, y=12)
#     # heading
#     a = tk.Label(
#         ImageUI,
#         text="Enter the details",
#         bg="black",
#         fg="yellow",
#         bd=10,
#         font=("arial", 24),
#     )
#     a.place(x=280, y=75)
#     # ER no
#     lbl1 = tk.Label(
#         ImageUI,
#         text="Enrollment No",
#         width=10,
#         height=2,
#         bg="black",
#         fg="yellow",
#         bd=5,
#         relief=RIDGE,
#         font=("times new roman", 12),
#     )
#     lbl1.place(x=120, y=130)
#     txt1 = tk.Entry(
#         ImageUI,
#         width=17,
#         bd=5,
#         validate="key",
#         bg="black",
#         fg="yellow",
#         relief=RIDGE,
#         font=("times", 25, "bold"),
#     )
#     txt1.place(x=250, y=130)
#     txt1["validatecommand"] = (txt1.register(testVal), "%P", "%d")

#     # name
#     lbl2 = tk.Label(
#         ImageUI,
#         text="Name",
#         width=10,
#         height=2,
#         bg="black",
#         fg="yellow",
#         bd=5,
#         relief=RIDGE,
#         font=("times new roman", 12),
#     )
#     lbl2.place(x=120, y=200)
#     txt2 = tk.Entry(
#         ImageUI,
#         width=17,
#         bd=5,
#         bg="black",
#         fg="yellow",
#         relief=RIDGE,
#         font=("times", 25, "bold"),
#     )
#     txt2.place(x=250, y=200)

#     lbl3 = tk.Label(
#         ImageUI,
#         text="Notification",
#         width=10,
#         height=2,
#         bg="black",
#         fg="yellow",
#         bd=5,
#         relief=RIDGE,
#         font=("times new roman", 12),
#     )
#     lbl3.place(x=120, y=270)

#     message = tk.Label(
#         ImageUI,
#         text="",
#         width=32,
#         height=2,
#         bd=5,
#         bg="black",
#         fg="yellow",
#         relief=RIDGE,
#         font=("times", 12, "bold"),
#     )
#     message.place(x=250, y=270)

#     def take_image():
#         l1 = txt1.get()
#         l2 = txt2.get()
#         takeImage.TakeImage(
#             l1,
#             l2,
#             haarcasecade_path,
#             trainimage_path,
#             message,
#             err_screen,
#             text_to_speech,
#         )
#         txt1.delete(0, "end")
#         txt2.delete(0, "end")

#     # take Image button
#     takeImg = tk.Button(
#         ImageUI,
#         text="Take Image",
#         command=take_image,
#         bd=10,
#         font=("times new roman", 18),
#         bg="black",
#         fg="yellow",
#         height=2,
#         width=12,
#         relief=RIDGE,
#     )
#     takeImg.place(x=130, y=350)

#     def train_image():
#         trainImage.TrainImage(
#             haarcasecade_path,
#             trainimage_path,
#             trainimagelabel_path,
#             message,
#             text_to_speech,
#         )

#     # train Image function call
#     trainImg = tk.Button(
#         ImageUI,
#         text="Train Image",
#         command=train_image,
#         bd=10,
#         font=("times new roman", 18),
#         bg="black",
#         fg="yellow",
#         height=2,
#         width=12,
#         relief=RIDGE,
#     )
#     trainImg.place(x=360, y=350)

# r = tk.Button(
#     window,
#     text="Register a new student",
#     command=TakeImageUI,
#     bd=10,
#     font=("times new roman", 16),
#     bg="black",
#     fg="yellow",
#     height=2,
#     width=17,
# )
# r.place(x=100, y=520)

# def automatic_attedance():
#     automaticAttedance.subjectChoose(text_to_speech)

# r = tk.Button(
#     window,
#     text="Take Attendance",
#     command=automatic_attedance,
#     bd=10,
#     font=("times new roman", 16),
#     bg="black",
#     fg="yellow",
#     height=2,
#     width=17,
# )
# r.place(x=600, y=520)

# def view_attendance():
#     show_attendance.subjectchoose(text_to_speech)

# r = tk.Button(
#     window,
#     text="View Attendance",
#     command=view_attendance,
#     bd=10,
#     font=("times new roman", 16),
#     bg="black",
#     fg="yellow",
#     height=2,
#     width=17,
# )
# r.place(x=1000, y=520)
# r = tk.Button(
#     window,
#     text="EXIT",
#     bd=10,
#     command=quit,
#     font=("times new roman", 16),
#     bg="black",
#     fg="yellow",
#     height=2,
#     width=17,
# )
# r.place(x=600, y=660)
# window.mainloop()






# import os
# import cv2
# import sqlite3
# import tkinter as tk
# from tkinter import ttk, messagebox, filedialog
# from PIL import Image, ImageTk
# from datetime import datetime

# # ------------------ CONSTANTS & PATHS ------------------ #
# DB_PATH = "attendance.db"
# TRAINING_IMG_DIR = "TrainingImage"
# TRAINER_DIR = "TrainingImageLabel"
# TRAINER_PATH = os.path.join(TRAINER_DIR, "trainer.yml")
# HAAR_CASCADE_PATH = "haarcascade_frontalface_default.xml"  # put your haarcascade here


# # ------------------ DATABASE SETUP ------------------ #
# def init_db():
#     conn = sqlite3.connect(DB_PATH)
#     cur = conn.cursor()

#     cur.execute("""
#         CREATE TABLE IF NOT EXISTS students (
#             id INTEGER PRIMARY KEY AUTOINCREMENT,
#             roll TEXT NOT NULL,
#             name TEXT NOT NULL,
#             department TEXT,
#             created_at TEXT
#         )
#     """)

#     cur.execute("""
#         CREATE TABLE IF NOT EXISTS attendance (
#             id INTEGER PRIMARY KEY AUTOINCREMENT,
#             student_id INTEGER,
#             timestamp TEXT,
#             status TEXT,
#             FOREIGN KEY(student_id) REFERENCES students(id)
#         )
#     """)

#     conn.commit()
#     conn.close()


# # ------------------ MAIN APP CLASS ------------------ #
# class AttendanceApp(tk.Tk):
#     def __init__(self):
#         super().__init__()

#         self.title("Face Recognition Attendance System")
#         self.geometry("1100x650")
#         self.configure(bg="#F5F7FB")

#         # init db & folders
#         init_db()
#         os.makedirs(TRAINING_IMG_DIR, exist_ok=True)
#         os.makedirs(TRAINER_DIR, exist_ok=True)

#         self._build_layout()

#     # ---------- UI Layout ---------- #
#     def _build_layout(self):
#         # Sidebar (left)
#         sidebar = tk.Frame(self, bg="#0F4C81", width=220)
#         sidebar.pack(side="left", fill="y")

#         logo = tk.Label(
#             sidebar,
#             text="Attendance\nSystem",
#             bg="#0F4C81",
#             fg="white",
#             font=("Segoe UI", 16, "bold"),
#             justify="left"
#         )
#         logo.pack(pady=30, padx=20, anchor="w")

#         btn_cfg = {
#             "font": ("Segoe UI", 11),
#             "bg": "#0F4C81",
#             "fg": "white",
#             "activebackground": "#145A93",
#             "activeforeground": "white",
#             "bd": 0,
#             "relief": "flat",
#             "anchor": "w",
#             "padx": 20,
#         }

#         tk.Button(sidebar, text="📊 Dashboard", command=self.show_dashboard, **btn_cfg).pack(fill="x", pady=5)
#         tk.Button(sidebar, text="🧑‍🎓 Register Student", command=self.show_register, **btn_cfg).pack(fill="x", pady=5)
#         tk.Button(sidebar, text="🧠 Train Model", command=self.show_train, **btn_cfg).pack(fill="x", pady=5)
#         tk.Button(sidebar, text="📸 Take Attendance", command=self.show_attendance, **btn_cfg).pack(fill="x", pady=5)
#         tk.Button(sidebar, text="📁 View Attendance", command=self.show_view_attendance, **btn_cfg).pack(fill="x", pady=5)

#         tk.Label(sidebar, text="© Your Name / College", bg="#0F4C81", fg="#D0E4FF",
#                  font=("Segoe UI", 8)).pack(side="bottom", pady=10)

#         # Main container (right)
#         self.content = tk.Frame(self, bg="#F5F7FB")
#         self.content.pack(side="left", fill="both", expand=True)

#         self.frames = {}

#         for F in (DashboardPage, RegisterPage, TrainPage, TakeAttendancePage, ViewAttendancePage):
#             frame = F(parent=self.content, controller=self)
#             self.frames[F.__name__] = frame
#             frame.grid(row=0, column=0, sticky="nsew")

#         self.show_dashboard()

#     def show_frame(self, name):
#         frame = self.frames[name]
#         frame.tkraise()

#     def show_dashboard(self):
#         self.show_frame("DashboardPage")

#     def show_register(self):
#         self.show_frame("RegisterPage")

#     def show_train(self):
#         self.show_frame("TrainPage")

#     def show_attendance(self):
#         self.show_frame("TakeAttendancePage")

#     def show_view_attendance(self):
#         self.show_frame("ViewAttendancePage")


# # ------------------ DASHBOARD PAGE ------------------ #
# class DashboardPage(tk.Frame):
#     def __init__(self, parent, controller):
#         super().__init__(parent, bg="#F5F7FB")
#         self.controller = controller

#         title = tk.Label(self, text="📊 Dashboard", bg="#F5F7FB",
#                          fg="#0F4C81", font=("Segoe UI", 20, "bold"))
#         title.pack(pady=20, anchor="w", padx=20)

#         # Cards
#         card_frame = tk.Frame(self, bg="#F5F7FB")
#         card_frame.pack(pady=10, padx=20, fill="x")

#         self.total_students_var = tk.StringVar(value="0")
#         self.total_today_var = tk.StringVar(value="0")

#         card1 = self._build_card(card_frame, "Total Students", self.total_students_var)
#         card2 = self._build_card(card_frame, "Today Attendance", self.total_today_var)

#         card1.pack(side="left", padx=10, fill="x", expand=True)
#         card2.pack(side="left", padx=10, fill="x", expand=True)

#         self.refresh_stats()

#     def _build_card(self, parent, title, value_var):
#         frame = tk.Frame(parent, bg="white", bd=0, relief="solid")
#         frame.configure(highlightbackground="#E1E7F0", highlightthickness=1)
#         frame.pack_propagate(False)
#         frame.config(height=100)

#         tk.Label(frame, text=title, bg="white", fg="#4A4A4A",
#                  font=("Segoe UI", 11, "bold")).pack(anchor="w", padx=15, pady=(12, 0))
#         tk.Label(frame, textvariable=value_var, bg="white", fg="#0F4C81",
#                  font=("Segoe UI", 22, "bold")).pack(anchor="w", padx=15, pady=(5, 10))

#         return frame

#     def refresh_stats(self):
#         conn = sqlite3.connect(DB_PATH)
#         cur = conn.cursor()

#         cur.execute("SELECT COUNT(*) FROM students")
#         total_students = cur.fetchone()[0] or 0

#         today = datetime.now().strftime("%Y-%m-%d")
#         cur.execute("SELECT COUNT(*) FROM attendance WHERE date(timestamp)=?", (today,))
#         total_today = cur.fetchone()[0] or 0

#         conn.close()

#         self.total_students_var.set(str(total_students))
#         self.total_today_var.set(str(total_today))


# # ------------------ REGISTER STUDENT PAGE ------------------ #
# class RegisterPage(tk.Frame):
#     def __init__(self, parent, controller):
#         super().__init__(parent, bg="#F5F7FB")
#         self.controller = controller

#         title = tk.Label(self, text="🧑‍🎓 Register Student", bg="#F5F7FB",
#                          fg="#0F4C81", font=("Segoe UI", 20, "bold"))
#         title.pack(pady=20, anchor="w", padx=20)

#         form = tk.Frame(self, bg="white")
#         form.pack(padx=20, pady=10, fill="x")
#         form.configure(highlightbackground="#E1E7F0", highlightthickness=1)

#         tk.Label(form, text="Roll No", bg="white", fg="#555",
#                  font=("Segoe UI", 11)).grid(row=0, column=0, padx=15, pady=10, sticky="w")
#         tk.Label(form, text="Name", bg="white", fg="#555",
#                  font=("Segoe UI", 11)).grid(row=1, column=0, padx=15, pady=10, sticky="w")
#         tk.Label(form, text="Department", bg="white", fg="#555",
#                  font=("Segoe UI", 11)).grid(row=2, column=0, padx=15, pady=10, sticky="w")

#         self.roll_var = tk.StringVar()
#         self.name_var = tk.StringVar()
#         self.dept_var = tk.StringVar()

#         entry_style = {"font": ("Segoe UI", 11), "bd": 1, "relief": "solid"}
#         tk.Entry(form, textvariable=self.roll_var, **entry_style).grid(row=0, column=1, padx=15, pady=10, sticky="ew")
#         tk.Entry(form, textvariable=self.name_var, **entry_style).grid(row=1, column=1, padx=15, pady=10, sticky="ew")
#         tk.Entry(form, textvariable=self.dept_var, **entry_style).grid(row=2, column=1, padx=15, pady=10, sticky="ew")

#         form.grid_columnconfigure(1, weight=1)

#         btn_frame = tk.Frame(form, bg="white")
#         btn_frame.grid(row=3, column=0, columnspan=2, pady=15, sticky="e", padx=15)

#         save_btn = tk.Button(
#             btn_frame,
#             text="Save & Capture Faces",
#             bg="#0F4C81",
#             fg="white",
#             font=("Segoe UI", 11, "bold"),
#             padx=15,
#             pady=6,
#             bd=0,
#             activebackground="#145A93",
#             activeforeground="white",
#             command=self.save_and_capture
#         )
#         save_btn.pack(side="right")

#     def save_and_capture(self):
#         roll = self.roll_var.get().strip()
#         name = self.name_var.get().strip()
#         dept = self.dept_var.get().strip()

#         if not roll or not name:
#             messagebox.showwarning("Validation", "Roll No and Name are required.")
#             return

#         conn = sqlite3.connect(DB_PATH)
#         cur = conn.cursor()

#         cur.execute("INSERT INTO students (roll, name, department, created_at) VALUES (?, ?, ?, ?)",
#                     (roll, name, dept, datetime.now().isoformat()))
#         student_id = cur.lastrowid

#         conn.commit()
#         conn.close()

#         messagebox.showinfo("Saved", f"Student saved with ID: {student_id}\nNow capturing face images.")
#         self.capture_images(student_id)

#     def capture_images(self, student_id):
#         if not os.path.exists(HAAR_CASCADE_PATH):
#             messagebox.showerror("Error", f"Haarcascade file not found at:\n{HAAR_CASCADE_PATH}")
#             return

#         face_cascade = cv2.CascadeClassifier(HAAR_CASCADE_PATH)
#         cam = cv2.VideoCapture(0)

#         count = 0
#         messagebox.showinfo("Instructions", "Camera will open.\nLook at the camera.\nPress 'q' to stop early.")

#         while True:
#             ret, img = cam.read()
#             if not ret:
#                 break

#             gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#             faces = face_cascade.detectMultiScale(gray, 1.3, 5)

#             for (x, y, w, h) in faces:
#                 count += 1
#                 face_img = gray[y:y+h, x:x+w]
#                 filename = os.path.join(TRAINING_IMG_DIR, f"{student_id}.{count}.jpg")
#                 cv2.imwrite(filename, face_img)
#                 cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)

#             cv2.imshow("Capturing Faces (Press q to exit)", img)

#             if cv2.waitKey(1) & 0xFF == ord('q'):
#                 break
#             if count >= 50:
#                 break

#         cam.release()
#         cv2.destroyAllWindows()

#         messagebox.showinfo("Done", f"Captured {count} face images for student ID {student_id}.")


# # ------------------ TRAIN MODEL PAGE ------------------ #
# class TrainPage(tk.Frame):
#     def __init__(self, parent, controller):
#         super().__init__(parent, bg="#F5F7FB")
#         self.controller = controller

#         title = tk.Label(self, text="🧠 Train Model (LBPH)", bg="#F5F7FB",
#                          fg="#0F4C81", font=("Segoe UI", 20, "bold"))
#         title.pack(pady=20, anchor="w", padx=20)

#         card = tk.Frame(self, bg="white")
#         card.pack(padx=20, pady=10, fill="x")
#         card.configure(highlightbackground="#E1E7F0", highlightthickness=1)

#         tk.Label(card, text="Train the LBPH face recognizer using captured images.",
#                  bg="white", fg="#444", font=("Segoe UI", 11)).pack(pady=15, padx=15, anchor="w")

#         train_btn = tk.Button(
#             card,
#             text="▶ Train Model Now",
#             bg="#0F4C81",
#             fg="white",
#             font=("Segoe UI", 12, "bold"),
#             padx=20,
#             pady=8,
#             bd=0,
#             activebackground="#145A93",
#             activeforeground="white",
#             command=self.train_model
#         )
#         train_btn.pack(pady=10, padx=15, anchor="w")

#     def train_model(self):
#         # Collect images and labels
#         image_paths = [os.path.join(TRAINING_IMG_DIR, f) for f in os.listdir(TRAINING_IMG_DIR)
#                        if f.endswith(".jpg") or f.endswith(".png")]

#         if len(image_paths) == 0:
#             messagebox.showwarning("No Data", "No training images found.")
#             return

#         faces = []
#         ids = []

#         for image_path in image_paths:
#             img = Image.open(image_path).convert("L")
#             img_np = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

#             # filename: studentId.count.jpg
#             filename = os.path.basename(image_path)
#             try:
#                 student_id = int(filename.split(".")[0])
#             except ValueError:
#                 continue

#             faces.append(img_np)
#             ids.append(student_id)

#         if len(faces) == 0:
#             messagebox.showwarning("No Valid Images", "Could not find valid training images.")
#             return

#         recognizer = cv2.face.LBPHFaceRecognizer_create()
#         recognizer.train(faces, np.array(ids))

#         recognizer.write(TRAINER_PATH)

#         messagebox.showinfo("Success", f"Training completed and model saved to:\n{TRAINER_PATH}")


# # ------------------ TAKE ATTENDANCE PAGE ------------------ #
# import numpy as np


# class TakeAttendancePage(tk.Frame):
#     def __init__(self, parent, controller):
#         super().__init__(parent, bg="#F5F7FB")
#         self.controller = controller

#         title = tk.Label(self, text="📸 Take Attendance", bg="#F5F7FB",
#                          fg="#0F4C81", font=("Segoe UI", 20, "bold"))
#         title.pack(pady=20, anchor="w", padx=20)

#         card = tk.Frame(self, bg="white")
#         card.pack(padx=20, pady=10, fill="x")
#         card.configure(highlightbackground="#E1E7F0", highlightthickness=1)

#         tk.Label(card, text="Start camera and mark attendance automatically using face recognition.",
#                  bg="white", fg="#444", font=("Segoe UI", 11)).pack(pady=15, padx=15, anchor="w")

#         start_btn = tk.Button(
#             card,
#             text="▶ Start Attendance",
#             bg="#0F4C81",
#             fg="white",
#             font=("Segoe UI", 12, "bold"),
#             padx=20,
#             pady=8,
#             bd=0,
#             activebackground="#145A93",
#             activeforeground="white",
#             command=self.start_attendance
#         )
#         start_btn.pack(pady=10, padx=15, anchor="w")

#     def start_attendance(self):
#         if not os.path.exists(TRAINER_PATH):
#             messagebox.showwarning("Model Missing", "Model not trained yet. Please train the model first.")
#             return

#         if not os.path.exists(HAAR_CASCADE_PATH):
#             messagebox.showerror("Error", f"Haarcascade file not found at:\n{HAAR_CASCADE_PATH}")
#             return

#         recognizer = cv2.face.LBPHFaceRecognizer_create()
#         recognizer.read(TRAINER_PATH)
#         face_cascade = cv2.CascadeClassifier(HAAR_CASCADE_PATH)

#         conn = sqlite3.connect(DB_PATH)
#         cur = conn.cursor()

#         cam = cv2.VideoCapture(0)
#         messagebox.showinfo("Info", "Camera started.\nPress 'q' to stop.")

#         recognized_ids = set()

#         while True:
#             ret, img = cam.read()
#             if not ret:
#                 break

#             gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#             faces = face_cascade.detectMultiScale(gray, 1.2, 5)

#             for (x, y, w, h) in faces:
#                 face_img = gray[y:y+h, x:x+w]
#                 student_id, conf = recognizer.predict(face_img)

#                 if conf < 80:  # lower = better
#                     cur.execute("SELECT name FROM students WHERE id=?", (student_id,))
#                     row = cur.fetchone()
#                     name = row[0] if row else f"ID {student_id}"

#                     cv2.putText(img, f"{name} ({int(conf)})", (x, y-10),
#                                 cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)
#                     cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)

#                     if student_id not in recognized_ids:
#                         recognized_ids.add(student_id)
#                         cur.execute("INSERT INTO attendance (student_id, timestamp, status) VALUES (?, ?, ?)",
#                                     (student_id, datetime.now().isoformat(), "Present"))
#                         conn.commit()
#                 else:
#                     cv2.putText(img, "Unknown", (x, y-10),
#                                 cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)
#                     cv2.rectangle(img, (x, y), (x+w, y+h), (0, 0, 255), 2)

#             cv2.imshow("Attendance (Press q to close)", img)

#             if cv2.waitKey(1) & 0xFF == ord('q'):
#                 break

#         cam.release()
#         cv2.destroyAllWindows()
#         conn.close()

#         messagebox.showinfo("Done", f"Attendance marked for {len(recognized_ids)} students.")


# # ------------------ VIEW ATTENDANCE PAGE ------------------ #
# class ViewAttendancePage(tk.Frame):
#     def __init__(self, parent, controller):
#         super().__init__(parent, bg="#F5F7FB")
#         self.controller = controller

#         title = tk.Label(self, text="📁 View Attendance", bg="#F5F7FB",
#                          fg="#0F4C81", font=("Segoe UI", 20, "bold"))
#         title.pack(pady=20, anchor="w", padx=20)

#         container = tk.Frame(self, bg="white")
#         container.pack(padx=20, pady=10, fill="both", expand=True)
#         container.configure(highlightbackground="#E1E7F0", highlightthickness=1)

#         # Controls
#         top_frame = tk.Frame(container, bg="white")
#         top_frame.pack(fill="x", pady=5, padx=5)

#         self.date_filter_var = tk.StringVar()
#         tk.Label(top_frame, text="Date (YYYY-MM-DD):", bg="white", fg="#444",
#                  font=("Segoe UI", 10)).pack(side="left", padx=5)
#         tk.Entry(top_frame, textvariable=self.date_filter_var,
#                  font=("Segoe UI", 10), bd=1, relief="solid", width=15).pack(side="left")

#         tk.Button(
#             top_frame,
#             text="🔍 Filter",
#             bg="#0F4C81",
#             fg="white",
#             font=("Segoe UI", 10, "bold"),
#             bd=0,
#             padx=10,
#             command=self.load_data
#         ).pack(side="left", padx=6)

#         tk.Button(
#             top_frame,
#             text="💾 Export CSV",
#             bg="#198754",
#             fg="white",
#             font=("Segoe UI", 10, "bold"),
#             bd=0,
#             padx=10,
#             command=self.export_csv
#         ).pack(side="right", padx=6)

#         # Table
#         self.tree = ttk.Treeview(container, columns=("id", "name", "roll", "timestamp", "status"),
#                                  show="headings", height=15)
#         self.tree.heading("id", text="ID")
#         self.tree.heading("name", text="Name")
#         self.tree.heading("roll", text="Roll No")
#         self.tree.heading("timestamp", text="Timestamp")
#         self.tree.heading("status", text="Status")

#         self.tree.column("id", width=50, anchor="center")
#         self.tree.column("name", width=160)
#         self.tree.column("roll", width=100)
#         self.tree.column("timestamp", width=200)
#         self.tree.column("status", width=80, anchor="center")

#         style = ttk.Style(self)
#         style.configure("Treeview", font=("Segoe UI", 10), rowheight=24)
#         style.configure("Treeview.Heading", font=("Segoe UI", 10, "bold"))

#         self.tree.pack(fill="both", expand=True, padx=5, pady=5)

#         self.load_data()

#     def load_data(self):
#         for row in self.tree.get_children():
#             self.tree.delete(row)

#         conn = sqlite3.connect(DB_PATH)
#         cur = conn.cursor()

#         if self.date_filter_var.get().strip():
#             date_str = self.date_filter_var.get().strip()
#             cur.execute("""
#                 SELECT a.id, s.name, s.roll, a.timestamp, a.status
#                 FROM attendance a
#                 JOIN students s ON a.student_id = s.id
#                 WHERE date(a.timestamp) = ?
#                 ORDER BY a.timestamp DESC
#             """, (date_str,))
#         else:
#             cur.execute("""
#                 SELECT a.id, s.name, s.roll, a.timestamp, a.status
#                 FROM attendance a
#                 JOIN students s ON a.student_id = s.id
#                 ORDER BY a.timestamp DESC
#             """)

#         rows = cur.fetchall()
#         conn.close()

#         for r in rows:
#             self.tree.insert("", "end", values=r)

#     def export_csv(self):
#         import csv

#         file_path = filedialog.asksaveasfilename(
#             defaultextension=".csv",
#             filetypes=[("CSV files", "*.csv")],
#             title="Save attendance as CSV"
#         )
#         if not file_path:
#             return

#         conn = sqlite3.connect(DB_PATH)
#         cur = conn.cursor()
#         cur.execute("""
#             SELECT a.id, s.name, s.roll, a.timestamp, a.status
#             FROM attendance a
#             JOIN students s ON a.student_id = s.id
#             ORDER BY a.timestamp DESC
#         """)
#         rows = cur.fetchall()
#         conn.close()

#         with open(file_path, "w", newline="", encoding="utf-8") as f:
#             writer = csv.writer(f)
#             writer.writerow(["ID", "Name", "Roll No", "Timestamp", "Status"])
#             writer.writerows(rows)

#         messagebox.showinfo("Exported", f"Attendance exported to:\n{file_path}")


# # ------------------ MAIN ENTRY ------------------ #
# if __name__ == "__main__":
#     app = AttendanceApp()
#     app.mainloop()













import os
import cv2
import sqlite3
import tkinter as tk
from tkinter import ttk, messagebox, filedialog
from PIL import Image, ImageTk
from datetime import datetime, timedelta
import numpy as np

# For graphs + PDF
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas as pdf_canvas

# ------------------ CONSTANTS & PATHS ------------------ #
DB_PATH = "attendance.db"
TRAINING_IMG_DIR = "TrainingImage"
TRAINER_DIR = "TrainingImageLabel"
TRAINER_PATH = os.path.join(TRAINER_DIR, "trainer.yml")
HAAR_CASCADE_PATH = "haarcascade_frontalface_default.xml"  # put your haarcascade file here

APP_PRIMARY = "#0F4C81"
APP_BG = "#F5F7FB"
CARD_BORDER = "#E1E7F0"
TEXT_DARK = "#333333"


# ------------------ DATABASE SETUP ------------------ #
def init_db():
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()

    cur.execute("""
        CREATE TABLE IF NOT EXISTS students (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            roll TEXT NOT NULL,
            name TEXT NOT NULL,
            department TEXT,
            created_at TEXT
        )
    """)

    cur.execute("""
        CREATE TABLE IF NOT EXISTS attendance (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            student_id INTEGER,
            timestamp TEXT,
            status TEXT,
            FOREIGN KEY(student_id) REFERENCES students(id)
        )
    """)

    conn.commit()
    conn.close()


# ------------------ LOGIN WINDOW ------------------ #
class LoginWindow(tk.Tk):
    """
    Simple login to choose role: admin / faculty
    Credentials:
        admin   / admin123
        faculty / fac123
    """

    def __init__(self):
        super().__init__()
        self.title("Login - Attendance System")
        self.geometry("420x320")
        self.configure(bg=APP_BG)
        self.resizable(False, False)

        self.role = None

        self._build_ui()

    def _build_ui(self):
        card = tk.Frame(self, bg="white")
        card.place(relx=0.5, rely=0.5, anchor="c", width=340, height=240)
        card.configure(highlightbackground=CARD_BORDER, highlightthickness=1)

        title = tk.Label(
            card,
            text="Face Attendance Login",
            bg="white",
            fg=APP_PRIMARY,
            font=("Segoe UI", 16, "bold")
        )
        title.pack(pady=(20, 5))

        subtitle = tk.Label(
            card,
            text="Sign in as Admin or Faculty",
            bg="white",
            fg="#777777",
            font=("Segoe UI", 9)
        )
        subtitle.pack(pady=(0, 15))

        form = tk.Frame(card, bg="white")
        form.pack(padx=20, pady=5, fill="x")

        tk.Label(form, text="Username", bg="white", fg=TEXT_DARK,
                 font=("Segoe UI", 10)).grid(row=0, column=0, sticky="w")
        tk.Label(form, text="Password", bg="white", fg=TEXT_DARK,
                 font=("Segoe UI", 10)).grid(row=2, column=0, sticky="w", pady=(10, 0))

        self.user_var = tk.StringVar()
        self.pass_var = tk.StringVar()

        entry_style = {"font": ("Segoe UI", 10), "bd": 1, "relief": "solid"}

        tk.Entry(form, textvariable=self.user_var, **entry_style).grid(
            row=1, column=0, sticky="ew", pady=(2, 0))
        tk.Entry(form, textvariable=self.pass_var, show="•",
                 **entry_style).grid(row=3, column=0, sticky="ew", pady=(2, 0))

        form.grid_columnconfigure(0, weight=1)

        btn = tk.Button(
            card,
            text="Login",
            bg=APP_PRIMARY,
            fg="white",
            font=("Segoe UI", 11, "bold"),
            bd=0,
            padx=15,
            pady=6,
            activebackground="#145A93",
            activeforeground="white",
            command=self._on_login
        )
        btn.pack(pady=18)

    def _on_login(self):
        username = self.user_var.get().strip().lower()
        password = self.pass_var.get().strip()

        if username == "admin" and password == "admin123":
            self.role = "Admin"
        elif username == "faculty" and password == "fac123":
            self.role = "Faculty"
        else:
            messagebox.showerror("Login Failed", "Invalid username or password.")
            return

        self.destroy()


# ------------------ MAIN APP CLASS ------------------ #
class AttendanceApp(tk.Tk):
    def __init__(self, role="Admin"):
        super().__init__()

        self.role = role

        self.title("Face Recognition Attendance System")
        self.geometry("1200x700")
        self.configure(bg=APP_BG)

        # init db & folders
        init_db()
        os.makedirs(TRAINING_IMG_DIR, exist_ok=True)
        os.makedirs(TRAINER_DIR, exist_ok=True)

        self._build_layout()

    # ---------- UI Layout ---------- #
    def _build_layout(self):
        # Sidebar (left)
        sidebar = tk.Frame(self, bg=APP_PRIMARY, width=230)
        sidebar.pack(side="left", fill="y")

        # Top logo / brand
        logo = tk.Label(
            sidebar,
            text=" AI Face\nAttendance",
            bg=APP_PRIMARY,
            fg="white",
            font=("Segoe UI", 18, "bold"),
            justify="left"
        )
        logo.pack(pady=(28, 8), padx=20, anchor="w")

        role_lbl = tk.Label(
            sidebar,
            text=f"Signed in as: {self.role}",
            bg=APP_PRIMARY,
            fg="#D0E4FF",
            font=("Segoe UI", 9)
        )
        role_lbl.pack(pady=(0, 25), padx=20, anchor="w")

        btn_cfg = {
            "font": ("Segoe UI", 11),
            "bg": APP_PRIMARY,
            "fg": "white",
            "activebackground": "#145A93",
            "activeforeground": "white",
            "bd": 0,
            "relief": "flat",
            "anchor": "w",
            "padx": 24,
        }

        tk.Button(sidebar, text="📊 Dashboard", command=self.show_dashboard, **btn_cfg).pack(fill="x", pady=4)
        tk.Button(sidebar, text="🧑‍🎓 Register Student", command=self.show_register, **btn_cfg).pack(fill="x", pady=4)
        tk.Button(sidebar, text="🧠 Train Model", command=self.show_train, **btn_cfg).pack(fill="x", pady=4)
        tk.Button(sidebar, text="📸 Take Attendance", command=self.show_attendance, **btn_cfg).pack(fill="x", pady=4)
        tk.Button(sidebar, text="📁 View Attendance", command=self.show_view_attendance, **btn_cfg).pack(fill="x", pady=4)
        tk.Button(sidebar, text="📈 Analytics & Reports", command=self.show_analytics, **btn_cfg).pack(fill="x", pady=4)

        tk.Label(sidebar, text="© Your Name / College", bg=APP_PRIMARY, fg="#D0E4FF",
                 font=("Segoe UI", 8)).pack(side="bottom", pady=10)

        # Main container (right)
        self.content = tk.Frame(self, bg=APP_BG)
        self.content.pack(side="left", fill="both", expand=True)

        # Top bar
        topbar = tk.Frame(self.content, bg="white", height=50)
        topbar.pack(side="top", fill="x")
        topbar.configure(highlightbackground=CARD_BORDER, highlightthickness=1)

        self.page_title_var = tk.StringVar(value="Dashboard")
        tk.Label(topbar, textvariable=self.page_title_var,
                 bg="white", fg=APP_PRIMARY, font=("Segoe UI", 15, "bold")
                 ).pack(side="left", padx=20)

        tk.Label(topbar, text=datetime.now().strftime("%d %b %Y"),
                 bg="white", fg="#777777", font=("Segoe UI", 9)
                 ).pack(side="right", padx=20)

        # Frame container for pages
        self.page_container = tk.Frame(self.content, bg=APP_BG)
        self.page_container.pack(side="top", fill="both", expand=True)

        self.frames = {}

        for F in (DashboardPage, RegisterPage, TrainPage,
                  TakeAttendancePage, ViewAttendancePage, AnalyticsPage):
            frame = F(parent=self.page_container, controller=self)
            self.frames[F.__name__] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_dashboard()

    def show_frame(self, name, title):
        self.page_title_var.set(title)
        frame = self.frames[name]
        if hasattr(frame, "on_show"):
            frame.on_show()
        frame.tkraise()

    def show_dashboard(self):
        self.show_frame("DashboardPage", "Dashboard")

    def show_register(self):
        self.show_frame("RegisterPage", "Register Student")

    def show_train(self):
        self.show_frame("TrainPage", "Train Model")

    def show_attendance(self):
        self.show_frame("TakeAttendancePage", "Take Attendance")

    def show_view_attendance(self):
        self.show_frame("ViewAttendancePage", "Attendance Records")

    def show_analytics(self):
        self.show_frame("AnalyticsPage", "Analytics & Reports")


# ------------------ DASHBOARD PAGE ------------------ #
class DashboardPage(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent, bg=APP_BG)
        self.controller = controller

        # Cards container
        card_frame = tk.Frame(self, bg=APP_BG)
        card_frame.pack(pady=25, padx=22, fill="x")

        self.total_students_var = tk.StringVar(value="0")
        self.total_today_var = tk.StringVar(value="0")
        self.last_attendance_var = tk.StringVar(value="—")

        card1 = self._build_card(card_frame, "Total Students", self.total_students_var)
        card2 = self._build_card(card_frame, "Today Attendance", self.total_today_var)
        card3 = self._build_card(card_frame, "Last Attendance", self.last_attendance_var)

        card1.pack(side="left", padx=8, fill="x", expand=True)
        card2.pack(side="left", padx=8, fill="x", expand=True)
        card3.pack(side="left", padx=8, fill="x", expand=True)

        # Welcome text
        info = tk.Label(
            self,
            text="Welcome to the Face Recognition Attendance System.\n"
                 "Use the left menu to manage students, train the model and take attendance.",
            bg=APP_BG,
            fg="#555555",
            font=("Segoe UI", 11),
            justify="left"
        )
        info.pack(padx=22, pady=10, anchor="w")

    def _build_card(self, parent, title, value_var):
        frame = tk.Frame(parent, bg="white", bd=0, relief="solid")
        frame.configure(highlightbackground=CARD_BORDER, highlightthickness=1)
        frame.pack_propagate(False)
        frame.config(height=100)

        tk.Label(frame, text=title, bg="white", fg="#4A4A4A",
                 font=("Segoe UI", 11, "bold")).pack(anchor="w", padx=15, pady=(12, 0))
        tk.Label(frame, textvariable=value_var, bg="white", fg=APP_PRIMARY,
                 font=("Segoe UI", 22, "bold")).pack(anchor="w", padx=15, pady=(5, 10))

        return frame

    def on_show(self):
        self.refresh_stats()

    def refresh_stats(self):
        conn = sqlite3.connect(DB_PATH)
        cur = conn.cursor()

        cur.execute("SELECT COUNT(*) FROM students")
        total_students = cur.fetchone()[0] or 0

        today = datetime.now().strftime("%Y-%m-%d")
        cur.execute("SELECT COUNT(*) FROM attendance WHERE date(timestamp)=?", (today,))
        total_today = cur.fetchone()[0] or 0

        cur.execute("SELECT timestamp FROM attendance ORDER BY timestamp DESC LIMIT 1")
        row = cur.fetchone()
        last_att = row[0] if row else None

        conn.close()

        self.total_students_var.set(str(total_students))
        self.total_today_var.set(str(total_today))
        self.last_attendance_var.set(last_att.split("T")[0] if last_att else "—")


# ------------------ REGISTER STUDENT PAGE (with photo preview) ------------------ #
class RegisterPage(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent, bg=APP_BG)
        self.controller = controller
        self.preview_img_label = None
        self.preview_photo = None

        card = tk.Frame(self, bg="white")
        card.pack(padx=22, pady=22, fill="x")
        card.configure(highlightbackground=CARD_BORDER, highlightthickness=1)

        tk.Label(card, text="Add / Register New Student",
                 bg="white", fg=APP_PRIMARY, font=("Segoe UI", 15, "bold")
                 ).grid(row=0, column=0, columnspan=2, sticky="w", pady=(18, 5), padx=18)

        tk.Label(card, text="Roll No", bg="white", fg=TEXT_DARK,
                 font=("Segoe UI", 11)).grid(row=1, column=0, padx=18, pady=(10, 6), sticky="w")
        tk.Label(card, text="Name", bg="white", fg=TEXT_DARK,
                 font=("Segoe UI", 11)).grid(row=2, column=0, padx=18, pady=6, sticky="w")
        tk.Label(card, text="Department", bg="white", fg=TEXT_DARK,
                 font=("Segoe UI", 11)).grid(row=3, column=0, padx=18, pady=6, sticky="w")

        self.roll_var = tk.StringVar()
        self.name_var = tk.StringVar()
        self.dept_var = tk.StringVar()

        entry_style = {"font": ("Segoe UI", 11), "bd": 1, "relief": "solid"}

        tk.Entry(card, textvariable=self.roll_var, **entry_style).grid(
            row=1, column=1, padx=18, pady=(10, 6), sticky="ew")
        tk.Entry(card, textvariable=self.name_var, **entry_style).grid(
            row=2, column=1, padx=18, pady=6, sticky="ew")
        tk.Entry(card, textvariable=self.dept_var, **entry_style).grid(
            row=3, column=1, padx=18, pady=6, sticky="ew")

        card.grid_columnconfigure(1, weight=1)

        # Right: photo preview box
        preview_frame = tk.Frame(card, bg="#FAFBFF")
        preview_frame.grid(row=1, column=2, rowspan=3, padx=(10, 18), pady=10, sticky="nsew")
        preview_frame.configure(highlightbackground=CARD_BORDER, highlightthickness=1)

        tk.Label(preview_frame, text="Last Captured Photo",
                 bg="#FAFBFF", fg="#666666", font=("Segoe UI", 10, "bold")
                 ).pack(pady=(6, 4))

        self.preview_img_label = tk.Label(preview_frame, bg="#FAFBFF")
        self.preview_img_label.pack(pady=4, padx=6)

        tk.Label(preview_frame, text="(will update after capture)",
                 bg="#FAFBFF", fg="#999999", font=("Segoe UI", 8)
                 ).pack(pady=(0, 8))

        btn_frame = tk.Frame(card, bg="white")
        btn_frame.grid(row=4, column=0, columnspan=3, pady=(10, 16), sticky="e", padx=18)

        save_btn = tk.Button(
            btn_frame,
            text="Save & Capture Faces",
            bg=APP_PRIMARY,
            fg="white",
            font=("Segoe UI", 11, "bold"),
            padx=15,
            pady=6,
            bd=0,
            activebackground="#145A93",
            activeforeground="white",
            command=self.save_and_capture
        )
        save_btn.pack(side="right")

    def save_and_capture(self):
        roll = self.roll_var.get().strip()
        name = self.name_var.get().strip()
        dept = self.dept_var.get().strip()

        if not roll or not name:
            messagebox.showwarning("Validation", "Roll No and Name are required.")
            return

        conn = sqlite3.connect(DB_PATH)
        cur = conn.cursor()

        cur.execute("INSERT INTO students (roll, name, department, created_at) VALUES (?, ?, ?, ?)",
                    (roll, name, dept, datetime.now().isoformat()))
        student_id = cur.lastrowid

        conn.commit()
        conn.close()

        messagebox.showinfo("Saved", f"Student saved with ID: {student_id}\nNow capturing face images.")
        last_img_path = self.capture_images(student_id)

        if last_img_path:
            self.update_preview(last_img_path)

    def capture_images(self, student_id):
        if not os.path.exists(HAAR_CASCADE_PATH):
            messagebox.showerror("Error", f"Haarcascade file not found at:\n{HAAR_CASCADE_PATH}")
            return None

        face_cascade = cv2.CascadeClassifier(HAAR_CASCADE_PATH)
        cam = cv2.VideoCapture(0)

        count = 0
        last_img_path = None
        messagebox.showinfo("Instructions", "Camera will open.\nLook at the camera.\nPress 'q' to stop early.")

        while True:
            ret, img = cam.read()
            if not ret:
                break

            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            faces = face_cascade.detectMultiScale(gray, 1.3, 5)

            for (x, y, w, h) in faces:
                count += 1
                face_img = gray[y:y + h, x:x + w]
                filename = os.path.join(TRAINING_IMG_DIR, f"{student_id}.{count}.jpg")
                cv2.imwrite(filename, face_img)
                last_img_path = filename
                cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)

            cv2.imshow("Capturing Faces (Press q to exit)", img)

            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
            if count >= 50:
                break

        cam.release()
        cv2.destroyAllWindows()

        messagebox.showinfo("Done", f"Captured {count} face images for student ID {student_id}.")
        return last_img_path

    def update_preview(self, img_path):
        if not os.path.exists(img_path):
            return
        img = Image.open(img_path)
        img = img.resize((140, 140))
        self.preview_photo = ImageTk.PhotoImage(img)
        self.preview_img_label.config(image=self.preview_photo)


# ------------------ TRAIN MODEL PAGE ------------------ #
class TrainPage(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent, bg=APP_BG)
        self.controller = controller

        card = tk.Frame(self, bg="white")
        card.pack(padx=22, pady=22, fill="x")
        card.configure(highlightbackground=CARD_BORDER, highlightthickness=1)

        tk.Label(card, text="Train Model (LBPH Face Recognizer)",
                 bg="white", fg=APP_PRIMARY, font=("Segoe UI", 15, "bold")
                 ).pack(pady=(18, 8), padx=18, anchor="w")

        tk.Label(card, text="Train the LBPH face recognizer using captured student images.",
                 bg="white", fg="#444444", font=("Segoe UI", 11)
                 ).pack(pady=(0, 12), padx=18, anchor="w")

        train_btn = tk.Button(
            card,
            text="▶ Train Model Now",
            bg=APP_PRIMARY,
            fg="white",
            font=("Segoe UI", 12, "bold"),
            padx=20,
            pady=8,
            bd=0,
            activebackground="#145A93",
            activeforeground="white",
            command=self.train_model
        )
        train_btn.pack(pady=(4, 18), padx=18, anchor="w")

    def train_model(self):
        image_paths = [os.path.join(TRAINING_IMG_DIR, f) for f in os.listdir(TRAINING_IMG_DIR)
                       if f.lower().endswith((".jpg", ".png"))]

        if len(image_paths) == 0:
            messagebox.showwarning("No Data", "No training images found.")
            return

        faces = []
        ids = []

        for image_path in image_paths:
            img_np = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
            if img_np is None:
                continue

            filename = os.path.basename(image_path)
            try:
                student_id = int(filename.split(".")[0])
            except ValueError:
                continue

            faces.append(img_np)
            ids.append(student_id)

        if len(faces) == 0:
            messagebox.showwarning("No Valid Images", "Could not find valid training images.")
            return

        recognizer = cv2.face.LBPHFaceRecognizer_create()
        recognizer.train(faces, np.array(ids))
        recognizer.write(TRAINER_PATH)

        messagebox.showinfo("Success", f"Training completed and model saved to:\n{TRAINER_PATH}")


# ------------------ TAKE ATTENDANCE PAGE ------------------ #
class TakeAttendancePage(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent, bg=APP_BG)
        self.controller = controller

        card = tk.Frame(self, bg="white")
        card.pack(padx=22, pady=22, fill="x")
        card.configure(highlightbackground=CARD_BORDER, highlightthickness=1)

        tk.Label(card, text="Take Attendance",
                 bg="white", fg=APP_PRIMARY, font=("Segoe UI", 15, "bold")
                 ).pack(pady=(18, 8), padx=18, anchor="w")

        tk.Label(card, text="Start camera and mark attendance automatically using face recognition.",
                 bg="white", fg="#444444", font=("Segoe UI", 11)
                 ).pack(pady=(0, 12), padx=18, anchor="w")

        start_btn = tk.Button(
            card,
            text="▶ Start Attendance",
            bg=APP_PRIMARY,
            fg="white",
            font=("Segoe UI", 12, "bold"),
            padx=20,
            pady=8,
            bd=0,
            activebackground="#145A93",
            activeforeground="white",
            command=self.start_attendance
        )
        start_btn.pack(pady=(4, 18), padx=18, anchor="w")

    def start_attendance(self):
        if not os.path.exists(TRAINER_PATH):
            messagebox.showwarning("Model Missing", "Model not trained yet. Please train the model first.")
            return

        if not os.path.exists(HAAR_CASCADE_PATH):
            messagebox.showerror("Error", f"Haarcascade file not found at:\n{HAAR_CASCADE_PATH}")
            return

        recognizer = cv2.face.LBPHFaceRecognizer_create()
        recognizer.read(TRAINER_PATH)
        face_cascade = cv2.CascadeClassifier(HAAR_CASCADE_PATH)

        conn = sqlite3.connect(DB_PATH)
        cur = conn.cursor()

        cam = cv2.VideoCapture(0)
        messagebox.showinfo("Info", "Camera started.\nPress 'q' to stop.")

        recognized_ids = set()

        while True:
            ret, img = cam.read()
            if not ret:
                break

            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            faces = face_cascade.detectMultiScale(gray, 1.2, 5)

            for (x, y, w, h) in faces:
                face_img = gray[y:y + h, x:x + w]
                student_id, conf = recognizer.predict(face_img)

                if conf < 80:
                    cur.execute("SELECT name FROM students WHERE id=?", (student_id,))
                    row = cur.fetchone()
                    name = row[0] if row else f"ID {student_id}"

                    cv2.putText(img, f"{name} ({int(conf)})", (x, y - 10),
                                cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)
                    cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)

                    if student_id not in recognized_ids:
                        recognized_ids.add(student_id)
                        cur.execute("INSERT INTO attendance (student_id, timestamp, status) VALUES (?, ?, ?)",
                                    (student_id, datetime.now().isoformat(), "Present"))
                        conn.commit()
                else:
                    cv2.putText(img, "Unknown", (x, y - 10),
                                cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)
                    cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 2)

            cv2.imshow("Attendance (Press q to close)", img)

            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

        cam.release()
        cv2.destroyAllWindows()
        conn.close()

        messagebox.showinfo("Done", f"Attendance marked for {len(recognized_ids)} students.")


# ------------------ VIEW ATTENDANCE PAGE (with photo preview + PDF) ------------------ #
class ViewAttendancePage(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent, bg=APP_BG)
        self.controller = controller

        container = tk.Frame(self, bg="white")
        container.pack(padx=22, pady=22, fill="both", expand=True)
        container.configure(highlightbackground=CARD_BORDER, highlightthickness=1)

        # Controls
        top_frame = tk.Frame(container, bg="white")
        top_frame.pack(fill="x", pady=5, padx=8)

        self.date_filter_var = tk.StringVar()
        tk.Label(top_frame, text="Date (YYYY-MM-DD):", bg="white", fg="#444",
                 font=("Segoe UI", 10)).pack(side="left", padx=5)
        tk.Entry(top_frame, textvariable=self.date_filter_var,
                 font=("Segoe UI", 10), bd=1, relief="solid", width=15).pack(side="left")

        tk.Button(
            top_frame,
            text="🔍 Filter",
            bg=APP_PRIMARY,
            fg="white",
            font=("Segoe UI", 10, "bold"),
            bd=0,
            padx=10,
            command=self.load_data
        ).pack(side="left", padx=6)

        tk.Button(
            top_frame,
            text="💾 Export CSV",
            bg="#198754",
            fg="white",
            font=("Segoe UI", 10, "bold"),
            bd=0,
            padx=10,
            command=self.export_csv
        ).pack(side="right", padx=6)

        tk.Button(
            top_frame,
            text="📄 Export PDF",
            bg="#6C2BD9",
            fg="white",
            font=("Segoe UI", 10, "bold"),
            bd=0,
            padx=10,
            command=self.export_pdf
        ).pack(side="right", padx=6)

        # Split table + right panel
        body = tk.Frame(container, bg="white")
        body.pack(fill="both", expand=True, padx=5, pady=(0, 8))

        # Table
        self.tree = ttk.Treeview(body, columns=("id", "name", "roll", "timestamp", "status"),
                                 show="headings", height=15)
        self.tree.heading("id", text="ID")
        self.tree.heading("name", text="Name")
        self.tree.heading("roll", text="Roll No")
        self.tree.heading("timestamp", text="Timestamp")
        self.tree.heading("status", text="Status")

        self.tree.column("id", width=50, anchor="center")
        self.tree.column("name", width=160)
        self.tree.column("roll", width=100)
        self.tree.column("timestamp", width=200)
        self.tree.column("status", width=80, anchor="center")

        style = ttk.Style(self)
        style.configure("Treeview", font=("Segoe UI", 10), rowheight=24)
        style.configure("Treeview.Heading", font=("Segoe UI", 10, "bold"))

        self.tree.bind("<<TreeviewSelect>>", self.on_row_select)

        self.tree.pack(side="left", fill="both", expand=True, padx=(0, 8))

        # Right: student photo preview
        preview = tk.Frame(body, bg="#FAFBFF", width=220)
        preview.pack(side="right", fill="y")
        preview.configure(highlightbackground=CARD_BORDER, highlightthickness=1)

        tk.Label(preview, text="Student Photo",
                 bg="#FAFBFF", fg="#666666", font=("Segoe UI", 11, "bold")
                 ).pack(pady=(10, 5))

        self.photo_label = tk.Label(preview, bg="#FAFBFF")
        self.photo_label.pack(pady=5, padx=10)

        self.photo_preview = None

        tk.Label(preview, text="(First training image found\nfor selected student)",
                 bg="#FAFBFF", fg="#999999", font=("Segoe UI", 8), justify="center"
                 ).pack(pady=(0, 10))

        self.load_data()

    def on_show(self):
        self.load_data()

    def load_data(self):
        for row in self.tree.get_children():
            self.tree.delete(row)

        conn = sqlite3.connect(DB_PATH)
        cur = conn.cursor()

        if self.date_filter_var.get().strip():
            date_str = self.date_filter_var.get().strip()
            cur.execute("""
                SELECT a.id, s.name, s.roll, a.timestamp, a.status, s.id
                FROM attendance a
                JOIN students s ON a.student_id = s.id
                WHERE date(a.timestamp) = ?
                ORDER BY a.timestamp DESC
            """, (date_str,))
        else:
            cur.execute("""
                SELECT a.id, s.name, s.roll, a.timestamp, a.status, s.id
                FROM attendance a
                JOIN students s ON a.student_id = s.id
                ORDER BY a.timestamp DESC
            """)

        rows = cur.fetchall()
        conn.close()

        for r in rows:
            # store student_id in "values" but hidden (extra at end)
            self.tree.insert("", "end", values=r[:-1], tags=(f"sid_{r[-1]}",))

    def export_csv(self):
        import csv

        file_path = filedialog.asksaveasfilename(
            defaultextension=".csv",
            filetypes=[("CSV files", "*.csv")],
            title="Save attendance as CSV"
        )
        if not file_path:
            return

        conn = sqlite3.connect(DB_PATH)
        cur = conn.cursor()
        cur.execute("""
            SELECT a.id, s.name, s.roll, a.timestamp, a.status
            FROM attendance a
            JOIN students s ON a.student_id = s.id
            ORDER BY a.timestamp DESC
        """)
        rows = cur.fetchall()
        conn.close()

        with open(file_path, "w", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow(["ID", "Name", "Roll No", "Timestamp", "Status"])
            writer.writerows(rows)

        messagebox.showinfo("Exported", f"Attendance exported to:\n{file_path}")

    def export_pdf(self):
        file_path = filedialog.asksaveasfilename(
            defaultextension=".pdf",
            filetypes=[("PDF files", "*.pdf")],
            title="Save attendance report as PDF"
        )
        if not file_path:
            return

        conn = sqlite3.connect(DB_PATH)
        cur = conn.cursor()
        cur.execute("""
            SELECT a.id, s.name, s.roll, a.timestamp, a.status
            FROM attendance a
            JOIN students s ON a.student_id = s.id
            ORDER BY a.timestamp DESC
        """)
        rows = cur.fetchall()
        conn.close()

        c = pdf_canvas.Canvas(file_path, pagesize=A4)
        width, height = A4

        c.setFont("Helvetica-Bold", 16)
        c.drawString(40, height - 50, "Attendance Report")

        c.setFont("Helvetica", 10)
        c.drawString(40, height - 70, f"Generated on: {datetime.now().strftime('%d-%m-%Y %H:%M')}")

        y = height - 100
        c.setFont("Helvetica-Bold", 10)
        headers = ["ID", "Name", "Roll No", "Timestamp", "Status"]
        x_positions = [40, 80, 250, 330, 480]

        for x, header in zip(x_positions, headers):
            c.drawString(x, y, header)

        c.setFont("Helvetica", 9)
        y -= 15

        for row in rows:
            if y < 60:
                c.showPage()
                y = height - 60
                c.setFont("Helvetica-Bold", 10)
                for x, header in zip(x_positions, headers):
                    c.drawString(x, y, header)
                c.setFont("Helvetica", 9)
                y -= 15

            for x, cell in zip(x_positions, row):
                c.drawString(x, y, str(cell))
            y -= 14

        c.save()
        messagebox.showinfo("Exported", f"PDF report exported to:\n{file_path}")

    def on_row_select(self, event):
        selected = self.tree.selection()
        if not selected:
            return

        item_id = selected[0]
        # Example of tag: ('sid_3',)
        tags = self.tree.item(item_id, "tags")
        student_id = None
        if tags:
            tag = tags[0]
            if tag.startswith("sid_"):
                try:
                    student_id = int(tag.split("_")[1])
                except ValueError:
                    pass

        if not student_id:
            return

        # find first training image for that student
        img_path = None
        for f in os.listdir(TRAINING_IMG_DIR):
            if f.startswith(str(student_id) + "."):
                img_path = os.path.join(TRAINING_IMG_DIR, f)
                break

        if img_path and os.path.exists(img_path):
            img = Image.open(img_path)
            img = img.resize((160, 160))
            self.photo_preview = ImageTk.PhotoImage(img)
            self.photo_label.config(image=self.photo_preview)
        else:
            self.photo_label.config(image="", text="No image found")


# ------------------ ANALYTICS & GRAPHS PAGE ------------------ #
class AnalyticsPage(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent, bg=APP_BG)
        self.controller = controller
        self.figure = None
        self.canvas = None

        container = tk.Frame(self, bg="white")
        container.pack(padx=22, pady=22, fill="both", expand=True)
        container.configure(highlightbackground=CARD_BORDER, highlightthickness=1)

        tk.Label(container, text="Attendance Analytics",
                 bg="white", fg=APP_PRIMARY, font=("Segoe UI", 15, "bold")
                 ).pack(pady=(18, 5), padx=18, anchor="w")

        tk.Label(container, text="Attendance per day (last 10 days)",
                 bg="white", fg="#555555", font=("Segoe UI", 10)
                 ).pack(pady=(0, 10), padx=18, anchor="w")

        self.chart_frame = tk.Frame(container, bg="white")
        self.chart_frame.pack(fill="both", expand=True, padx=18, pady=(0, 18))

    def on_show(self):
        self.draw_chart()

    def draw_chart(self):
        for widget in self.chart_frame.winfo_children():
            widget.destroy()

        dates = []
        counts = []

        conn = sqlite3.connect(DB_PATH)
        cur = conn.cursor()

        today = datetime.now().date()
        days_back = 10

        for i in range(days_back - 1, -1, -1):
            day = today - timedelta(days=i)
            day_str = day.strftime("%Y-%m-%d")
            cur.execute("SELECT COUNT(*) FROM attendance WHERE date(timestamp)=?", (day_str,))
            cnt = cur.fetchone()[0] or 0
            dates.append(day.strftime("%d-%b"))
            counts.append(cnt)

        conn.close()

        # Create matplotlib figure
        self.figure = plt.Figure(figsize=(6, 3.5))
        ax = self.figure.add_subplot(111)
        ax.plot(dates, counts, marker="o")
        ax.set_xlabel("Date")
        ax.set_ylabel("Attendance Count")
        ax.set_title("Last 10 Days Attendance")
        ax.grid(True)

        self.canvas = FigureCanvasTkAgg(self.figure, master=self.chart_frame)
        self.canvas.draw()
        self.canvas.get_tk_widget().pack(fill="both", expand=True)


# ------------------ MAIN ENTRY ------------------ #
if __name__ == "__main__":
    # 1) Show login
    login = LoginWindow()
    login.mainloop()

    # 2) If user logged in successfully, open main app
    if login.role:
        app = AttendanceApp(role=login.role)
        app.mainloop()





