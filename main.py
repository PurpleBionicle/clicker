import pyautogui as auto
import time
from colorama import Fore
import multiprocessing

flags = [False, False, False]
varient = [ 'photo/1.png', 'photo/2.png', 'photo/3.png', 'photo/4.png', 'photo/5.png', 'photo/6.png', 'photo/7.png',
           'photo/8.png', 'photo/9.png', 'photo/10.png', 'photo/bs.png', 'photo/bs2.png','photo/go.png']
varient2 = ['photo/1.png', 'photo/2.png', 'photo/3.png', 'photo/4.png', 'photo/5.png', 'photo/6.png', 'photo/7.png',
            'photo/8.png', 'photo/9.png', 'photo/10.png', 'photo/bs.png', 'photo/bs2.png', 'photo/go.png']


def timer():
    print(Fore.RED + 'Я начну работать через 3 сек!')

    print(Fore.MAGENTA + str(1))
    time.sleep(1)
    print(Fore.BLUE + str(2))
    time.sleep(1)
    print(Fore.GREEN + str(3))
    time.sleep(1)


def search(i, n):
    place = auto.locateOnScreen(i)
    if place:
        flags[n] = True
        auto.moveTo(place[0] + place[2] / 2, place[1] + place[3] / 2)
        auto.click()
        t2= time.time()
        print(t2-t1)
    if flags[0]==True and flags[1]==True:
        auto.moveTo(place[0]+place[2]/2,place[1]+place[3]/2)
        auto.click()


timer()
t1 = time.time()

# place = auto.locateOnScreen('bs.png')
procs = []
# for k in range(2):
for j in varient:
    multiprocessing.Process(target=search, args=(j,0)).start()

# for i in varient2:
#     # proc = multiprocessing.Process(target=search,  args=(i,))
#     # proc.start()
#     # procs.append(proc)
#     # for proc in procs:
#     #     proc.join()
#     # procs.clear()
#     multiprocessing.Process(target=search, args=(i,1)).start()

print(flags)

# auto.confirm("Are you ready?")

# screen = auto.screenshot('screenshot.png', region=(auto.size()[0] * 0.25, auto.size()[1] * 0.80,
#                                                     auto.size()[0] * 0.42, auto.size()[1] * 0.9))
#
# picture = Image.open('screenshot.png')
# cord = (0, 0, auto.size()[0] * 0.42, auto.size()[1] * 0.2) # лево, верх, право, низ
# picture.crop(cord).save('screen_new.jpg', quality=95)
#
