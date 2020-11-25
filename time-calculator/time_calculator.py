def add_time(start, duration, day = None):
    
    days = ("Sunday","Monday","Tuesday","Wednesday","Thursday","Friday","Saturday")
    time,meridiem = start.split(' ')
    duration = list(map(int,duration.split(':')))
    time = list(map(int,time.split(':')))
    days_passed = 0
                
    while duration[1] > 0:
            time[1] += 1
            duration[1] -= 1
              
            if time[1] >= 60:
                time[1] -= 60
                duration[0] += 1
                
    while duration[0] > 0 :
        time[0] += 1
        duration[0] -= 1
        if time[0] == 12: 
            if meridiem == "PM":
                meridiem = "AM"
                days_passed += 1
            else:
                meridiem = "PM"  
                
        if time[0] > 12:
            time[0] -=12
    
    new_time = f"{time[0]}:{time[1]:02} {meridiem}"
    if day is not None:
        d = days.index(day.capitalize()) + days_passed
        while d >= 7:
            d -= 7
        new_time += f', {days[d]}'
        
    if days_passed == 1:
        new_time += f' (next day)'
    elif days_passed > 1:
        new_time += f' ({days_passed} days later)'

    return new_time