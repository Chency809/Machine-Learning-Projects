#!/usr/bin/env python3
# @Time    : 6/16/2020 9:55 AM
# @Author  : Chency Liu
# @School  : Cornell College
# @FileName: multiprocessing_test.py
# @Software: PyCharm
# @Github  : https://github.com/Chency809?tab=repositories

import multiprocessing
import time

def print_(interval):
    print("Sarts: (interval {})".format(interval))
    time.sleep(interval)
    print("Ends: (interval {})".format(interval))

# we have to add this line
if __name__ == '__main__':
    p1 = multiprocessing.Process(target = print_, args = (2, ))
    p2 = multiprocessing.Process(target=print_, args=(3,))

    p2.start()
    p1.start()
    #p1.join()


