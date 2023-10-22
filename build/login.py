import tkinter as tk
import sqlite3 as sq
from tkinter import messagebox

# Create the main application window
app = tk.Tk()
app.title("Login/Signup Page")

# Function to handle login button click
def login():
    username = username_entry.get()
    password = password_entry.get()
    
    if username == "your_username" and password == "your_password":
        messagebox.showinfo("Login Successful", "Welcome, " + username + "!")
    else:
        messagebox.showerror("Login Failed", "Invalid username or password")

# Function to handle signup button click
def signup():
    new_username = new_username_entry.get()
    new_password = new_password_entry.get()
    new_email = new_email_entry.get()
    new_age = new_age_entry.get()
    
    # You can save the new_username and new_password to a file or database here 
    conn = sq.connect("Autoscheduler.db")
    cursor = conn.cursor()
    cursor.execute('''INSERT INTO Users(Username,Password,Age,Email_Id) VALUES(%s,%s,%s,%s) ''',(new_username,new_password,new_age,new_email))       
    conn.commit()
    conn.close()
    
# Create frames
login_frame = tk.Frame(app)
login_frame.pack(pady=10)
signup_frame = tk.Frame(app)
signup_frame.pack(pady=10)

# Login frame widgets
tk.Label(login_frame, text="Login").grid(row=0, column=0, columnspan=2)
tk.Label(login_frame, text="Username:").grid(row=1, column=0)
username_entry = tk.Entry(login_frame)
username_entry.grid(row=1, column=1)
tk.Label(login_frame, text="Password:").grid(row=2, column=0)
password_entry = tk.Entry(login_frame, show="*")
password_entry.grid(row=2, column=1)
login_button = tk.Button(login_frame, text="Login", command=login)
login_button.grid(row=3, column=0, columnspan=2)

# Signup frame widgets
tk.Label(signup_frame, text="Signup").grid(row=0, column=0, columnspan=2)
tk.Label(signup_frame, text="New Username:").grid(row=1, column=0)
new_username_entry = tk.Entry(signup_frame)
new_username_entry.grid(row=1, column=1)
tk.Label(signup_frame, text="New Password:").grid(row=2, column=0)
new_password_entry = tk.Entry(signup_frame, show="*")
new_password_entry.grid(row=2, column=1)
tk.Label(signup_frame, text="Email:").grid(row=3,column=0)
new_email_entry = tk.Entry(signup_frame)
new_email_entry.grid(row=3,column=1)
tk.Label(signup_frame, text="Age:").grid(row=4,column=0)
new_age_entry = tk.Entry(signup_frame)
new_age_entry.grid(row=4,column=1)
signup_button = tk.Button(signup_frame, text="Signup", command=signup)
signup_button.grid(row=5, column=0, columnspan=2)

app.mainloop()
