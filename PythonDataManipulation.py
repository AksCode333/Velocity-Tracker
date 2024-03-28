import serial
from subprocess import call
from matplotlib import pyplot as plt
import tkinter as tk
from tkinter import ttk
import sv_ttk
import datetime
import gspread
from oauth2client.service_account import ServiceAccountCredentials

SERIAL_PORT = 'COM3'
BAUD_RATE = 115200
ser = serial.Serial(SERIAL_PORT, BAUD_RATE)

#google sheets stuff
scope = ["https://spreadsheets.google.com/feeds",'https://www.googleapis.com/auth/spreadsheets',"https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]
creds = ServiceAccountCredentials.from_json_keyfile_name("creds.json", scope)
client = gspread.authorize(creds)
sheet = client.open("Fitness").sheet1

now = datetime.datetime.now()
formatted_date = now.strftime("%m/%d/%y")

aquired_pos = []
aquired_time = []
check = [False]

def read_and_process_data():
    line = ser.readline().decode('utf-8').strip()
    sensorValues = line.split(',')

    aquired_pos.append(round(float(sensorValues[0]), 2))
    aquired_time.append(round(float(sensorValues[1])/10000, 2))

# test_list = [2, 3, 4, 1, 4, 5, 7, 8, 10, 2, 1, 4, 5, 3, 4, 1,2,3 ,4.33,5,6,7,8,9,10, 5, 11,2,  200, 2000, 4, 12020, 2012,2, 2,2,2,2,4, 1, 2, 3, 4, 7, 8, 9, 100,]
# time = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46]
test_list = aquired_pos
time = aquired_time
# print(len(test_list), len(time))
if len(test_list) != len(time):
    print("your positional data doesn't match your time data")

final_time = []
final_velocities = []
final_accelerations = []
final_lists = []
rep_vel_split = []
rep_acel_slit = []
peak_velocity = []
peak_acceleration = []
location_of_peak = []
location_of_acell_peak = []

def getIncreasingLists(list):
    x = 0
    results = []
    current = [list[0]]
    time_current = [time[0]]
    time_results = []
    for i in range(1, len(list)): #go through the whole length of the list for each calue
        if list[i-1] <= list[i]: #check if number is increaseing
            current.append(list[i]) #make the number the one were loooking for it it was larger than the last
            time_current.append(time[i])
        else:
            results.append(current) #Add the whole string toresults
            time_results.append(time_current)
            current = [list[i]] #Go on to the next
            time_current = [time[i]]
        if i == len(list) - 1: #also check if it is the last value
            results.append(current) #finish
            time_results.append(time_current)
    return results, time_results

def clean_data(pos, time):
    x = 0
    while(x < len(pos)): #while the rep we are looking at is les than the total number of reps
        if len(pos[x]) < 4: #if there is less than 4 data points
            del(pos[x]) #remove them
            del(time[x])
            x = x -1 #ignore this as one of the options becuase we just removed it
        x = x+1 #look at the next rep

    return pos, time

def calc_avg_vel(position_data, time_data):
    ROMS = []
    TIMES = []
    VELS = []
    x= 0
    for i in position_data: #goes through pos data and subtracts the last place from the first pace to get the time
        total_rom = int(i[len(i) - 1]) - int(i[0])
        ROMS.append(round(total_rom, 2))
    for i in time_data:  #goes through TIME data and subtracts the last place from the first pace to get the time
        total_time = int(i[len(i) - 1]) - int(i[0])
        TIMES.append(round(total_time,2))
    while x < len(ROMS):
        v = ROMS[x]/TIMES[x]
        VELS.append(round(v, 2))
        x += 1
    return VELS, ROMS, TIMES

def calc_avg_acell(velocity, times):
    rep_number = 0
    for i in velocity:
        z = velocity[rep_number] / (times[rep_number]/100)
        z = round(z, 3)
        final_accelerations.append(z)
        rep_number = rep_number + 1

def individual_velocities(pos, time): #and acellerations
    x = 0
    def determine_remove_last(x): #see if there is not an even number of data points
        if len(pos[x])/2 != int(len(pos[x])/2): #check if the len /2 is equal to the int version of len/2
            pos[len(pos) -1].pop() #Remove the last item from the 
            time[len(time) -1].pop()
            print("OD NUMBER")
    
    for i in pos:
        var = 0
        curr = []
        acel_curr = []
        determine_remove_last(x) #see if u need to reverse it
        start = 0
        end = 1
        while var < len(pos[x]) /2 -1: #go through each location in the rep
            d = pos[x][end] - pos[x][start]
            t = time[x][end] - time[x][start]
            v = d/t
            a = v/t
            curr.append(v)
            acel_curr.append(round(a, 3))
            start += 2
            end += 2
            var += 1
        x = x+1
        rep_vel_split.append(curr)
        rep_acel_slit.append(acel_curr)
        curr = []
        acel_curr = []

def find_peak_velocity(velocties):
    for reps in velocties: #goe through each rep
        x = [0]
        for vel in reps: #Geoes through each velcotiy location within on the rep
            x.append(vel)# adds the new veloity to the list
            if x[1] > x[0]: #checks if it is larger
                y = x[1] #if it is larger than add to results
                del(x[0])
            else:
                del(x[1])
        peak_velocity.append(round(y, 3))

def find_peak_acelleration(acellerations):
    for reps in acellerations:
        x = [0]
        for acell in reps: #Geoes through each velcotiy location within on the rep
            x.append(acell)# adds the new veloity to the list
            if x[1] > x[0]: #checks if it is larger
                y = x[1] #if it is larger than add to results
                del(x[0])
            else:
                del(x[1])
        peak_acceleration.append(y)

def loc_peak(veloc, peaks):
    x = 0
    on_off_switch = 0
    count = [0, 0]
    for reps in veloc:
        for p in reps:
            if p == peaks[x]: #see if the velocity is the highest
                on_off_switch = 1
                count[0] +=1
            else:
                count[on_off_switch] += 1
        location_of_peak.append(round(count[0] / len(reps), 2* 100))
        x=x+1
        count = [0, 0]
        on_off_switch = 0

def loc_peak_acell(acell, peaks):
    x = 0
    on_off_switch = 0
    count = [0, 0]
    for reps in acell:
        for p in reps:
            if p == peaks[x]: #see if the velocity is the highest
                on_off_switch = 1
                count[0] +=1
            else:
                count[on_off_switch] += 1
        location_of_acell_peak.append(round(count[0] / len(reps), 2* 100))
        x=x+1
        count = [0, 0]
        on_off_switch = 0

rep_dict = {}

def create_dict(poss, time, indi_vel, peak, peak_loc, times, vel, acell, indiv_acell, acell_peak, acell_peak_loc, roms, ELAPSED_TIME):   
    rep_number = 0
    for i in poss:
        to_add = {("rep " + str(rep_number + 1)): [poss[rep_number], times[rep_number], indi_vel[rep_number], peak[rep_number], peak_loc[rep_number], time[rep_number], vel[rep_number],acell[rep_number], indiv_acell[rep_number], acell_peak[rep_number], acell_peak_loc[rep_number], roms[rep_number], rep_number+1, ELAPSED_TIME[rep_number]]}
        rep_dict.update(to_add)
        rep_number += 1

def delete_rep(x):
        del rep_dict["rep " + str(x)]
        # print(rep_dict)

conv_to_seconds = []

def make_the_data():
    final_lists, final_time = (getIncreasingLists(test_list))
    final_lists, final_time = (clean_data(final_lists, final_time))
    final_velocities, final_roms, final_elaspsed_time = calc_avg_vel(final_lists, final_time)
    calc_avg_acell(final_velocities, final_elaspsed_time)
    individual_velocities(final_lists, final_time)
    find_peak_velocity(rep_vel_split)
    find_peak_acelleration(rep_acel_slit)
    loc_peak(rep_vel_split, peak_velocity)
    loc_peak_acell(rep_acel_slit, peak_acceleration)

    for i in final_elaspsed_time:
        conv_to_seconds.append(i/100)

    print("the Velocitys of the reps was ", final_velocities)
    print("the Acellerations of the reps was ", final_accelerations)
    print("the ROM of the rep was ", final_roms)
    print("The Time was ", conv_to_seconds)
    print("The # of reps was ", len(final_time))
    # print("The INDIVIDUAL rep velocties were ", rep_vel_split)
    # print("the individual acelerations were ", rep_acel_slit)
    print("the Peak velocity in each rep was", peak_velocity)
    print("the Peak acceleration in each rep was", peak_acceleration)
    print("the location of peak velocity was", location_of_peak, "%")
    print("the location of aceleration velocity was", location_of_acell_peak, "%")

        
    create_dict(final_lists, final_time, rep_vel_split, peak_velocity, location_of_peak, conv_to_seconds, final_velocities, final_accelerations, rep_acel_slit, peak_acceleration, location_of_acell_peak, final_roms, final_elaspsed_time)

    # x_data1 = final_elaspsed_time
    # y_data1 = final_velocities

    # x_data2 = aquired_pos[0]
    # y_data2 = aquired_time[0]

    # fig = plt.figure()
    # ax1 = fig.add_subplot(1, 2, 1)
    # ax2 = fig.add_subplot(1, 2, 2)
    # ax1.plot(x_data1, y_data1, label='data 1')
    # ax2.plot(x_data2, y_data2, label='data 2')
    # ax1.set_xlabel('Time (s)')
    # ax1.set_ylabel('Scale (Bananas)')
    # ax1.set_title('first data set')
    # ax1.legend()
    # ax2.set_xlabel('Time (s)')
    # ax2.set_ylabel('Scale (Bananas)')
    # ax2.set_title('second data set')
    # ax2.legend()

    # plt.show()
# make_the_data()
def run():
    while check[0] == True:
            root.update()
            read_and_process_data()
            if check[0] == False:
                print("Keyboard Interrupt")
                # print(aquired_pos)
                # print(aquired_time)
                make_the_data()
                delayed_show()


class show_rep():
    def __init__(self, list):
        #final_lists, final_time, rep_vel_split, peak_velocity, location_of_peak, conv_to_seconds, final_velocities, final_accelerations, rep_acel_slit, peak_acceleration, location_of_acell_peak, final_roms, rep nubmer
        self.rep_num = list[12]
        self.velocity = list[6]
        self.range_of_motion = list[11]
        self.rep_time = list[1]
        self.peak_velocitys = list[3]
        self.peak_accel = list[9]
    

    def make_tkvalues(name):
        number = ('REP #: ' + str(name.rep_num))
        vel = ('REP VEL: ' + str(name.velocity))
        rom = ('REP ROM: ' + str(name.range_of_motion))
        time = ('REP TIME: ' + str(name.rep_time))
        peakv = ('PEAK VEL: ' + str(name.peak_velocitys))
        peaka = ('PEAK ACELL: ' + str(name.peak_accel))

        def show():
            #determine which row it should be ing
            n = name.rep_num
            if n < 6:
                rowv = values1
                values1.pack(expand=True, fill="both", padx=10, pady=10)
            elif(n > 5 and n < 11):
                rowv= values2
                values2.pack(expand=True, fill="both", padx=10, pady=10)
            elif(n > 10 and n < 16):
                rowv= values3
                values3.pack(expand=True, fill="both", padx=10, pady=10)
            elif(n > 15 and n < 21):
                rowv= values4
                values4.pack(expand=True, fill="both", padx=10, pady=10)

            #make the rep box and put it down
            rep_storage = ttk.Frame(rowv, borderwidth=5, relief="sunken")
            rep_storage.pack(expand=True,side=tk.LEFT,padx=6,pady=6)

            rep_numbers = ttk.Label(rep_storage, text=number,padding=5)
            rep_numbers.grid(row=0, column=0)
            vel_value = ttk.Label(rep_storage, text=vel, padding=5)
            vel_value.grid(row=1, column=0)
            rom_value = ttk.Label(rep_storage, text=rom, padding=5)
            rom_value.grid(row=2, column=0)
            time_value = ttk.Label(rep_storage, text=time, padding=5)
            time_value.grid(row=3, column=0)
            peak_v = ttk.Label(rep_storage, text=peakv, padding=5)
            peak_v.grid(row=4, column=0)
            peak_a = ttk.Label(rep_storage, text=peaka, padding=5)
            peak_a.grid(row=5, column=0)
            delete_reps = ttk.Button(rep_storage, text="DELETE " + str(number), padding = 5, command=lambda: delete_rep(n))
            delete_reps.grid(row = 6, column=0)

        show()

def finalize_data():
    #CALCULATING AVG VELOCITY
    ca = 0
    for i in rep_dict:
        ca = ca + rep_dict[i][6]
    ca = ca/len(rep_dict)

    aa = 0
    for i in rep_dict:
        aa = aa + rep_dict[i][7]
    aa = aa/len(rep_dict)

    ar = 0
    for i in rep_dict:
        ar = ar + rep_dict[i][11]
    ar = ar/len(rep_dict)

    at = 0
    for i in rep_dict:
            at = at + rep_dict[i][13]
    at = at/len(rep_dict)
    
    SEND_TO_GOOGLE_SHEETS = [formatted_date, shared_variable, weight_entry.get(),len(rep_dict), ca, aa, ar, at, "rom deviation", "vel Droppoff", "random"] # len(FINAL_VELOCITIES), sum(FINAL_VELOCITIES)/len(FINAL_VELOCITIES), sum(FINAL_ROMS)/ len(FINAL_VELOCITIES), sum(FINAL_TIMES)/len(FINAL_ROMS)
    for i in rep_dict:# poss 0, time 1, indi_vel 2, peak 3, peak_loc 4, times 5, vel 6, acell 7, indiv_acell 8, acell_peak 9, acell_peak_loc 10, roms 11
        SEND_TO_GOOGLE_SHEETS.append(rep_dict[i][6]) #vel
    while len(SEND_TO_GOOGLE_SHEETS) < 21: #adds in the blank ones so that I can keep adding to the google sehets past the resp
        SEND_TO_GOOGLE_SHEETS.append("")

    for i in rep_dict:
        SEND_TO_GOOGLE_SHEETS.append(rep_dict[i][13]) #TIMES
    while len(SEND_TO_GOOGLE_SHEETS) < 31: 
        SEND_TO_GOOGLE_SHEETS.append("")

    for i in rep_dict:
        SEND_TO_GOOGLE_SHEETS.append(rep_dict[i][11]) #ROMS
    while len(SEND_TO_GOOGLE_SHEETS) < 41: 
        SEND_TO_GOOGLE_SHEETS.append("")

    for i in rep_dict:
        SEND_TO_GOOGLE_SHEETS.append(rep_dict[i][3]) #PEAK VELOCITY 
    while len(SEND_TO_GOOGLE_SHEETS) < 51: 
        SEND_TO_GOOGLE_SHEETS.append("")

    for i in rep_dict:
        SEND_TO_GOOGLE_SHEETS.append(rep_dict[i][4]) #PEAK VELOCITY LOCATION
    while len(SEND_TO_GOOGLE_SHEETS) < 61: 
        SEND_TO_GOOGLE_SHEETS.append("")

    for i in rep_dict:
        SEND_TO_GOOGLE_SHEETS.append(rep_dict[i][9]) #PEAK ACELLERATION
    while len(SEND_TO_GOOGLE_SHEETS) < 71: 
        SEND_TO_GOOGLE_SHEETS.append("")

    for i in rep_dict:
        SEND_TO_GOOGLE_SHEETS.append(rep_dict[i][10]) #PEAK ACELERATION LOCATION
    while len(SEND_TO_GOOGLE_SHEETS) < 81: 
        SEND_TO_GOOGLE_SHEETS.append("")

    for i in rep_dict:
        SEND_TO_GOOGLE_SHEETS.append(rep_dict[i][7]) #ACELLERATIOSN
    while len(SEND_TO_GOOGLE_SHEETS) < 91: 
        SEND_TO_GOOGLE_SHEETS.append("")

    sheet.insert_row(SEND_TO_GOOGLE_SHEETS, 2)

def should_check():
    check[0] = True
    print("go")
    run()
    # start_all()
def shouldnt_check():
    check[0] = False
    

# Create the main window
# def start_all():
#     while(check[0] == True):
#         print("tests")
#         make_the_data()
#         root.update()
#     else:
#         print("ITS IS NO")

root = tk.Tk()
root.title("Velocity tracker")

# Set window size
root.geometry("900x900")

# Create a frame to hold the buttons
button_frame = ttk.Frame(root)
button_frame.pack(expand=True, side=tk.TOP)

def kg_or_lb(value):
    global kglb
    kglb = value
# Create and place the buttons within the frame
button1 = ttk.Button(button_frame, text="Start Set",command=lambda: should_check(), padding=20)
button1.grid(row=0, column=0, padx=50, pady=10)

button2 = ttk.Button(button_frame, text="Pause Set",command=lambda: shouldnt_check(), padding=20)
button2.grid(row=0, column=1, padx=50, pady=10)

button3 = ttk.Button(button_frame, text="Reset", padding=20)
button3.grid(row=0, column=2,  padx=50, pady=10)

button4 = ttk.Button(button_frame, text="Send Data",command=lambda: finalize_data(), padding=20)
button4.grid(row=0, column=3, padx=50, pady=10)

#creates the widgets for enteringthe set data
# Weight Choice
DECIDER_frame = ttk.Frame(root,borderwidth=5, relief="sunken",padding= 1)
DECIDER_frame.pack(expand=True, side=tk.TOP)
weight_frame = ttk.Frame(button_frame,borderwidth=5, relief="sunken",padding= 1)
weight_frame.grid(row=1, column=0, columnspan=2)
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
shared_variable = ""
# Start the GUI event loop
text_var = tk.StringVar()
text_var.set(shared_variable)

def update_text(value):
    global shared_variable
    shared_variable = value
    text_var.set(shared_variable)  # Update the text box with the new value
    
#DO THE LIFT TYPE CHOCIEC
#Create a frame to push all of the other info into the center
frame = ttk.Frame(button_frame,borderwidth=5, relief="sunken",padding= 1)
frame.grid(row=1, column=2,pady=10, padx=10, columnspan=2)

text_box = ttk.Entry(frame, textvariable=text_var, state='readonly', width=30)
text_box.grid(row=0, column=1, columnspan=3,padx=10, pady=10)

# Create three buttons that update the shared variable with different values
button1 = ttk.Button(frame, text="Bench", command=lambda: update_text('Bench'), padding=10)
button1.grid(row=1, column=1)

button2 = ttk.Button(frame, text="Squat", command=lambda: update_text('Squat'), padding=10)
button2.grid(row=1, column=2)

button3 = ttk.Button(frame, text="Deadlift", command=lambda: update_text('Deadlift'), padding=10)
button3.grid(row=1, column=3, pady=10)

liftcho = ttk.Label(frame, text="LIFT TYPE")
liftcho.grid(row=0, column=0, padx=10, pady=40)

values1 = ttk.Frame(root, borderwidth=3, relief="sunken")
values2 = ttk.Frame(root, borderwidth=3, relief="sunken")
values3 = ttk.Frame(root, borderwidth=3, relief="sunken")
values4 = ttk.Frame(root, borderwidth=3, relief="sunken")


def delayed_show():
    for i in rep_dict:
        rep = show_rep(rep_dict[i])
        rep.make_tkvalues()
        root.update()

sv_ttk.set_theme("dark")
root.mainloop()

