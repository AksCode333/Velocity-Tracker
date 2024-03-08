import tkinter as tk
from tkinter import ttk
import sv_ttk

def enter(x):
    print("Changing the reps")

def start():
    print("Begin Rep")
def update_reps(value):
    global rep_num
    global str_rep_num
    rep_num = value
    str_rep_num = str(rep_num)
    number_var.set(str_rep_num)

def update_text(value):
    global shared_variable
    shared_variable = value
    text_var.set(shared_variable)  # Update the text box with the new value

def kg_or_lb(value):
    global kglb
    kglb = value

def delete_rep(rep_num):
    print("deleted rep ", rep_num)

# Initialize the main Tkinter window
root = tk.Tk()
root.geometry("1050x600")
root.title("Velocity Tracking GUI Program")

# Initialize a shared variable
shared_variable = ""
rep_num = 0
str_rep_num = ""
kglb = ""

# Create a StringVar to update the text box
text_var = tk.StringVar()
text_var.set(shared_variable)
number_var = tk.IntVar()
number_var.set(rep_num)
#stores weight value

# Create a text box (entry widget) that displays the shared variable
#Create a frame to push all of the other info into the center
frame = ttk.Frame(root,borderwidth=5, relief="sunken",padding= 1)
frame.grid(row=0, column=0, rowspan=1, pady=10, padx=10)

text_box = ttk.Entry(frame, textvariable=text_var, state='readonly', width=30)
text_box.grid(row=0, column=1, columnspan=3,padx=10, pady=10)

# Create three buttons that update the shared variable with different values
button1 = ttk.Button(frame, text="Bench", command=lambda: update_text('Bench'), padding=10)
button1.grid(row=1, column=1)

button2 = ttk.Button(frame, text="Squat", command=lambda: update_text('Squat'), padding=10)
button2.grid(row=1, column=2)

button3 = ttk.Button(frame, text="Deadlift", command=lambda: update_text('Deadlift'), padding=10)
button3.grid(row=1, column=3)

liftcho = ttk.Label(frame, text="LIFT TYPE")
liftcho.grid(row=0, column=0, padx=10, pady=40)

#START OF THE REP DECIDER
frame2 = ttk.Frame(root,borderwidth=5, relief="sunken",padding= 1)
frame2.grid(row=0, column=1, rowspan=1, padx=10, pady=10)
frame2.bind("<Enter>", enter)

weight_choice = ttk.Label(frame2, text="# of Reps")
weight_choice.grid(row=0, column=4, padx=10, pady=40)
#buttons ----
Rbutton1 = ttk.Button(frame2, text="1", command=lambda: update_reps(1), padding=10)
Rbutton1.grid(row=1, column=5)

Rbutton2 = ttk.Button(frame2, text="3", command=lambda: update_reps(3), padding=10)
Rbutton2.grid(row=1, column=6)

Rbutton3 = ttk.Button(frame2, text="5", command=lambda: update_reps(5), padding=10)
Rbutton3.grid(row=1, column=7)

Rbutton4 = ttk.Button(frame2, text="8", command=lambda: update_reps(8), padding=10)
Rbutton4.grid(row=1, column=8)

Rbutton5 = ttk.Button(frame2, text="10", command=lambda: update_reps(10), padding=10)
Rbutton5.grid(row=1, column=9)
#display the number
Rtext_box = ttk.Entry(frame2, textvariable=number_var, state='readonly', width=30)
Rtext_box.grid(row=0, column=5, columnspan=5,padx=10, pady=10)

# Weight Choice
weight_frame = ttk.Frame(root,borderwidth=5, relief="sunken",padding= 1)
weight_frame.grid(row=2, column=0, rowspan=1, pady=5, padx=5)
weight_lab = ttk.Label(weight_frame, text="   Weight   ")
weight_lab.grid(row=3, column=0, padx=10, pady=50)

#Entry location
weight_entry = ttk.Entry(weight_frame, width=40)
weight_entry.grid(row=4, column=0,padx=15, pady=5,rowspan=1,columnspan=3)
#buttons
kg_button = ttk.Button(weight_frame, text="KG", command=lambda: kg_or_lb("KG"), padding=20)
kg_button.grid(row=3, column=1)

lb_button = ttk.Button(weight_frame, text="LB", command=lambda: kg_or_lb("LB"), padding=20)
lb_button.grid(row=3, column=2)
#NOTES
note_frame = ttk.Frame(root, borderwidth=5, relief = "sunken", padding=1)
note_frame.grid(row=2, column=1, rowspan=1, pady=10, padx=10,columnspan=1)

notes = ttk.Frame(note_frame, borderwidth=5, relief = "sunken", padding=1)
notes.grid(row=3, column=5, rowspan=2, pady=10, padx=5, columnspan = 1)
weight_lab = ttk.Label(notes, text="   Notes   ")
weight_lab.grid(row=3, column=4, padx=3, pady=40)


notes_entry = ttk.Entry(note_frame, width=30)
notes_entry.grid(row=3, column=6, padx=5, pady=45,rowspan=1,columnspan=1)


# #BoX TO SHOW ALL THE DATA
results = ttk.Frame(root, borderwidth=0, relief="sunken",padding= 1)
results.grid(row=5, column=0, pady=10, padx=5, columnspan=2)

#REP 1
rep1 = ttk.Frame(results, borderwidth=5, relief="sunken",padding= 1)
rep1.grid(row=5, column=1, rowspan=2, pady=10, padx=5)
rep1_vel = ttk.Label(rep1, text = "AVG VEL = ", width=20)
rep1_vel.grid(row=1, column=1)
rep1_rom = ttk.Label(rep1, text = "ROM = ", width=20)
rep1_rom.grid(row=2, column=1)
rep1_time = ttk.Label(rep1, text = "TIME = ", width=20)
rep1_time.grid(row=3, column=1)
rep1_other = ttk.Label(rep1, text = "Other = ", width=20)
rep1_other.grid(row=4, column=1)
rep1_delete = ttk.Button(rep1, text="DELETE", command=lambda: delete_rep(1), padding=10)
rep1_delete.grid(row=5, column=1)

#REP 2
rep2 = ttk.Frame(results, borderwidth=5, relief="sunken",padding= 1)
rep2.grid(row=5, column=2, rowspan=2, pady=10, padx=5)
rep2_vel = ttk.Label(rep2, text = "AVG VEL = ", width=20)
rep2_vel.grid(row=1, column=1)
rep2_rom = ttk.Label(rep2, text = "ROM = ", width=20)
rep2_rom.grid(row=2, column=1)
rep2_time = ttk.Label(rep2, text = "TIME = ", width=20)
rep2_time.grid(row=3, column=1)
rep2_other = ttk.Label(rep2, text = "Other = ", width=20)
rep2_other.grid(row=4, column=1)
rep2_delete = ttk.Button(rep2, text="DELETE", command=lambda: delete_rep(2), padding=10)
rep2_delete.grid(row=5, column=1)

#REP 3
rep3 = ttk.Frame(results, borderwidth=5, relief="sunken",padding= 1)
rep3.grid(row=5, column=3, rowspan=2, pady=10, padx=5)
rep3_vel = ttk.Label(rep3, text = "AVG VEL = ", width=20)
rep3_vel.grid(row=1, column=1)
rep3_rom = ttk.Label(rep3, text = "ROM = ", width=20)
rep3_rom.grid(row=2, column=1)
rep3_time = ttk.Label(rep3, text = "TIME = ", width=20)
rep3_time.grid(row=3, column=1)
rep3_other = ttk.Label(rep3, text = "Other = ", width=20)
rep3_other.grid(row=4, column=1)
rep3_delete = ttk.Button(rep3, text="DELETE", command=lambda: delete_rep(3), padding=10)
rep3_delete.grid(row=5, column=1)

#REP 4
rep4 = ttk.Frame(results, borderwidth=5, relief="sunken",padding= 1)
rep4.grid(row=5, column=4, rowspan=2, pady=10, padx=5)
rep4_vel = ttk.Label(rep4, text = "AVG VEL = ", width=20)
rep4_vel.grid(row=1, column=1)
rep4_rom = ttk.Label(rep4, text = "ROM = ", width=20)
rep4_rom.grid(row=2, column=1)
rep4_time = ttk.Label(rep4, text = "TIME = ", width=20)
rep4_time.grid(row=3, column=1)
rep4_other = ttk.Label(rep4, text = "Other = ", width=20)
rep4_other.grid(row=4, column=1)
rep4_delete = ttk.Button(rep4, text="DELETE", command=lambda: delete_rep(4), padding=10)
rep4_delete.grid(row=5, column=1)

#rep 5
rep5 = ttk.Frame(results, borderwidth=5, relief="sunken",padding= 1)
rep5.grid(row=5, column=5, rowspan=2, pady=10, padx=5)
rep5_vel = ttk.Label(rep5, text = "AVG VEL = ", width=20)
rep5_vel.grid(row=1, column=1)
rep5_rom = ttk.Label(rep5, text = "ROM = ", width=20)
rep5_rom.grid(row=2, column=1)
rep5_time = ttk.Label(rep5, text = "TIME = ", width=20)
rep5_time.grid(row=3, column=1)
rep5_other = ttk.Label(rep5, text = "Other = ", width=20)
rep5_other.grid(row=4, column=1)
rep5_delete = ttk.Button(rep5, text="DELETE", command=lambda: delete_rep(5), padding=10)
rep5_delete.grid(row=5, column=1)

# Start Button
start_outline = ttk.Frame(root, borderwidth=5, relief="raised")
start_outline.grid(row=6, column=0, columnspan=2)
start_button = ttk.Button(start_outline, text="START", command=lambda: start(), padding=10,width=100)
start_button.grid(row=1, column=1)

# Start the Tkinter event loop
# This is where the magic happens
sv_ttk.set_theme("dark")
root.mainloop()