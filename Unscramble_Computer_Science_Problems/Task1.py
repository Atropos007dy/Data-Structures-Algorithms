"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)


"""
TASK 1:
How many different telephone numbers are there in the records? 
Print a message:
"There are <count> different telephone numbers in the records."
"""
N_calls=len(calls)
N_texts=len(texts)
seen=set()
for ii in range(N_calls):
    if calls[ii][0] not in seen:
        seen.add(calls[ii][0])
    if calls[ii][1] not in seen:
        seen.add(calls[ii][1])

for ii in range(N_texts):
    if texts[ii][0] not in seen:
        seen.add(texts[ii][0])
    if texts[ii][1] not in seen:
        seen.add(texts[ii][1])

count=len(seen)
print("There are {:} different telephone numbers in the records.".format(count))