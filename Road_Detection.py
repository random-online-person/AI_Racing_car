import numpy as np
import cv2
from Screen_cap import grab_screen
from GetKeyPressed import key_check
import time
import math

def canny_edge_detector(image):
    blur = cv2.GaussianBlur(image, (5, 5), 0)
    canny = cv2.Canny(blur, 270, 350)
    return canny

def roi(img, vertices):
    mask = np.zeros_like(img)
    cv2.fillPoly(mask, np.int32([vertices]), 255)
    masked = cv2.bitwise_and(img, mask)
    return masked

def create_coordinates(image, line_parameters,ints):
    x1, y1, x2, y2 = 0,0,0,0
    if not np.isnan(line_parameters).any():
        slope, intercept = line_parameters[0],line_parameters[1]
        print(image.shape)
        y1 = image.shape[0]
        y2 = int(y1 * (3 / 5))
        x1 = int((y1 - intercept) / slope)
        x2 = int((y2 - intercept) / slope)
    return np.array([x1, y1, x2, y2])

def average_slope_intercept(image, lines):
    left_fit = []
    right_fit = []
    for line in lines:
        x1, y1, x2, y2 = line.reshape(4)
        parameters = np.polyfit((x1, x2), (y1, y2), 1)
        slope = parameters[0]
        intercept = parameters[1]
        print(parameters,"para")
        if slope < 0:
            left_fit.append((slope, intercept))
        else:
            right_fit.append((slope, intercept))

    left_fit_average = np.average(left_fit, axis = 0)
    right_fit_average = np.average(right_fit, axis = 0)
    print(left_fit_average,"left_array")
    left_line = create_coordinates(image, left_fit_average,2)
    right_line = create_coordinates(image, right_fit_average,3)
    return np.array([left_line, right_line])

def display_lines(image, lines, sor):
    print(sor, lines.shape)
    line_image = np.zeros_like(image)
    if (lines is not None):
        print((x1, y1, x2, y2))
        cv2.line(line_image, (x1, y1), (x2, y2), (255, 0, 0), 10)
    return line_image

def mask_by_colour(image, lower, upper):
    mask = cv2.inRange(image, lower, upper)
    masked_image = cv2.bitwise_and(image, image, mask = mask)
    return masked_image

paused = False

vertices = np.array([[0,750],[0,350], [1250,350], [1250,750]], np.int32)

def main():
    while True:
        if not paused:
            screen = grab_screen(region=(0,30,1250,750))
            org_screen = screen
            screen = cv2.cvtColor(screen, cv2.COLOR_BGR2HSV)
            screen_TEMP = canny_edge_detector(screen)
            screen_TEMP = roi(screen_TEMP, vertices)
            linesP = cv2.HoughLinesP(screen_TEMP, 1, np.pi / 180, 50, None, 50, 10)
            if linesP is not None:
                for i in range(0, len(linesP)):
                    l = linesP[i][0]
                    cv2.line(org_screen, (l[0], l[1]), (l[2], l[3]), (0,0,255), 3, cv2.LINE_AA)
            #org_screen = mask_by_colour(org_screen, np.array([0, 50, 50]), np.array([255, 100, 100]))
            screen = cv2.resize(org_screen, (500, 300))
            cv2.imshow("result",screen)
        if cv2.waitKey(25) & 0xFF == ord('q'):
            cv2.destroyAllWindows()
            break


main()
