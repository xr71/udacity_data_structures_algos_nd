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

def total_time_maker(calls:list) -> dict:
    total_time_log = {}

    for call in calls:
        calling_num = call[0]
        answering_num = call[1]

        # calling time and answering time are both time spent on the phone
        # get the running time in seconds already spent by each number
        # set this number to 0 if not in dictionary yet
        # add on the new row's number of seconds
        calling_num_time = total_time_log.get(calling_num, 0)
        answering_num_time = total_time_log.get(answering_num, 0)

        total_time_log[calling_num] = calling_num_time + int(call[3])
        total_time_log[answering_num] = answering_num_time + int(call[3])

    return total_time_log

time_log = total_time_maker(calls)
max_number = max(time_log, key=time_log.get)
max_time = time_log[max_number]

print(f"{max_number} spent the longest time, {max_time} seconds, on the phone during September 2016.")
