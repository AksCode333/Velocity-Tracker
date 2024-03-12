import tkinter as tk
from tkinter import ttk
import sv_ttk
import serial
import datetime
import gspread
from oauth2client.service_account import ServiceAccountCredentials

#google sheets stuff
scope = ["https://spreadsheets.google.com/feeds",'https://www.googleapis.com/auth/spreadsheets',"https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]
creds = ServiceAccountCredentials.from_json_keyfile_name("creds.json", scope)
client = gspread.authorize(creds)
sheet = client.open("Fitness").sheet1

# Get the current date
now = datetime.datetime.now()
formatted_date = now.strftime("%m/%d/%y")

# Constants
# SERIAL_PORT = '/dev/cu.usbserial-14310'
# BAUD_RATE = 115200
# ser = serial.Serial(SERIAL_PORT, BAUD_RATE)
global vel_list
number_of_reps = 0
#serial connections

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
    if rep_num == 1:  
        rep1_vel_value.set("VEL: N/A")
        rep1_rom_value.set("ROM: N/A")
    if rep_num == 2:
        rep2_vel_value.set("VEL: N/A")
        rep2_rom_value.set("ROM: N/A")
    if rep_num == 3:
        rep3_vel_value.set("VEL: N/A")
        rep3_rom_value.set("ROM: N/A")
    if rep_num == 4:
        rep4_vel_value.set("VEL: N/A")
        rep4_rom_value.set("ROM: N/A")
    if rep_num == 5:
        rep5_vel_value.set("VEL: N/A")
        rep5_rom_value.set("ROM: N/A")
    if rep_num == 6:
        rep6_vel_value.set("VEL: N/A")
        rep6_rom_value.set("ROM: N/A")
    if rep_num == 7:
        rep7_vel_value.set("VEL: N/A")
        rep7_rom_value.set("ROM: N/A")
    if rep_num == 8:
        rep8_vel_value.set("VEL: N/A")
        rep8_rom_value.set("ROM: N/A")
    if rep_num == 9:
        rep9_vel_value.set("VEL: N/A")
        rep9_rom_value.set("ROM: N/A")
    if rep_num == 10:
        rep10_vel_value.set("VEL: N/A")
        rep10_rom_value.set("ROM: N/A")

    # vel_list = []
    # # print(number_of_reps)
    # # if number_of_reps > 1:
    # vel_list.append(rep1_vel_value.set("0"))
#retrieve the data from the arduino
def get_data():
    SERIAL_PORT = 'COM3'
    BAUD_RATE = 115200
    ser = serial.Serial(SERIAL_PORT, BAUD_RATE)
    def read_and_process_data():
        line = ser.readline().decode('utf-8').strip()
        sensorValues = line.split(': ')

        rep_value.append(str(sensorValues[0]))
        vel.append(float(sensorValues[1]))
        rom.append(float(sensorValues[2]))
        
        # k = 0
        # for i in vel:
        #     vel_list.append(vel[k])
        #     k = k+1
    # print the recieved values
    number_of_reps = number_var.get() + 1
    print(number_of_reps)
    while(len(rep_value) < number_of_reps):
        read_and_process_data()
    if(len(rep_value) >= number_of_reps):
        organize_data(rep_value, vel, number_of_reps, rom)
#oranize the data and send it out to display\

def organize_data(number, velocity, nor, rom):
    print(velocity)
    print(nor)
    if nor > 0:  
        rep1_vel_value.set("AVG VEL: " + str(velocity[0]))
        rep1_rom_value.set("ROM: " + str(rom[0]))
        # rep1_time_value.set("TIME: " + str(time[0]))
    else:
        rep1_vel_value.set("VEL: N/A")
        rep1_rom_value.set("ROM: N/A")
        rep1_time_value.set("TIME: N/A")
    if nor > 1:
        rep2_vel_value.set("AVG VEL: " + str(velocity[1]))
        rep2_rom_value.set("ROM: "+ str(rom[1]))
        # rep2_time_value.set("TIME: " + str(time[1]))
    else:
        rep2_vel_value.set("VEL: N/A")
        rep2_rom_value.set("ROM: N/A")
        rep2_time_value.set("TIME: N/A")
    if nor > 2:
        rep3_vel_value.set("AVG VEL: " + str(velocity[2]))
        rep3_rom_value.set("ROM: " + str(rom[2]))
        # rep3_time_value.set("TIME: " + str(time[2]))
    else:
        rep3_vel_value.set("VEL: N/A")
        rep3_rom_value.set("ROM: N/A")
        rep3_time_value.set("TIME: N/A")
    if nor > 3:
        rep4_vel_value.set("AVG VEL: " + str(velocity[3]))
        rep4_rom_value.set("ROM: " + str(rom[3]))
        # rep4_time_value.set("TIME: " + str(time[3]))
    else:
        rep4_vel_value.set("VEL: N/A")
        rep4_rom_value.set("ROM: N/A")
        rep4_time_value.set("TIME: N/A")
    if nor > 4:
        rep5_vel_value.set("AVG VEL: " + str(velocity[4]))
        rep5_rom_value.set("ROM: " + str(rom[4]))
        # rep5_time_value.set("TIME: " + str(time[4]))
    else:
        rep5_vel_value.set("VEL: N/A")
        rep5_rom_value.set("ROM: N/A")
        rep5_time_value.set("TIME: N/A")
    if nor > 5:
        rep6_vel_value.set("AVG VEL: " + str(velocity[5]))
        rep6_rom_value.set("ROM: " + str(rom[5]))
        # rep6_time_value.set("TIME: " + str(time[5]))
    else:
        rep6_vel_value.set("VEL: N/A")
        rep6_rom_value.set("ROM: N/A")
        rep6_time_value.set("TIME: N/A")
    if nor > 6:
        rep7_vel_value.set("AVG VEL: " + str(velocity[6]))
        rep7_rom_value.set("ROM: " + str(rom[6]))
        # rep7_time_value.set("TIME: " + str(time[6]))
    else:
        rep7_vel_value.set("VEL: N/A")
        rep7_rom_value.set("ROM: N/A")
        rep7_time_value.set("TIME: N/A")
    if nor > 7:
        rep8_vel_value.set("AVG VEL: " + str(velocity[7]))
        rep8_rom_value.set("ROM: " + str(rom[7]))
        # rep8_time_value.set("TIME: " + str(time[7]))
    else:
        rep8_vel_value.set("VEL: N/A")
        rep8_rom_value.set("ROM: N/A")
        rep8_time_value.set("TIME: N/A")
    if nor > 8:
        rep9_vel_value.set("AVG VEL: " + str(velocity[8]))
        rep9_rom_value.set("ROM: " + str(rom[8]))
        # rep9_time_value.set("TIME: " + str(time[8]))
    else:
        rep9_vel_value.set("VEL: N/A")
        rep9_rom_value.set("ROM: N/A")
        rep9_time_value.set("TIME: N/A")
    if nor > 9:
        rep10_vel_value.set("AVG VEL: " + str(velocity[9]))
        rep10_rom_value.set("ROM: " + str(rom[9]))
        # rep10_time_value.set("TIME: " + str(time[9]))
    else:
        rep10_vel_value.set("VEL: N/A")
        rep10_rom_value.set("ROM: N/A")
        rep10_time_value.set("TIME: N/A")
    for x in range(nor):
        print(number[x], ",", velocity[x])
    global number_of_reps
    number_of_reps = nor

def finalize_data():
    blank = rep5_vel_value.get()
    FINAL_VELOCITIES = []
    FINAL_ROMS = []
    if str(rep1_vel_value.get()) != "0" and rep1_vel_value.get() != "VEL: N/A":  
        x1 = rep1_vel_value.get()
        x1 = x1.split(': ')
        FINAL_VELOCITIES.append(float(x1[1]))
        x = rep1_rom_value.get()
        x = x.split(': ')
        FINAL_ROMS.append(float(x[1]))

    if str(rep2_vel_value.get()) != "0"and rep2_vel_value.get() != "VEL: N/A":  
        x2 = rep2_vel_value.get()
        x2 = x2.split(': ')
        FINAL_VELOCITIES.append(float(x2[1]))
        x = rep2_rom_value.get()
        x = x.split(': ')
        FINAL_ROMS.append(float(x[1]))

    if str(rep3_vel_value.get()) != "0"and rep3_vel_value.get() != "VEL: N/A":  
        x3 = rep3_vel_value.get()
        x3 = x3.split(': ')
        FINAL_VELOCITIES.append(float(x3[1]))
        x = rep3_rom_value.get()
        x = x.split(': ')
        FINAL_ROMS.append(float(x[1]))

    if str(rep4_vel_value.get()) != "0" and rep4_vel_value.get() != "VEL: N/A":  
        x3 = rep4_vel_value.get()
        x3 = x3.split(': ')
        FINAL_VELOCITIES.append(float(x3[1]))
        x = rep4_rom_value.get()
        x = x.split(': ')
        FINAL_ROMS.append(float(x[1]))

    if str(rep5_vel_value.get()) != "VEL: N/A":  
        print("its not working")
        x3 = rep5_vel_value.get()
        x3 = x3.split(': ')
        FINAL_VELOCITIES.append(float(x3[1]))
        x = rep5_rom_value.get()
        x = x.split(': ')
        FINAL_ROMS.append(float(x[1]))

    if str(rep6_vel_value.get()) != "0" and rep6_vel_value.get() != "VEL: N/A":  
        x3 = rep6_vel_value.get()
        x3 = x3.split(': ')
        FINAL_VELOCITIES.append(float(x3[1]))
        x = rep6_rom_value.get()
        x = x.split(': ')
        FINAL_ROMS.append(float(x[1]))

    if str(rep7_vel_value.get()) != "VEL: N/A" and rep7_vel_value.get() != "":  
        print("rep 7 is ", str(rep7_vel_value.get()))
        x3 = rep7_vel_value.get()
        x3 = x3.split(': ')
        FINAL_VELOCITIES.append(float(x3[1]))
        x = rep7_rom_value.get()
        x = x.split(': ')
        FINAL_ROMS.append(float(x[1]))

    if str(rep8_vel_value.get()) != "0" and rep8_vel_value.get() != "VEL: N/A":  
        x3 = rep8_vel_value.get()
        x3 = x3.split(': ')
        FINAL_VELOCITIES.append(float(x3[1]))
        x = rep8_rom_value.get()
        x = x.split(': ')
        FINAL_ROMS.append(float(x[1]))

    if str(rep9_vel_value.get()) != "0" and rep9_vel_value.get() != "VEL: N/A":  
        x3 = rep9_vel_value.get()
        x3 = x3.split(': ')
        FINAL_VELOCITIES.append(float(x3[1]))
        x = rep9_rom_value.get()
        x = x.split(': ')
        FINAL_ROMS.append(float(x[1]))

    if str(rep10_vel_value.get()) != "0" and rep10_vel_value.get() != "VEL: N/A":  
        x3 = rep10_vel_value.get()
        x3 = x3.split(': ')
        FINAL_VELOCITIES.append(float(x3[1]))
        x = rep10_rom_value.get()
        x = x.split(': ')
        FINAL_ROMS.append(float(x[1]))

    # if rep10_vel_value.get() != "0":  
    #     x3 = rep10_vel_value.get()
    #     x3 = x3.split(': ')
    #     FINAL_VELOCITIES.append(float(x3[1]))
    print("The fnial velocities were: ", FINAL_VELOCITIES)
    print("there were ", len(FINAL_VELOCITIES), "reps")
    print("The AVG set velocity was: ", sum(FINAL_VELOCITIES)/len(FINAL_VELOCITIES))
    print("The weight was: ",weight_entry.get()," ", kglb)
    print("the lift was: ", shared_variable)

    send_to_sheet = [formatted_date, shared_variable, weight_entry.get(), len(FINAL_VELOCITIES), sum(FINAL_VELOCITIES)/len(FINAL_VELOCITIES)]
    for i in FINAL_VELOCITIES: #add all the reps to the google sheet
        send_to_sheet.append(i)
    while len(send_to_sheet) < 15: #adds in the blank ones so that I can keep adding to the google sehets past the resp
        send_to_sheet.append("")
    for i in FINAL_ROMS:
        send_to_sheet.append(i)
    while len(send_to_sheet) < 25:
        send_to_sheet.append("")

    sheet.insert_row(send_to_sheet, 2)


#Random Variables
rep_value = []
vel = []
rom = []
# Initialize the main Tkinter window
root = tk.Tk()
root.geometry("950x800")
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
#ALL REP VALUES -------------
rep1_vel_value = 0
rep1_vel_value = tk.StringVar()
rep2_vel_value = 0
rep2_vel_value = tk.StringVar()
rep3_vel_value = 0
rep3_vel_value = tk.StringVar()
rep4_vel_value = 0
rep4_vel_value = tk.StringVar()
rep5_vel_value = 0
rep5_vel_value = tk.StringVar()
rep6_vel_value = 0
rep6_vel_value = tk.StringVar()
rep7_vel_value = 0
rep7_vel_value = tk.StringVar()
rep8_vel_value = 0
rep8_vel_value = tk.StringVar()
rep9_vel_value = 0
rep9_vel_value = tk.StringVar()
rep10_vel_value = 0
rep10_vel_value = tk.StringVar()
#all rom values
rep1_rom_value = 0
rep1_rom_value = tk.StringVar()
rep2_rom_value = 0
rep2_rom_value = tk.StringVar()
rep3_rom_value = 0
rep3_rom_value = tk.StringVar()
rep4_rom_value = 0
rep4_rom_value = tk.StringVar()
rep5_rom_value = 0
rep5_rom_value = tk.StringVar()
rep6_rom_value = 0
rep6_rom_value = tk.StringVar()
rep7_rom_value = 0
rep7_rom_value = tk.StringVar()
rep8_rom_value = 0
rep8_rom_value = tk.StringVar()
rep9_rom_value = 0
rep9_rom_value = tk.StringVar()
rep10_rom_value = 0
rep10_rom_value = tk.StringVar()
rep1_time_value = 0
rep1_time_value = tk.StringVar()
rep2_time_value = 0
rep2_time_value = tk.StringVar()
rep3_time_value = 0
rep3_time_value = tk.StringVar()
rep4_time_value = 0
rep4_time_value = tk.StringVar()
rep5_time_value = 0
rep5_time_value = tk.StringVar()
rep6_time_value = 0
rep6_time_value = tk.StringVar()
rep7_time_value = 0
rep7_time_value = tk.StringVar()
rep8_time_value = 0
rep8_time_value = tk.StringVar()
rep9_time_value = 0
rep9_time_value = tk.StringVar()
rep10_time_value = 0
rep10_time_value = tk.StringVar()
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
rep1_vel = ttk.Label(rep1, textvariable=(rep1_vel_value), width=20)
rep1_vel.grid(row=1, column=1)
rep1_rom = ttk.Label(rep1, textvariable=(rep1_rom_value), width=20)
rep1_rom.grid(row=2, column=1)
rep1_time = ttk.Label(rep1,textvariable=(rep1_time_value) , width=20)
rep1_time.grid(row=3, column=1)
rep1_other = ttk.Label(rep1, text = "Other = ", width=20)
rep1_other.grid(row=4, column=1)
rep1_delete = ttk.Button(rep1, text="DELETE", command=lambda: delete_rep(1), padding=10)
rep1_delete.grid(row=5, column=1)

#REP 2
rep2 = ttk.Frame(results, borderwidth=5, relief="sunken",padding= 1)
rep2.grid(row=5, column=2, rowspan=2, pady=10, padx=5)
rep2_vel = ttk.Label(rep2, textvariable=rep2_vel_value, width=20)
rep2_vel.grid(row=1, column=1)
rep2_rom = ttk.Label(rep2, textvariable=(rep2_rom_value), width=20)
rep2_rom.grid(row=2, column=1)
rep2_time = ttk.Label(rep2, textvariable=(rep2_time_value), width=20)
rep2_time.grid(row=3, column=1)
rep2_other = ttk.Label(rep2, text = "Other = ", width=20)
rep2_other.grid(row=4, column=1)
rep2_delete = ttk.Button(rep2, text="DELETE", command=lambda: delete_rep(2), padding=10)
rep2_delete.grid(row=5, column=1)

#REP 3
rep3 = ttk.Frame(results, borderwidth=5, relief="sunken",padding= 1)
rep3.grid(row=5, column=3, rowspan=2, pady=10, padx=5)
rep3_vel = ttk.Label(rep3, textvariable=rep3_vel_value, width=20)
rep3_vel.grid(row=1, column=1)
rep3_rom = ttk.Label(rep3, textvariable=(rep3_rom_value), width=20)
rep3_rom.grid(row=2, column=1)
rep3_time = ttk.Label(rep3, textvariable=(rep3_time_value), width=20)
rep3_time.grid(row=3, column=1)
rep3_other = ttk.Label(rep3, text = "Other = ", width=20)
rep3_other.grid(row=4, column=1)
rep3_delete = ttk.Button(rep3, text="DELETE", command=lambda: delete_rep(3), padding=10)
rep3_delete.grid(row=5, column=1)

#REP 4
rep4 = ttk.Frame(results, borderwidth=5, relief="sunken",padding= 1)
rep4.grid(row=5, column=4, rowspan=2, pady=10, padx=5)
rep4_vel = ttk.Label(rep4,textvariable=rep4_vel_value, width=20)
rep4_vel.grid(row=1, column=1)
rep4_rom = ttk.Label(rep4,textvariable=(rep4_rom_value), width=20)
rep4_rom.grid(row=2, column=1)
rep4_time = ttk.Label(rep4, textvariable=(rep4_time_value), width=20)
rep4_time.grid(row=3, column=1)
rep4_other = ttk.Label(rep4, text = "Other = ", width=20)
rep4_other.grid(row=4, column=1)
rep4_delete = ttk.Button(rep4, text="DELETE", command=lambda: delete_rep(4), padding=10)
rep4_delete.grid(row=5, column=1)

#rep 5
rep5 = ttk.Frame(results, borderwidth=5, relief="sunken",padding= 1)
rep5.grid(row=5, column=5, rowspan=2, pady=10, padx=5)
rep5_vel = ttk.Label(rep5, textvariable=rep5_vel_value, width=20)
rep5_vel.grid(row=1, column=1)
rep5_rom = ttk.Label(rep5,textvariable=(rep5_rom_value), width=20)
rep5_rom.grid(row=2, column=1)
rep5_time = ttk.Label(rep5,textvariable=(rep5_time_value), width=20)
rep5_time.grid(row=3, column=1)
rep5_other = ttk.Label(rep5, text = "Other = ", width=20)
rep5_other.grid(row=4, column=1)
rep5_delete = ttk.Button(rep5, text="DELETE", command=lambda: delete_rep(5), padding=10)
rep5_delete.grid(row=5, column=1)
#REP 6
rep6 = ttk.Frame(results, borderwidth=5, relief="sunken",padding= 1)
rep6.grid(row=7, column=1, rowspan=2, pady=10, padx=5)
rep6_vel = ttk.Label(rep6,textvariable=rep6_vel_value, width=20)
rep6_vel.grid(row=1, column=1)
rep6_rom = ttk.Label(rep6, textvariable=(rep6_rom_value), width=20)
rep6_rom.grid(row=2, column=1)
rep6_time = ttk.Label(rep6, textvariable=(rep6_time_value), width=20)
rep6_time.grid(row=3, column=1)
rep6_other = ttk.Label(rep6, text = "Other = ", width=20)
rep6_other.grid(row=4, column=1)
rep6_delete = ttk.Button(rep6, text="DELETE", command=lambda: delete_rep(6), padding=10)
rep6_delete.grid(row=5, column=1)
#REP 7
rep7 = ttk.Frame(results, borderwidth=5, relief="sunken",padding= 1)
rep7.grid(row=7, column=2, rowspan=2, pady=10, padx=5)
rep7_vel = ttk.Label(rep7,textvariable=rep7_vel_value, width=20)
rep7_vel.grid(row=1, column=1)
rep7_rom = ttk.Label(rep7, textvariable=(rep7_rom_value), width=20)
rep7_rom.grid(row=2, column=1)
rep7_time = ttk.Label(rep7, textvariable=(rep7_time_value), width=20)
rep7_time.grid(row=3, column=1)
rep7_other = ttk.Label(rep7, text = "Other = ", width=20)
rep7_other.grid(row=4, column=1)
rep7_delete = ttk.Button(rep7, text="DELETE", command=lambda: delete_rep(7), padding=10)
rep7_delete.grid(row=5, column=1)
#REP 8
rep8 = ttk.Frame(results, borderwidth=5, relief="sunken",padding= 1)
rep8.grid(row=7, column=3, rowspan=2, pady=10, padx=5)
rep8_vel = ttk.Label(rep8,textvariable=rep8_vel_value, width=20)
rep8_vel.grid(row=1, column=1)
rep8_rom = ttk.Label(rep8,textvariable=(rep8_rom_value), width=20)
rep8_rom.grid(row=2, column=1)
rep8_time = ttk.Label(rep8, textvariable=(rep8_time_value), width=20)
rep8_time.grid(row=3, column=1)
rep8_other = ttk.Label(rep8, text = "Other = ", width=20)
rep8_other.grid(row=4, column=1)
rep8_delete = ttk.Button(rep8, text="DELETE", command=lambda: delete_rep(8), padding=10)
rep8_delete.grid(row=5, column=1)
#REP 9
rep9 = ttk.Frame(results, borderwidth=5, relief="sunken",padding= 1)
rep9.grid(row=7, column=4, rowspan=2, pady=10, padx=5)
rep9_vel = ttk.Label(rep9,textvariable=rep9_vel_value, width=20)
rep9_vel.grid(row=1, column=1)
rep9_rom = ttk.Label(rep9, textvariable=(rep9_rom_value), width=20)
rep9_rom.grid(row=2, column=1)
rep9_time = ttk.Label(rep9,textvariable=(rep9_time_value), width=20)
rep9_time.grid(row=3, column=1)
rep9_other = ttk.Label(rep9, text = "Other = ", width=20)
rep9_other.grid(row=4, column=1)
rep9_delete = ttk.Button(rep9, text="DELETE", command=lambda: delete_rep(9), padding=10)
rep9_delete.grid(row=5, column=1)
#REP 10
rep10 = ttk.Frame(results, borderwidth=5, relief="sunken",padding= 1)
rep10.grid(row=7, column=5, rowspan=2, pady=10, padx=5)
rep10_vel = ttk.Label(rep10,textvariable=rep10_vel_value, width=20)
rep10_vel.grid(row=1, column=1)
rep10_rom = ttk.Label(rep10,textvariable=(rep10_rom_value), width=20)
rep10_rom.grid(row=2, column=1)
rep10_time = ttk.Label(rep10, textvariable=(rep10_time_value), width=20)
rep10_time.grid(row=3, column=1)
rep10_other = ttk.Label(rep10, text = "Other = ", width=20)
rep10_other.grid(row=4, column=1)
rep10_delete = ttk.Button(rep10, text="DELETE", command=lambda: delete_rep(10), padding=10)
rep10_delete.grid(row=5, column=1)
# Start Button

start_outline = ttk.Frame(root, borderwidth=5, relief="raised")
start_outline.grid(row=9, column=0, columnspan=2)
start_button = ttk.Button(start_outline, text="START", command=lambda: get_data(), padding=10,width=100)
start_button.grid(row=1, column=1)
#FINALIZE DATA
final = ttk.Frame(root, borderwidth= 5, relief="raised")
final.grid(row=10, column=0,pady=10,columnspan=2)
finish = ttk.Button(final, text="SEND DATA", command=lambda: finalize_data(), padding=10,width=50)
finish.grid(row=1,column=1)

# Start the Tkinter event loop
# This is where the magic happens
sv_ttk.set_theme("dark")
root.mainloop()
