import pyautogui as auto
import time
from colorama import Fore
import multiprocessing

flags = []
varient = ['photo/go.png', 'photo/1.png', 'photo/2.png', 'photo/3.png', 'photo/4.png', 'photo/5.png', 'photo/6.png',
           'photo/7.png', 'photo/bs.png', 'photo/bs2.png']
varient2 = ['photo/terminal.png', 'photo/1.png', 'photo/2.png', 'photo/8.png', 'photo/9.png']
varient3 = ['photo/1.png', 'photo/2.png', 'photo/3.png', 'photo/4.png', 'photo/5.png', 'photo/6.png', 'photo/7.png',
            'photo/bs.png', 'photo/bs2.png', 'photo/info.png']


def timer():
    print(Fore.RED + 'Я начну работать через 3 сек!')

    print(Fore.MAGENTA + str(1))
    time.sleep(1)
    print(Fore.BLUE + str(2))
    time.sleep(1)
    print(Fore.GREEN + str(3))
    time.sleep(1)


def search_1(i):
    place = auto.locateOnScreen(i)

    def search_3(j):
        place = auto.locateOnScreen(j)

        if bool(place):
            print(3)
            auto.moveTo(place[0] + place[2] / 2, place[1] + place[3] / 2)
            auto.click()
            t2 = time.time()
            print(t2 - t1)
            exit(1)

    def search_2(k):
        place = auto.locateOnScreen(k)

        if bool(place):
            print(2)
            for j in varient3:
                proc = multiprocessing.Process(target=search_3, args=(j,))
                proc.start()
                procs.append(proc)
            for proc in procs:
                proc.join()
            procs.clear()

    if bool(place):
        print(1)
        for k in varient2:
            proc = multiprocessing.Process(target=search_2, args=(k,))
            proc.start()
            procs.append(proc)
        for proc in procs:
            proc.join()
        procs.clear()

    # if flags[0]==True and flags[1]==True:
    #     auto.moveTo(place[0]+place[2]/2,place[1]+place[3]/2)
    #     auto.click()


timer()
t1 = time.time()

procs = []

for i in varient:
    proc = multiprocessing.Process(target=search_1, args=(i,))
    proc.start()
    procs.append(proc)
for proc in procs:
    proc.join()
procs.clear()

# auto.confirm("Are you ready?")

# screen = auto.screenshot('screenshot.png', region=(auto.size()[0] * 0.25, auto.size()[1] * 0.80,
#                                                     auto.size()[0] * 0.42, auto.size()[1] * 0.9))
#
# picture = Image.open('screenshot.png')
# cord = (0, 0, auto.size()[0] * 0.42, auto.size()[1] * 0.2) # лево, верх, право, низ
# picture.crop(cord).save('screen_new.jpg', quality=95)
#
