test_list = [2, 3, 4, 1, 4, 5, 7, 8, 10, 2, 1, 4, 5, 3, 4, 1,2,3 ,4.33,5,6,7,8,9,10, 5, 11,2,  200, 2000, 4, 12020, 2012,2, 2,2,2,2,4, 1, 2, 3, 4, 7, 8, 9, 100,]
time = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46]
# print(len(test_list), len(time))
if len(test_list) != len(time):
    print("your positional data doesn't match your time data")

final_time = []
final_velocities = []
final_lists = []
rep_vel_split = []
peak_velocity = []
location_of_peak = []

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
        ROMS.append(total_rom)
    for i in time_data:  #goes through TIME data and subtracts the last place from the first pace to get the time
        total_time = int(i[len(i) - 1]) - int(i[0])
        TIMES.append(total_time)
    while x < len(ROMS):
        v = ROMS[x]/TIMES[x]
        VELS.append(v)
        x += 1
    return VELS, ROMS, TIMES

def individual_velocities(pos, time):
    x = 0
    def determine_remove_last(x): #see if there is not an even number of data points
        if len(pos[x])/2 != int(len(pos[x])/2): #check if the len /2 is equal to the int version of len/2
            pos[len(pos) -1].pop() #Remove the last item from the 
            time[len(time) -1].pop()
    
    for i in pos:
        var = 0
        curr = []
        determine_remove_last(x) #see if u need to reverse it
        start = 0
        end = 1
        while var < len(pos[x]) /2: #go through each location in the rep
            
            d = pos[x][end] - pos[x][start]
            t = time[x][end] - time[x][start]
            v = d/t
            curr.append(v)
            start += 2
            end += 2
            var += 1
        x = x+1
        rep_vel_split.append(curr)
        curr = []

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
        peak_velocity.append(y)

def loc_peak(veloc, peaks):
    x = 0
    on_off_switch = 0
    count = [0, 0]
    for reps in veloc:
        for p in reps:
            if p == peaks[x]: #see if the velocity is the highest
                print("here is the peak")
                on_off_switch = 1
                count[0] +=1
            else:
                count[on_off_switch] += 1
        location_of_peak.append(count / len(reps))
        

final_lists, final_time = (getIncreasingLists(test_list))
# print(final_lists)
# print(final_time)
final_lists, final_time = (clean_data(final_lists, final_time))
# print(final_lists)
# print(final_time)
final_velocities, final_roms, final_elaspsed_time = calc_avg_vel(final_lists, final_time)
individual_velocities(final_lists, final_time)
find_peak_velocity(rep_vel_split)
loc_peak(rep_vel_split, peak_velocity)

print("the Velocity of the rep was ", final_velocities)
print("the ROM of the rep was ", final_roms)
print("The Time was ", final_elaspsed_time)
print("The # of reps was ", len(final_time))
print("The INDIVIDUAL rep velocties were ", rep_vel_split)
print("the Peak velocity in each rep was", peak_velocity)
print("the location of peak velocity was", location_of_peak)
