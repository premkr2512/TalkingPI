#Current_day = day[date.today().weekday()]
#for i in menu['day']:
#    c1+=1
#    if i.lower() == Current_day.lower():
#        for j in range(len(time1)):
#            c2+=1
#            t1 = time1[j]
#            # wish_me()
#            s = menu.iat[c1,j+1]
#            print(s)
#            speak("in" + rutine[j])
#            #time.sleep(0.5)
#            speak(s)
#from city_loc_JArvish import speak
import pandas as pd
from jarvish_speak import speak
from datetime import datetime ,date
dates = pd.read_csv("day and Dates.csv")
today_date=date.today().strftime("%d")
#Current_date = Dates & Days[]
weekDays = ("Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday")
months = ['January','February','March','April','May','June','July','August','September','October','November','December']
dt = datetime.today()
def dates_festival():
    c1=0
    c2=1
    for i in dates['Dates & Days']:
        l = len(today_date)
        j=i
        i = i[0:l]
        i = str(i)
        month_of_year = dt.month
        month_now = months[month_of_year-1]
        if i == today_date:
            if month_now in j:
                speak("Sir today'date is :",i,months[month_of_year-1],"And its time to celebrate",dates.iat[c1,c2])
    else:
        day = weekDays[datetime.today().weekday()-1]
        speak("Today is "+day+"Its a nornaml day as usual")
        c1=c1+1
    #if i.lower() == Current_day.lower():
    #    for j in range(len(time1)):
    #        c2+=1
    #        t1 = time1[j]
    #        # wish_me()
    #        s = menu.iat[c1,j+1]
    #        print(s)
    #        speak("in" + rutine[j])
    #        #time.sleep(0.5)
    #        speak(s)
