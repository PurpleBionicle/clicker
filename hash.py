from PIL import Image
import imagehash
import time
import pyautogui as auto
import photos
import os
import multiprocessing

# auto.confirm("Are you ready?")
found_photos = []
procs = []
vec1_hash, vec2_hash, vec3_hash = [], [], []


def make_photo():
    count = int(0)
    photo = ['first.png', 'second.png', 'third.png']

    for x in photo:
        if os.path.isfile(x):
            os.remove(x)

    screen = auto.screenshot('full.png', region=(auto.size()[0] * 0.24, auto.size()[1] * 0.80,
                                                 auto.size()[0] * 0.42, auto.size()[1] * 0.9))
    picture = Image.open('full.png')

    for i in photo:
        cord = (0, auto.size()[1] * 0.01 + count * auto.size()[1] * 0.015,
                auto.size()[0] * 0.1,
                auto.size()[1] * 0.01 + (count + 1) * auto.size()[1] * 0.015)  # лево, верх, право, низ
        picture.crop(cord).save(i, quality=95)
        count += 1
    return photo


def multiproccessing_search(vec, vec_hash, request_photo_hash):
    for index_array in range(len(vec_hash)):
        if (request_photo_hash - vec_hash[index_array]) <= 3:
            found_photos.append(vec[index_array])
            print(1)
            break


# def pic_hash(vec,i):
#     vec.append(imagehash.dhash(i))
#     return vec

def hashing():
    photo = make_photo()

    vec1 = [Image.open(x) for x in photos.varient]
    vec2 = [Image.open(x) for x in photos.varient2]
    vec3 = [Image.open(x) for x in photos.varient3]
    # vec = [vec1,vec2,vec3]

    vec1_hash, vec2_hash, vec3_hash = [], [], []

    request_photos = [Image.open(photo[0]), Image.open(photo[1]),
                      Image.open(photo[2])]
    request_photos_hash = []

    for i in vec1:
        # proc = multiprocessing.Process(target=pic_hash, args=(vec1,i))
        # proc.start()
        # procs.append(proc)
        vec1_hash.append(imagehash.dhash(i))

    for k in vec2:
        # proc = multiprocessing.Process(target=pic_hash, args=(vec2, i))
        # proc.start()
        # procs.append(proc)
        vec2_hash.append(imagehash.dhash(k))

    for n in vec3:
        # proc = multiprocessing.Process(target=pic_hash, args=(vec, i))
        # proc.start()
        # procs.append(proc)
        vec3_hash.append(imagehash.dhash(n))

    # for proc in procs:
    #     proc.join()
    # procs.clear()
    t1 = time.time()

    for x in request_photos:
        request_photos_hash.append(imagehash.dhash(x))

    for index_input in range(len(request_photos_hash)):
        for index_array in range(len(vec1_hash)):
            if (request_photos_hash[index_input] - vec1_hash[index_array]) <= 3:
                found_photos.append(vec1[index_array])
                print(1)
                break
        for index_array in range(len(vec2_hash)):
            if (request_photos_hash[index_input] - vec2_hash[index_array]) <= 3:
                found_photos.append(vec2[index_array])
                print(2)
                break

        for index_array in range(len(vec3_hash)):
            if (request_photos_hash[index_input] - vec3_hash[index_array]) <= 3:
                found_photos.append(vec3[index_array])
                print(3)
                break

    if len(found_photos) == len(request_photos):
        # place = auto.locateOnScreen(varient3[index])
        auto.moveTo(auto.size()[0] * 0.3,
                    auto.size()[1] * 0.95)
        auto.click()
        print(time.time() - t1)
        print("All photos have been found!\n")
    else:
        print("Some photos have not been found!\n")
    if os.path.isfile('full.png'):
        os.remove('full.png')
