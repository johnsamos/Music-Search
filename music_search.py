# in this project you can play music from the path you will give
from pygame import mixer, time
import os
        
print("what would you like to listen")
mypath='/home/john/Desktop/Assistant'   # Here you can change the path of the music
inp=input("give folder: ")  # Here you say to the computer wich folder you would like to play 
mixer.init()
mypath=os.path.join(mypath,inp)
for song in os.listdir(mypath):
    if song.endswith(".mp3"):    # For now the program open all the files who ends with .mp3
        print('Playing:',song)
        mixer.music.load(os.path.join(mypath,song))
        mixer.music.play()
    while mixer.music.get_busy(): 
        time.Clock().tick(1)