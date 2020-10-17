#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#Problem Set 3
#16 Oct 2020
#Sarah Steele Cabrera


# In[4]:


#Problem 1
#!/usr/bin/env python

data = open('/blue/bsc4452/share/Class_Files/data/CO-OPS__8729108__wl.csv') #load data and read csv

maxwater = -1.0 #set up reference for highest water level value

next(data) #skip header row

for number, line in enumerate(data): #start the loop
    line.strip() #remove extra spaces
    waterlevel = line.split(',')[1] #add comma as column separator, select only the water level column
    date = line.split(',')[0] #assign the date column to a variable separated by commas
    timedateseparate = line.split(' ')[0] #separate the time and date into two columns
    time = timedateseparate.split(',')[0] #assign the time column to a variable separated by commas
    waterlevel.strip() #remove extra spaces at beginning and end of water level value
    if len(waterlevel) >= 1: #start loop for non-zero values of waterlevel
        waterlevel = float(line.split(',')[1]) #convert water level values into numbers to sort by numerical value
        if waterlevel >= maxwater: #look only at the next line if it is higher than the previous highest value
            maxwater = waterlevel #assign this new water level to highest
            continue #proceed to next iteration
        else: #if value isn't higher than current highest value
            continue
    else:
        continue

print(f"The maximum water level, {maxwater} ft., occured at {time} on {date}")
            


# In[8]:


#Problem 2
#!/usr/bin/env python

#copy script from above to get highest water level
data = open('/blue/bsc4452/share/Class_Files/data/CO-OPS__8729108__wl.csv') #load data and read csv

maxwater = -1.0 #set up reference for highest water level value

next(data) #skip header row

for number, line in enumerate(data): #start the loop
    line.strip() #remove extra spaces
    waterlevel = line.split(',')[1] #add comma as column separator, select only the water level column
    date = line.split(',')[0] #assign the date column to a variable separated by commas
    timedateseparate = line.split(' ')[0] #separate the time and date into two columns
    time = timedateseparate.split(',')[0] #assign the time column to a variable separated by commas
    waterlevel.strip() #remove extra spaces at beginning and end of water level value
    if len(waterlevel) >= 1: #start loop for non-zero values of waterlevel
        waterlevel = float(line.split(',')[1]) #convert water level values into numbers to sort by numerical value
        if waterlevel >= maxwater: #look only at the next line if it is higher than the previous highest value
            maxwater = waterlevel #assign this new water level to maxwater
            continue #proceed to next iteration
        else: #if value isn't higher than current highest value
            continue
    else:
        continue

print(f"The maximum water level, {maxwater} ft., occured at {time} on {date}")


#low water level
data = open('/blue/bsc4452/share/Class_Files/data/CO-OPS__8729108__wl.csv') #load data and read csv

minwater = 10.0 #set up reference for highest water level value

next(data) #skip header row

for number, line in enumerate(data): #start the loop
    line.strip() #remove extra spaces
    waterlevel = line.split(',')[1] #add comma as column separator, select only the water level column
    date = line.split(',')[0] #assign the date column to a variable separated by commas
    timedateseparate = line.split(' ')[0] #separate the time and date into two columns
    time = timedateseparate.split(',')[0] #assign the time column to a variable separated by commas
    waterlevel.strip() #remove extra spaces at beginning and end of water level value
    if len(waterlevel) >= 1: #start loop for non-zero values of waterlevel
        waterlevel = float(line.split(',')[1]) #convert water level values into numbers to sort by numerical value
        if waterlevel <= minwater: #look only at the next line if it is lower than the previous lowest value
            minwater = waterlevel #assign this new water level to minwater
            continue #proceed to next iteration
        else: #if value isn't lower than current lowest value
            continue
    else:
        continue

print(f"The minimum water level, {minwater} ft., occured at {time} on {date}")

#average water level
data = open('/blue/bsc4452/share/Class_Files/data/CO-OPS__8729108__wl.csv') #load data and read csv

counter = 0.0 #set starting points for iterations to build from
total = 0.0

next(data) #skip header row

for number, line in enumerate(data): #start the loop
    line.strip() #remove extra spaces
    waterlevel = line.split(',')[1] #add comma as column separator, select only the water level column
    date = line.split(',')[0] #assign the date column to a variable separated by commas
    timedateseparate = line.split(' ')[0] #separate the time and date into two columns
    time = timedateseparate.split(',')[0] #assign the time column to a variable separated by commas
    waterlevel.strip() #remove extra spaces at beginning and end of water level value
    if len(waterlevel) >= 1: #start loop for non-zero values of waterlevel
        waterlevel = float(line.split(',')[1]) #convert water level values into numbers to sort by numerical value
        total = (total + waterlevel)
        counter = (counter + 1)
        continue
    else: #ignore empty values
        continue
        
average = round((total/counter),3)

print(f"The average water level was {average} ft. during the sampling period")


# In[11]:


#Problem 3
#!/usr/bin/env python

data = open('/blue/bsc4452/share/Class_Files/data/CO-OPS__8729108__wl.csv') #load data and read csv

lastwaterlevel = 2.421 #reference for previous water level
lastdiff = 0 #reference for difference between measurements

next(data) #skip header row

for number, line in enumerate(data): #start the loop
    line.strip() #remove extra spaces
    waterlevel = line.split(',')[1] #add comma as column separator, select only the water level column
    date = line.split(',')[0] #assign the date column to a variable separated by commas
    timedateseparate = line.split(' ')[0] #separate the time and date into two columns
    time = timedateseparate.split(',')[0] #assign the time column to a variable separated by commas
    waterlevel.strip() #remove extra spaces at beginning and end of water level value
    if len(waterlevel) >= 1:
        waterlevel = float(line.split(',')[1]) #convert water level values into numbers to sort by numerical value
        diff = waterlevel - lastwaterlevel #caclulate the difference between current and previous water level in the loop
        lastwaterlevel = waterlevel #reassign the water level value of the current value in the loop to the previous value in the loop
        if diff >= lastdiff: #see if current difference is greater than previous greater distance
            lastdiff = diff #reassign variables for the time at greatest difference
            timeofdifference = time
            dateofdifference = date
            waterlevelafterdifference = waterlevel
            continue
        else: #ignore if difference is smaller
            continue
    else: #ignore empty values
        continue

print(f'The fastest rise in water level per 6-minute period between measurements was {lastdiff}, which was observed on {dateofdifference} at {timeofdifference}')
        


# In[23]:


#Problem 4
#!/usr/bin/env python

data = open('/blue/bsc4452/share/Class_Files/data/CO-OPS__8729108__wl.csv') #load data and read csv

lastwaterlevel = 2.421 #reference for previous water level

next(data) #skip header row

for number, line in enumerate(data): #start the loop
    line.strip() #remove extra spaces
    waterlevel = line.split(',')[1] #add comma as column separator, select only the water level column
    date = line.split(',')[0] #assign the date column to a variable separated by commas
    timedateseparate = line.split(' ')[0] #separate the time and date into two columns
    time = timedateseparate.split(',')[0] #assign the time column to a variable separated by commas
    waterlevel.strip() #remove extra spaces at beginning and end of water level value
    if len(waterlevel) >= 1:
        waterlevel = float(line.split(',')[1]) #convert water level values into numbers to sort by numerical value
        if waterlevel >= 5.0: #print warning for high water level
            print('WARNING: WATER LEVEL IS VERY HIGH!')
        else: 
            print('Water level is acceptable.')
        diff = waterlevel - lastwaterlevel #caclulate the difference between current and previous water level in the loop
        lastwaterlevel = waterlevel #reassign the water level value of the current value in the loop to the previous value in the loop
        if diff >= 0.25: #see if current difference is greater than established threshold
            print('WARNING: WATER LEVEL IS RISING QUICKLY!')
        else:
            continue
else:
    print('No reading received for this time')
        


# In[ ]:




