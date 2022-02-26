"""
Read file into texts and calls.
It's ok if you don't understand how to read files
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during 
September 2016.".
"""

#look at calls duration only
N=len(calls)
time_spent={} 
for ii in range(N):
    time_spent[calls[ii][0]]=time_spent.get(calls[ii][0],0)+int(calls[ii][-1])
    time_spent[calls[ii][1]]=time_spent.get(calls[ii][1],0)+int(calls[ii][-1])

#
phone = max(time_spent, key=time_spent.get)
time=time_spent[phone]
print("{:} spent the longest time, {:} seconds, on the phone during September 2016.".format(phone,time))