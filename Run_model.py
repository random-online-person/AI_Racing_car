import numpy as np
from Screen_cap import grab_screen
import cv2
import time
from directkeys import PressKey,ReleaseKey, W, A, S, D
from Model_arch import alexnet
from GetKeyPressed import key_check

import random

def roi(img, vertices):
    mask = np.zeros_like(img)
    cv2.fillPoly(mask, vertices, 255)
    masked = cv2.bitwise_and(img, mask)
    return masked

w =  [1,0,0,0,0,0]
s =  [0,1,0,0,0,0]
a =  [0,0,1,0,0,0]
d =  [0,0,0,1,0,0]
wa = [0,0,0,0,1,0]
wd = [0,0,0,0,0,1]
nk = [0,0,0,0,0,0]

def Drive(prediction):
    if (max(prediction) == prediction[0]):
        PressKey(W)
        ReleaseKey(S)
        ReleaseKey(D)
        ReleaseKey(A)
        print("W")
    elif (max(prediction) == prediction[1]):
        PressKey(S)
        ReleaseKey(W)
        ReleaseKey(D)
        ReleaseKey(A)
        print("S")
    elif (max(prediction) == prediction[2]):
        PressKey(A)
        ReleaseKey(S)
        ReleaseKey(D)
        ReleaseKey(W)
        print("A")
    elif (max(prediction) == prediction[3]):
        PressKey(D)
        ReleaseKey(S)
        ReleaseKey(W)
        ReleaseKey(A)
        print("D")
    elif (max(prediction) == prediction[4]):
        PressKey(A)
        PressKey(W)
        ReleaseKey(S)
        ReleaseKey(D)
        print("WA")
    elif (max(prediction) == prediction[5]):
        PressKey(D)
        PressKey(W)
        ReleaseKey(S)
        ReleaseKey(A)
        print("WD")

WIDTH = 480
HEIGHT = 160
LR = 1e-3
EPOCHS = 30
MODEL_NAME = 'D:/Projects/self_driving_car/Save_model/no_{}name-{}-epochs-{}.model'.format(LR, 'final_3',EPOCHS)

vertices = np.array([[0,120],[150,110], [350,110], [480,120], [480,270], [0,270]], np.int32)

model = alexnet(WIDTH, HEIGHT, LR)
model.load(MODEL_NAME)



def main():
    last_time = time.time()
    for i in list(range(4))[::-1]:
        print(i+1)
        time.sleep(1)

    paused = False

    #prob_output_normal_final = []
    while(True):

        if not paused:
            # 800x600 windowed mode
            #screen =  np.array(ImageGrab.grab(bbox=(0,40,800,640)))
            screen = grab_screen(region=(0,30,1250,750))
            screen = cv2.cvtColor(screen, cv2.COLOR_BGR2GRAY)
            screen = cv2.resize(screen, (480,270))
            screen = roi(screen, [vertices])
            screen = screen[110:270, 0:480]
            screen = screen.reshape(WIDTH,HEIGHT,1)
            prediction = model.predict([screen])[0]
            Drive(prediction)
            keys = key_check()
            #print("%.4f" % prediction[0], "%.4f" % prediction[1], "%.4f" % prediction[2], "%.4f" % prediction[3])
            #prob_output_normal_final.append(prediction)
            #if (len(prob_output_normal_final) % 250 == 0):
            #    print(len(prob_output_normal_final))

            #if(len(prob_output_normal_final) % 5000 == 0):
            #    prob_output_normal_final = np.array(prob_output_normal_final)
            #    file_name = 'D:/Projects/self_driving_car/Training_data/output-probs-normal-{}.npy'.format(4)
            #    np.save(file_name,prob_output_normal_final)
            #    print("Saved")

        keys = key_check()

        # p pauses game and can get annoying.
        if 'T' in keys:
            if paused:
                paused = False
                time.sleep(1)
            else:
                paused = True
                ReleaseKey(A)
                ReleaseKey(W)
                ReleaseKey(D)
                ReleaseKey(S)
                time.sleep(1)

main()
