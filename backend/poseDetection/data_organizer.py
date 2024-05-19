import pandas as pd
import time

def writeToFile(pathname, angle, count, startTime, exercise):
    df = pd.read_csv(pathname)
    delta = "neutral" #detects if angle is increasing, decreasing or staying still
    current_point = len(df)-2
    newrep = False
    struggling = False
    halfrep = False
    bugtest = "NaN"
    #make sure that we have at least 3 datapoints ()
    if current_point >= 3:
        #check previous two points to see if its increasing or decreasing
        delta_sens = 5 #sensitivity to detect increasing vs decreasing
        if df.loc[current_point, "angle"] - df.loc[current_point - 1, "angle"] < -delta_sens and df.loc[current_point - 1, "angle"] - df.loc[current_point - 2, "angle"] < -delta_sens:
            delta = "decreasing"
        elif df.loc[current_point, "angle"] - df.loc[current_point - 1, "angle"] >delta_sens and df.loc[current_point - 1, "angle"] - df.loc[current_point - 2, "angle"] >delta_sens:
            delta = "increasing"
        if exercise == "bicep":
            pass

        #check if count has changed
        if df.loc[current_point,"count"] != df.loc[current_point-1,"count"] and df.loc[current_point,"count"].is_integer():
            newrep = True
        
        
        #check if the user is struggling
        #check if the user has been in the same spot for the last 5 seconds (about 80 entries)
        struggle_sens = 50 #sensitivity for the struggling condition
        if current_point >= struggle_sens:
            for i in range(struggle_sens):
                if df.loc[current_point, "delta"] != df.loc[current_point-i,"delta"]:
                    struggling = False
                    break
                elif i == struggle_sens - 1:
                    struggling = True
                    delta = "struggling"
        
        #check if the user did a rep but didnt make it all the way
        half_rep_sens = 20
        #checks if there are enough data points and if the value should be increasing (counter value is an integer)
        if current_point >= half_rep_sens and df.loc[current_point, "count"].is_integer():
            dec_counter = 0
            for i in range(half_rep_sens):
                #check if the value i rows before is decreasing, and that the counter is an integer
                if df.loc[current_point-i, "delta"] == "decreasing" and df.loc[current_point-i, "count"].is_integer():
                    dec_counter += 1 
                    bugtest = dec_counter
                #to prevent repeats, insta break the loop if there was alraedy a half rep or struggling call
                elif df.loc[current_point-i, "delta"] == "half rep" or df.loc[current_point-i, "delta"] == "struggling":
                    dec_counter == 0
                    break
                #if at least 10 (half) of the outputs are decreasing, notify the user they did a half rep
                if dec_counter == 3:
                    halfrep = True
                    delta = "half rep"
                    break
        
    
    with open("curl_angle_count.txt", "a") as f:
        f.write(f"{bugtest},{angle},{count},{time.time() - startTime},{delta},{newrep},{struggling},{halfrep}\n")
    
    return newrep, struggling, halfrep

