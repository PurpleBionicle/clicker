import time
from colorama import Fore
import hash

def timer():
    print(Fore.RED + 'Я начну работать через 3 сек!')

    print(Fore.MAGENTA + str(1))
    time.sleep(1)
    print(Fore.BLUE + str(2))
    time.sleep(1)
    print(Fore.GREEN + str(3))
    time.sleep(1)

if __name__ == "__main__":
    timer()
    t1 = time.time()
    hash.hashing()
    print(time.time()-t1)
    # locate_on_screen()

