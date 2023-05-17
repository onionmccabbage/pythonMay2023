from threading import Thread
import random
import time


def sleepRand():
    time.sleep( random.random()*20 )
    print('running on a separate thread')

if __name__ == '__main__':
    '''invoke our function on a SEPARATE thread'''
    t1 = Thread(target=sleepRand)
    t2 = Thread(target=sleepRand)
    t3 = Thread(target=sleepRand)
    t1.start()
    t2.start()
    t3.start()
    t1.join()
    t2.join()
    t3.join()
    print('back to the main thread')