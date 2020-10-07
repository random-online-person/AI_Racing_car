import cv2
import numpy as np
from Screen_cap import grab_screen
#from pytesseract import image_to_string
from tesseract import image_to_string

file_paths = []
for i in range(9):
    file_paths.append('D:/Projects/self_driving_car/Snaps/NFS_{}.PNG'.format(i + 1))

lower = np.array([50,100,100])
upper = np.array([80,255,255])

lower = np.array([0,100,100])
upper = np.array([255,255,255])

def main():
    q = 0
    k = True
    j = 0
    while k:
        #k = False
        #image_org = grab_screen(region=(0,30,1250,750))
        image_org = cv2.imread(file_paths[q])
        j = j + 0.5
        lower = np.array([55,100,100])
        upper = np.array([90,255,255])
        #image_org = cv2.bilateralFilter(image_org,9,75,75)
        speed_img = image_org[610:700, 1090:1200]
        image_org = cv2.medianBlur(image_org,5)
        image = cv2.cvtColor(image_org, cv2.COLOR_BGR2HSV)
        #speed_img =
        print(image_to_string(speed_img))
        #image_org = cv2.GaussianBlur(image_org, (3, 3), 0)
        #back = cv2.imread(bd)
        #back = cv2.resize(back, (image.shape[0], image.shape[1]))
        #crop_img = img[y:y+h, x:x+w]
        #colour_extract = image_org[500:750, 200:950]
        #image_org = cv2.GaussianBlur(image_org, (5, 5), 0)
        #colour_extract = cv2.cvtColor(colour_extract, cv2.COLOR_BGR2HSV)
        #lower, upper = colour_extracting(colour_extract)
        #print(colour_extract.shape)
        #print(lower, upper)
        #image = cv2.cvtColor(image_org, cv2.COLOR_BGR2HSV)
        #mask = cv2.inRange(image_org, lower, upper)
        #image = cv2.bitwise_and(image_org, image_org, mask= mask)
        #linesP = cv2.HoughLinesP(cv2.cvtColor(image, cv2.COLOR_BGR2GRAY), 1, np.pi / 180, 50, None, 50, 10)
        #if linesP is not None:
        #    for i in range(0, len(linesP)):
        #        l = linesP[i][0]
        #        cv2.line(image, (l[0], l[1]), (l[2], l[3]), (0,0,255), 3, cv2.LINE_AA)
        cv2.imshow("window",speed_img)
        #cv2.imshow("crop",colour_extract)
        #cv2.imshow("org", image_org)
        if cv2.waitKey(25) & 0xFF == ord('q'):
            cv2.destroyAllWindows()
            break

main()
