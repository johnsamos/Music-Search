from pygame import mixer, time
import os
        
print("what would you like to listen")
mypath='/Users/johny/Music/'   # Here you can change the path of the music
inp=input("give folder: ")  # input your folder name for example rock to start playing music from this file 
mixer.init()
mypath=os.path.join(mypath,inp)
for song in os.listdir(mypath):
    if song.endswith(".mp3"):   
        print('Playing:',song)
        mixer.music.load(os.path.join(mypath,song))
        mixer.music.play()
    while mixer.music.get_busy(): 
        time.Clock().tick(1)
