import os
import datetime
import time
# Get current formatted time
for _ in range(5):
    curr_time = time.strftime("%H:%M:%S")
    print(f"Current time: {curr_time}")
    time.sleep(1)
    os.system('cls')

# Countdown from 10 to 0
seconds=int(input("For how many seconds you want to set timer:"))
print("Countdown:")
for i in range(seconds, -1, -1):
    print(i)
    time.sleep(1)
print("Time's up!")









