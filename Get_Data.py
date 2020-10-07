import numpy as np
import cv2
import os
import time
from Screen_cap import grab_screen
from GetKeyPressed import key_check

w =  [1,0,0,0,0,0]
s =  [0,1,0,0,0,0]
a =  [0,0,1,0,0,0]
d =  [0,0,0,1,0,0]
wa = [0,0,0,0,1,0]
wd = [0,0,0,0,0,1]
nk = [0,0,0,0,0,0]

def keys_to_output(keys):

    output = [0,0,0,0,0,0]

    if 'W' in keys and 'A' in keys:
        output = wa
    elif 'W' in keys and 'D' in keys:
        output = wd
    elif 'S' in keys and 'A' in keys:
        output = s
    elif 'S' in keys and 'D' in keys:
        output = s
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
    file_name = 'D:/Projects/self_driving_car/Final_data/training_data_9_final-{}.npy'.format(starting_value)

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

def main(file_name, starting_value):

    file_name = file_name
    starting_value = starting_value
    paused = False
    timer = True
    training_data = []

    if timer:
        for i in range(4)[::-1]:
            print(i + 1, "sec left")
            time.sleep(1)
        print("Starting Rec")

    last_time = time.time()

    while True:
        if not paused:
            screen = grab_screen(region=(0,30,1250,750))
            screen = cv2.cvtColor(screen, cv2.COLOR_BGR2GRAY)
            screen = cv2.resize(screen, (500,288))
            screen = roi(screen, [vertices])
            screen = screen[110:270, 0:480]
            #cv2.imshow("fens", screen)
            #cv2.imshow("crop", crop)


            keys = key_check()

            output = keys_to_output(keys)
            training_data.append([screen/255,output])
            last_time = time.time()
            #print(output)


            if len(training_data) % 250 == 0:
                print(len(training_data))

                if len(training_data) == 4000:
                    np.save(file_name,training_data)
                    print('SAVED')
                    training_data = []
                    starting_value += 1
                    file_name = 'D:/Projects/self_driving_car/Final_data/training_data_9_final-{}.npy'.format(starting_value)


        if cv2.waitKey(25) & 0xFF == ord('q'):
            cv2.destroyAllWindows()
            break

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

file_name = 'D:/Projects/self_driving_car/Final_data/training_data_9_final-{}.npy'.format(starting_value)

print(file_name)

main(file_name, starting_value)
