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


potential_set = set()
nontelemarket_set = set()
# anyone who sends texts is not a marketer
for text in texts:
    nontelemarket_set.add(text[0])
    nontelemarket_set.add(text[1])

# anyone who makes a call is a potential suspect, but not if they receive a call
for call in calls:
    potential_set.add(call[0])
    nontelemarket_set.add(call[1])

# final telemarket set
telemarket_set = potential_set - nontelemarket_set

print("These numbers could be telemarketers:")
for tm in sorted(telemarket_set):
    print(tm)