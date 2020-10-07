import cv2
from Screen_cap import grab_screen
from directkeys import PressKey,ReleaseKey, W, A, S, D
from GetKeyPressed import key_check
import time
import pytesseract
from sklearn.externals import joblib

def get_3_points(image):
    points_coord = []
    higth, width, ch = image.shape
    points_coord.append([(higth*2)/3, width/2])
    points_coord.append([(higth*2)/3, (width * 2)/7])
    points_coord.append([(higth*2)/3, (width * 5)/7])
    return points_coord

def process_image(img):
    img = cv2.medianBlur(img,5)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    return img

def get_point_data(img, point_coord, size):
    avg_colours = []
    color = (0, 0, 0)
    for coord in point_coord:
        temp_img = img[int(coord[0]-size):int(coord[0]+size), int(coord[1]-size):int(coord[1]+size)]
        start =  (int(coord[1]-size),int(coord[0]-size))
        end =  (int(coord[1]+size),int(coord[0]+(size*2)))
        img = cv2.rectangle(img, start,  end, color, 5)
        avg_colours.append(get_avg_colour(temp_img))
    return avg_colours, img

def get_avg_colour(img):
    colour_value = []
    for i in range(img.shape[0]):
        for j in range(img.shape[1]):
            colour_value.append(img[i][j])
    return (sum(colour_value)/(img.shape[0] * img.shape[1]))

def process_data(points_data):
    rigth = False
    left = False
    if int(points_data[0]) in range(int(points_data[1] - 20), int(points_data[1] + 20)):
        rigth = True
    if int(points_data[0]) in range(int(points_data[2] - 20), int(points_data[2] + 20)):
        left = True
    check_path(rigth, left)

def check_path(rigth, left):
    if rigth and left:
        drive("w")
    elif rigth and not left:
        drive("d")
    elif not rigth and left:
        drive("a")
    else:
        drive("s")

def drive(key):
    if key == "w":
        PressKey(W)
        ReleaseKey(S)
        ReleaseKey(D)
        ReleaseKey(A)
        print("W")
    elif key == "a":
        PressKey(A)
        ReleaseKey(S)
        ReleaseKey(D)
        ReleaseKey(W)
        print("A")
    elif key == "d":
        PressKey(D)
        ReleaseKey(S)
        ReleaseKey(A)
        ReleaseKey(W)
        print("D")
    elif key == "s":
        PressKey(S)
        ReleaseKey(W)
        print("S")

def get_speed(img):
    speed_img = img[637:670, 1120:1185]
    speed_img = cv2.cvtColor(speed_img, cv2.COLOR_BGR2GRAY)
    ret,speed_img = cv2.threshold(speed_img,127,255,cv2.THRESH_BINARY_INV)
    speed_img = cv2.medianBlur(speed_img,5)
    custom_config = r'--oem 3 --psm 6 outputbase digits'
    speed_img = cv2.Canny(speed_img, 100, 200)
    speed = pytesseract.image_to_string(speed_img, config=custom_config)
    return speed,speed_img


file_paths = []
for i in range(9):
    file_paths.append('D:/Projects/self_driving_car/Snaps/NFS_{}.PNG'.format(i + 1))

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files (x86)\Tesseract-OCR\tesseract.exe"

def main():
    paused = False
    while not paused:
        #image_org = cv2.imread(file_paths[0])
        image_org = grab_screen(region=(0,30,1250,750))
        #speed, speed_img = get_speed(image_org)
        points = get_3_points(image_org)
        image = process_image(image_org)
        point_colour_value, image_org = get_point_data(image, points, 50)
        #print(type(speed))
        process_data(point_colour_value)
        #
        color = (0, 0, 0)
        image_org = cv2.rectangle(image_org, (1120,635),  (1185,670), color, 5)
        #cv2.imshow("window",  cv2.resize(image_org, (500, 300)))
        #cv2.imshow("window",  cv2.resize(speed_img, (500, 300)))
        if cv2.waitKey(25) & 0xFF == ord('q'):
            cv2.destroyAllWindows()
            break
        keys = key_check()
        if 'T' in keys:
            print("son")
            if paused:
                paused = False
                print('unpaused!')
                time.sleep(1)
            else:
                print('Pausing!')
                paused = True
                time.sleep(1)


main()
