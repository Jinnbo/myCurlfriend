import pandas as pd
import time

def writeToFile(pathname, angle, count, startTime, exercise):
    df = pd.read_csv(pathname)
    delta = "neutral" #detects if angle is increasing, decreasing or staying still
    current_point = len(df)-2
    newrep = False
    struggling = False

    #make sure that we have at least 3 datapoints ()
    if current_point >= 3:
        #detector for outliers
        # if df.loc[current_point, "angle"] - df.loc[current_point - 1, "angle"] > 50:
        #     #if the angle is an outlier, set it to the previous point
        #     angle = df.loc[current_point-1,"angle"]
        #check previous two points to see if its increasing or decreasing
        delta_sens = 10 #sensitivity to detect increasing vs decreasing
        if df.loc[current_point, "angle"] - df.loc[current_point - 1, "angle"] <-delta_sens and df.loc[current_point - 1, "angle"] - df.loc[current_point - 2, "angle"] <-delta_sens:
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
        struggle_sens = 80 #sensitivity for the struggling condition
        if current_point >= struggle_sens:
            for i in range(struggle_sens):
                if df.loc[current_point, "delta"] != df.loc[current_point-i,"delta"]:
                    struggling = False
                    break
                elif i == struggle_sens - 1:
                    struggling = True
                    delta = "not struggling"
                    print("THIS SHOULD BE NOT STRUGGLING: ", df.loc[current_point, "delta"])

        
    
    with open("curl_angle_count.txt", "a") as f:
        f.write(f"{angle},{count},{time.time() - startTime},{delta},{newrep},{struggling}\n")
    
    print("We are returning ", newrep)
    return newrep, struggling


