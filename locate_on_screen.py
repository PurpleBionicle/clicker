import pyautogui as auto
import multiprocessing
import time
import photos

procs = []

def search_1(i):
    place = auto.locateOnScreen(i)

    def search_3(j):
        place = auto.locateOnScreen(j)

        if bool(place):
            print(3)
            auto.moveTo(place[0] + place[2] / 2, place[1] + place[3] / 2)
            auto.click()
            exit(1)

    def search_2(k):
        place = auto.locateOnScreen(k)

        if bool(place):
            print(2)
            for j in photos.varient3:
                proc = multiprocessing.Process(target=search_3, args=(j,))
                proc.start()
                procs.append(proc)
            for proc in procs:
                proc.join()
            procs.clear()

    if bool(place):
        print(1)
        for k in photos.varient2:
            proc = multiprocessing.Process(target=search_2, args=(k,))
            proc.start()
            procs.append(proc)
        for proc in procs:
            proc.join()
        procs.clear()

    # if flags[0]==True and flags[1]==True:
    #     auto.moveTo(place[0]+place[2]/2,place[1]+place[3]/2)
    #     auto.click()

def locate_on_screen():

    for i in photos.varient:
        proc = multiprocessing.Process(target=search_1, args=(i,))
        proc.start()
        procs.append(proc)
    for proc in procs:
        proc.join()
    procs.clear()