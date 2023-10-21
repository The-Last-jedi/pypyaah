import tkinter as tk
import customtkinter as ctk
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage,ttk
from pathlib import Path
from tkcalendar import Calendar, DateEntry

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"D:\PycharmPractice\pyproject\build\assets\notclicked")

global image
font=("Times 20 italic bold", 32 * -1)


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


root = ctk.CTk()
root.geometry("1280x800")
root.title("Auto Scheduler")
root.resizable(False, False)

main = ctk.CTkFrame(root, fg_color='#0B3954')
main.place(x=75, y=75)
main.pack_propagate(False)
main.configure(width=1205, height=725)

op_frame = ctk.CTkFrame(root, fg_color='#D9D9D9')
top_frame = ctk.CTkFrame(root, fg_color='#087E8B')

op_frame.place(x=0, y=75)
op_frame.pack_propagate(False)
op_frame.configure(width=75, height=725)

top_frame.place(x=0, y=0)
top_frame.pack_propagate(False)
top_frame.configure(height=75, width=1280)

top_label = ctk.CTkLabel(top_frame,
                         anchor="nw",
                         text="Auto Task Scheduler",
                         fg_color="#087E8B",
                         font=("Times 20 italic bold", 32 * -1))
top_label.pack(pady=12)
button_image_1 = PhotoImage(
    file="assets/clicked/Home.png")


def clear_frame():
    for frame in main.winfo_children():
        frame.destroy()


def change_home():
    new_image = PhotoImage(file="assets/clicked/Home.png")
    new_image1 = PhotoImage(file="assets/notclicked/Tasks.png")
    new_image2 = PhotoImage(file="assets/notclicked/Profile.png")
    button_2.config(image=new_image1)
    button_2.image = new_image1
    button_3.config(image=new_image2)
    button_3.image = new_image2

    button_1.config(image=new_image)
    button_1.image = new_image
    clear_frame()
    home()


def change_tasks():
    new_image = PhotoImage(file="assets/clicked/Tasks.png")
    new_image1 = PhotoImage(file="assets/notclicked/Home.png")
    new_image2 = PhotoImage(file="assets/notclicked/Profile.png")
    button_1.config(image=new_image1)
    button_1.image = new_image1
    button_3.config(image=new_image2)
    button_3.image = new_image2

    button_2.config(image=new_image)
    button_2.image = new_image
    clear_frame()
    tasks()


def change_profile():
    new_image = PhotoImage(file="assets/clicked/Profile.png")
    new_image1 = PhotoImage(file="assets/notclicked/Home.png")
    new_image2 = PhotoImage(file="assets/notclicked/Tasks.png")
    button_1.config(image=new_image1)
    button_1.image = new_image1
    button_2.config(image=new_image2)
    button_2.image = new_image2

    button_3.config(image=new_image)
    button_3.image = new_image
    clear_frame()
    profile()


def home():
    Home = ctk.CTkFrame(main)
    label1 = ctk.CTkLabel(Home, text="Home Page\n\nPage = 1", )
    label1.pack()
    Home.pack()
    pass


def tasks():
    task = ctk.CTkFrame(main)
    # Task Name
    tn_label = ctk.CTkLabel(task, font=font, text="Task Name")
    tn_label.place(x=20, y=20)
    tn_entry = ctk.CTkEntry(task,font=font,text_color='#000', fg_color='#fff', border_color='#0C9295', border_width=2, width=180)
    tn_entry.place(x=200,y=20)

    # Task Priority
    tp_label = ctk.CTkLabel(task, font=font, text="Task Priority")
    tp_label.place(x=20, y=90)
    optionsp=['Very High', 'High', 'Medium', 'Low']
    variable1 = ctk.StringVar()
    priority_options= ctk.CTkComboBox(task, font = font,text_color='#000', fg_color='#fff',dropdown_hover_color=
    '#0C9295', button_color='#0C9295',button_hover_color='#0C9295', border_color='#0C9295',width=180, variable=variable1, values=optionsp)
    priority_options.place(x=200, y=90)

    # Task Status
    ts_label = ctk.CTkLabel(task, font=font, text="Task Status")
    ts_label.place(x=20, y=160)
    optionss = ['Pending', 'Upcoming', 'Completed']
    variable2 = ctk.StringVar()
    priority_options = ctk.CTkComboBox(task, font=font, text_color='#000', fg_color='#fff', dropdown_hover_color=
    '#0C9295', button_color='#0C9295', button_hover_color='#0C9295', border_color='#0C9295', width=180,
                                       variable=variable2, values=optionss)
    priority_options.place(x=200, y=160)


    #Ending Date
    ts_label = ctk.CTkLabel(task, font=font, text="Ending Date")
    ts_label.place(x=20, y=230)

    cal = DateEntry(task, width=20, background='darkblue',
                    foreground='#fff')
    cal.place(x=200, y=230)

    task.place(x=20, y=20)
    task.pack_propagate(False)
    task.configure(width=406, height=401)


def profile():
    Profile = ctk.CTkFrame(main)
    label1 = ctk.CTkLabel(Profile, text="Profile Page\n\nPage = 1", )
    label1.pack()
    Profile.pack()
    pass


def logout():
    pass


button_1 = Button(op_frame,
                  image=button_image_1,
                  borderwidth=0,
                  highlightthickness=0,
                  command=change_home,
                  relief="flat"
                  )
button_1.pack()
button_image_2 = PhotoImage(
    file=relative_to_assets("Tasks.png"))

button_2 = Button(op_frame,
                  image=button_image_2,
                  borderwidth=0,
                  highlightthickness=0,
                  command=change_tasks,
                  relief="flat"
                  )
button_2.pack()

button_image_3 = PhotoImage(
    file=relative_to_assets("Profile.png"))

button_3 = Button(op_frame,
                  image=button_image_3,
                  borderwidth=0,
                  highlightthickness=0,
                  command=change_profile,
                  relief="flat"
                  )
button_3.pack()

button_image_4 = PhotoImage(
    file=relative_to_assets("Logout.png"))

button_4 = Button(op_frame,
                  image=button_image_4,
                  borderwidth=0,
                  highlightthickness=0,
                  command=lambda: logout(),
                  relief="flat"
                  )
button_4.pack(side=ctk.BOTTOM)

root.mainloop()
