def dayOfProgrammer(year):
    totalDays = 244
    programmerDay = 256
    if year == 1918: #1918 is not a leap year
        date = programmerDay - (totalDays - 1 - 13) #because 13 days were less due to change in the calendar and 1 less because it is not a leap year 
        return str(date)+'.'+'09'+'.'+str(year)        
        
    if year > 1918:
        if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
            date = programmerDay - totalDays
        else: 
            date = programmerDay - (totalDays - 1) #-1 because it is not a leap year
    else:
        if year % 4 == 0:
            date = programmerDay - totalDays
        else:
            date = programmerDay - (totalDays - 1) #-1 because it is not a leap year
    return str(date)+'.'+'09'+'.'+str(year)