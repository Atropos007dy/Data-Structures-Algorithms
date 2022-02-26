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
TASK 4:
The telephone company want to identify numbers that might be doing
telephone marketing. Create a set of possible telemarketers:
these are numbers that make outgoing calls but never send texts,
receive texts or receive incoming calls.

Print a message:
"These numbers could be telemarketers: "
<list of numbers>
The list of numbers should be print out one per line in lexicographic order with no duplicates.
"""

N_text=len(texts)
N_calls=len(calls)

candidates=set()
#all number making calls:
for ii in range(N_calls):
    calling=calls[ii][0]
    candidates.add(calling)

#print(candidates)
#remove candidates that receiving calls:
for ii in range(N_calls):
    receiving=calls[ii][1]
    if receiving in candidates:
        candidates.remove(receiving)

# remove candidates that using texts:
for ii in range(N_text):
    calling=texts[ii][0]
    receiving=texts[ii][1]
    if calling in candidates:
        candidates.remove(calling)
    if receiving in candidates:
        candidates.remove(receiving)
        
candidates=sorted(candidates)
print("These numbers could be telemarketers: ")
for num in candidates:
    print(num)

