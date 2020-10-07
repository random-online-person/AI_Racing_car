import numpy as np
from Screen_cap import grab_screen
from GetKeyPressed import key_check
import cv2
import os
import time

w = [1,0,0,0,0,0,0,0,0]
s = [0,1,0,0,0,0,0,0,0]
a = [0,0,1,0,0,0,0,0,0]
d = [0,0,0,1,0,0,0,0,0]
wa = [0,0,0,0,1,0,0,0,0]
wd = [0,0,0,0,0,1,0,0,0]
sa = [0,0,0,0,0,0,1,0,0]
sd = [0,0,0,0,0,0,0,1,0]
nk = [0,0,0,0,0,0,0,0,1]

def keys_to_output(keys):

    output = [0,0,0,0,0,0,0,0,0]

    if 'W' in keys and 'A' in keys:
        output = wa
    elif 'W' in keys and 'D' in keys:
        output = wd
    elif 'S' in keys and 'A' in keys:
        output = sa
    elif 'S' in keys and 'D' in keys:
        output = sd
    elif 'W' in keys:
        output = w
    elif 'S' in keys:
        output = s
    elif 'A' in keys:
        output = a
    elif 'D' in keys:
        output = d
    else:
        output = nk
    return output

starting_value = 1

while True:
    file_name = 'training_data-{}.npy'.format(starting_value)

    if os.path.isfile(file_name):
        print('File exists, moving along',starting_value)
        starting_value += 1
    else:
        print('File does not exist, starting fresh!',starting_value)

        break

def roi(img, vertices):
    mask = np.zeros_like(img)
    cv2.fillPoly(mask, vertices, 255)
    masked = cv2.bitwise_and(img, mask)
    return masked

vertices = np.array([[0,120],[150,110], [350,110], [480,120], [480,270], [0,270]], np.int32)

while (True):
    screen = grab_screen(region=(0,30,1010,800))
    screen = cv2.cvtColor(screen, cv2.COLOR_BGR2GRAY)
    screen = cv2.resize(screen, (480,270))
    screen = roi(screen, [vertices])
    cv2.imshow("fens", screen)
    if cv2.waitKey(25) & 0xFF == ord('q'):
        cv2.destroyAllWindows()
        break

def main(file_name, starting_value):
    """
    file_name = file_name
    starting_value = starting_value
    training_data = []
    print("test 1")
    '''
    for i in list(range(4))[::-1]:
        print(i+1)
        time.sleep(1)
        '''

    print('STARTING!!!')
    last_time = time.time()
    """
    paused = False
    ten_fps = True
    while(True):
        screen = grab_screen(region=(0,30,1010,800))
        screen = cv2.cvtColor(screen, cv2.COLOR_BGR2GRAY)
        screen = cv2.resize(screen, (480,270))
        screen = roi(screen, [vertices])
        cv2.imshow("fens", screen)

        if not paused:


            keys = key_check()
            #print('loop took {} seconds'.format(time.time()-last_time))
            '''
            if (time.time() - last_time >= 0.1):
                output = keys_to_output(keys)
                training_data.append([screen,output])
                last_time = time.time()

                if len(training_data) % 100 == 0:
                    print(len(training_data))

                    if len(training_data) == 1000:
                        np.save(file_name,training_data)
                        print('SAVED')
                        training_data = []
                        starting_value += 1
                        file_name = 'D:/Projects/self_driving_car/Training_data/training_data-{}.npy'.format(starting_value)
            #cv2.imshow('window',cv2.resize(screen,(640,360)))
            #if cv2.waitKey(25) & 0xFF == ord('q'):
            #    cv2.destroyAllWindows()
            #    break
            '''

    keys = key_check()
    if 'T' in keys:
        if paused:
            paused = False
            print('unpaused!')
            time.sleep(1)
        else:
            print('Pausing!')
            paused = True
            time.sleep(1)

file_name = 'D:/Projects/self_driving_car/Training_data/training_data-{}.npy'.format(starting_value)
#main(file_name, starting_value)
