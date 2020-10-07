import numpy as np
import pandas as pd
from collections import Counter
from random import shuffle

#w =  [1,0,0,0,0,0]
#s =  [0,1,0,0,0,0]
#a =  [0,0,1,0,0,0]
#d =  [0,0,0,1,0,0]
#wa = [0,0,0,0,1,0]
#wd = [0,0,0,0,0,1]
#nk = [0,0,0,0,0,0]

file_names = []

for i in range(1, 27):
    file_names.append('D:/Projects/self_driving_car/Final_data/training_data_9_final-{}.npy'.format(i))


for i in file_names:
    lefts = []
    rights = []
    forwards = []
    backwords = []

    train_data = np.load(i)

    shuffle(train_data)

    for data in train_data:
        img = data[0]
        choice = data[1]

        if choice == [0,0,1,0,0,0] or choice == [0,0,0,0,1,0]:
            lefts.append([img,choice])
        elif choice == [1,0,0,0,0,0]:
            forwards.append([img,choice])
        elif choice == [0,0,0,1,0,0] or choice == [0,0,0,0,0,1]:
            rights.append([img,choice])
        elif choice == [0,1,0,0,0,0]:
            backwords.append([img,choice])


    print(len(lefts), len(rights))
    x = max(len(lefts), len(rights))
    forwards = forwards[:x]

    final_data = forwards + lefts + rights + backwords
    shuffle(final_data)

    print(len(final_data), "lnkn")
    np.save(i, final_data)
    print("Saved")
"""
    if q >= 20:
        final_data = forwards + lefts + rights + backwords
        shuffle(final_data)
        print(len(final_data), "lnkn")
        np.save(i, final_data)
        print("Saved")
        q = 0
        lefts = []
        rights = []
        forwards = []
        backwords = []



        if choice == [0,0,1,0,0,0,0,0,0] or choice == [0,0,0,0,1,0,0,0,0]:
            if choice == [0,0,1,0,0,0,0,0,0]:
                choice = [0,0,1,0,0,0]
            elif choice == [0,0,0,0,1,0,0,0,0]:
                choice = [0,0,0,0,1,0]
            lefts.append([img,choice])
        elif choice == [1,0,0,0,0,0,0,0,0]:
            choice = [1,0,0,0,0,0]
            forwards.append([img,choice])
        elif choice == [0,0,0,1,0,0,0,0,0] or choice == [0,0,0,0,0,1,0,0,0]:
            if choice == [0,0,0,1,0,0,0,0,0]:
                choice = [0,0,0,1,0,0]
            elif choice == [0,0,0,0,0,1,0,0,0]:
                choice = [0,0,0,0,0,1]
            rights.append([img,choice])
        elif choice == [0,1,0,0,0,0,0,0,0] or choice == [0,0,0,0,0,0,1,0,0] or choice == [0,0,0,0,0,0,0,1,0]:
            choice = [0,1,0,0,0,0]
            backwords.append([img,choice])
        else:
            counting = 1 + counting
"""
