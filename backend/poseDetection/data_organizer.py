import pandas as pd
import time



def writeToFile(pathname, angle, count, startTime, exercise):
    df = pd.read_csv(pathname)
    delta = "neutral" #detects if angle is increasing, decreasing or staying still
    current_point = len(df)
    #make sure that we have at least 3 datapoints ()
    if current_point >= 3:
        #detector for outliers
        if df.loc[current_point, angle] - df.loc[current_point - 1, angle] > 50:
            #if the angle is an outlier, set it to the previous point
            angle = df.loc[current_point-1,angle]
        #check previous two points to see if its increasing or decreasing
        delta_sens = 5 #sensitivity to detect increasing vs decreasing
        if df.loc[current_point, "angle"] - df.loc[current_point - 1, "angle"] <-delta_sens and df.loc[current_point - 1, "angle"] - df.loc[current_point - 2, "angle"] <-delta_sens:
            delta = "decreasing"
        elif df.loc[current_point, "angle"] - df.loc[current_point - 1, "angle"] >delta_sens and df.loc[current_point - 1, "angle"] - df.loc[current_point - 2, "angle"] >delta_sens:
            delta = "increasing"
        if exercise == "bicep":
            pass
            

    
    with open("curl_angle_count.txt", "a") as f:
        f.write(f"{angle},{count},{time.time() - startTime},{delta}\n")
    
    return


