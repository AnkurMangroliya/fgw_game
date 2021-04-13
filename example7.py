from pygame import mixer
from datetime import datetime
from time import time
def musiconloop(file,stopper):
    mixer.init()
    mixer.music.load(file)
    mixer.music.play()
    while True:
        a = input()
        if a == stopper:
            mixer.music.stop()
            break
def log_now(msg):
    with open("mylogs.txt","a") as f:
        f.write(f"{msg} {datetime.now()}\n")
if __name__ == '__main__':
    init_water = time()
    init_eyes = time()
    init_exercise = time()
    watersecs = 5
    exsecs = 10
    exessecs = 20

    while True:
        if time() - init_water>watersecs:
            print("water Drinking time . 'drank' to stop the alarm")
            musiconloop("water.mp3",'drank')
            init_water = time()
            log_now("drank water at ")
        if time() - init_eyes>exsecs:
            print(" eyeexercise time . 'dyeye' to stop the alarm")
            musiconloop("eye.mp3",'dyeye')
            init_eyes = time()
            log_now("eye excercise at ")
        if time() - init_exercise>exessecs:
            print(" excercise time . 'dyphy' to stop the alarm")
            musiconloop("exercise.mp3",'dyphy')
            init_exercise = time()
            log_now("pyhsical excercise  at ")

