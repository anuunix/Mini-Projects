#!/usr/bin/env python
# coding: utf-8

# In[ ]:


username = "deepak"

import time
from pygame import mixer

def gettime():
    local_time = time.asctime(time.localtime(time.time()))
    print("Local time:", local_time)
    return local_time

def log(x):
    with open("log_file.txt", "a") as f:
        f.write("At ")
        f.write(str(gettime()))
        f.write(f" :=> {x} \n")

def music(announcement, mp3, logname, stopword="stop"):
    print(announcement)
    mixer.init()

    try:
        mixer.music.load(mp3)
    except Exception as e:
        print(f"❌ Error loading audio file '{mp3}':", e)
        return

    mixer.music.set_volume(0.7)
    mixer.music.play()
    print(f"Enter '{stopword}' to stop the music")

    while True:
        z = input().strip()
        if z.lower() == stopword.lower():
            mixer.music.stop()
            log(f"{username} {logname}")
            break
        else:
            print(f"Invalid input! Please enter '{stopword}' to stop the music.")

# ------------------------------
# Main Loop
watertime = time.time()
eyetime = time.time()
excertime = time.time()

waterzone = 27*60  # seconds
eyezone = 30*60
excerzone = 45*60

while True:
    current_hour = time.localtime().tm_hour

    if 9 <= current_hour <= 17:
        if time.time() - watertime >= waterzone:
            print("💧 Playing water reminder...")
            music("💧 Drink Water", "water-191999.mp3", "Drank Water", stopword="stop")
            watertime = time.time()

        elif time.time() - excertime >= excerzone:
            print("🏃‍♂️ Playing exercise reminder...")
            music("💪🏽🏃‍♂️ Walk", "Excercise.mp3", "Walked", stopword="stop")
            excertime = time.time()

        elif time.time() - eyetime >= eyezone:
            print("👀 Playing eye exercise reminder...")
            music("👀🧿 Eye Exercise", "Aankh.mp3", "Done Eye Exercise", stopword="stop")
            eyetime = time.time()

        time.sleep(1)  # Slight pause to avoid CPU overuse
    else:
        print("⏹️ Outside working hours. Exiting program.")
        break


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




