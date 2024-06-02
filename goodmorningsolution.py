import time
timestamp = time.strftime('%H:%M:%S')
print("Current time in HH:MM:SS format:", timestamp)
hour = int(time.strftime('%H'))
print(hour)
if (hour>=0 and hour<12):
    print("Good morning!")
elif( hour >=12 and hour<17):
    print("Good afternoon.")
else:
    print("Good night.")