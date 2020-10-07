from keras.models import Model
from YOLO_V3 import decode_netout, correct_yolo_boxes, do_nms, draw_boxes
import numpy as np
from numpy import expand_dims
from keras.models import load_model
from keras.preprocessing.image import load_img
from keras.preprocessing.image import img_to_array
import cv2
from PIL import Image
from Screen_cap import grab_screen
from GetKeyPressed import key_check
import time

#from matplotlib import pyplot
#from matplotlib.patches import Rectangle

anchors = [[116,90,  156,198,  373,326],  [30,61, 62,45,  59,119], [10,13,  16,30,  33,23]]
labels = ["person", "bicycle", "car", "motorbike", "aeroplane", "bus", "train", "truck", \
          "boat", "traffic light", "fire hydrant", "stop sign", "parking meter", "bench", \
          "bird", "cat", "dog", "horse", "sheep", "cow", "elephant", "bear", "zebra", "giraffe", \
          "backpack", "umbrella", "handbag", "tie", "suitcase", "frisbee", "skis", "snowboard", \
          "sports ball", "kite", "baseball bat", "baseball glove", "skateboard", "surfboard", \
          "tennis racket", "bottle", "wine glass", "cup", "fork", "knife", "spoon", "bowl", "banana", \
          "apple", "sandwich", "orange", "broccoli", "carrot", "hot dog", "pizza", "donut", "cake", \
          "chair", "sofa", "pottedplant", "bed", "diningtable", "toilet", "tvmonitor", "laptop", "mouse", \
          "remote", "keyboard", "cell phone", "microwave", "oven", "toaster", "sink", "refrigerator", \
          "book", "clock", "vase", "scissors", "teddy bear", "hair drier", "toothbrush"]

model = load_model('D:/Projects/self_driving_car/Save_model/model.h5')

filename = 'C:/Users/yasht/Desktop/junk/Holi/DSC_0158.JPG'

def load_image_pixels(filename, shape):
    image = load_img(filename)
    width, height = image.size
    image = load_img(filename, target_size=shape)
    image = img_to_array(image)
    image = image.astype('float32')
    image /= 255.0
    image = expand_dims(image, 0)
    return image, width, height

def nparray_to_image(img):

    data = img.ctypes.data_as(POINTER(c_ubyte))
    image = ndarray_image(data, img.ctypes.shape, img.ctypes.strides)

    return image

input_w, input_h = 416, 416

#image, image_w, image_h = load_image_pixels(filename, (input_w, input_h))

#print(type(image))
#print(image.shape)

#yhat = model.predict(image)

#print([a.shape for a in yhat])

class_threshold = 0.6
nms_threshold = 0.5

#boxes = list()
#for i in range(len(yhat)):
#	boxes += decode_netout(yhat[i][0], anchors[i], class_threshold,nms_threshold, input_h, input_w)

#correct_yolo_boxes(boxes, image_h, image_w, input_h, input_w)

#do_nms(boxes, 0.5)

#org_image = cv2.imread(filename,0)

#print(type(org_image))

#draw_boxes(org_image, boxes, labels, class_threshold)

#org_image = (org_image.squeeze()*255).astype(np.uint8)

#img = Image.fromarray(org_image, mode='RGB')
#img.show()


#image = Image.fromarray(image.astype('uint8'), 'RGB')

#image = nparray_to_image(image)

#cv2.imwrite(filename[:-4] + '_detected' + filename[-4:], org_image)
image_w, image_h = 1250, 720

def main():
    paused = False
    while True:
        if not paused:
            screen = grab_screen(region=(0,30,1250,750))
            screen = cv2.cvtColor(screen, cv2.COLOR_BGR2RGB)
            org_image = screen
            screen = cv2.resize(screen,(input_w, input_h))
            screen = img_to_array(screen)
            screen /= 255.0
            screen = expand_dims(screen, 0)
            #screen = cv2.resize(screen,(1, 416, 416, 3))
            yhat = model.predict(screen)
            boxes = list()
            for i in range(len(yhat)):
            	boxes += decode_netout(yhat[i][0], anchors[i], class_threshold,nms_threshold, input_h, input_w)
            correct_yolo_boxes(boxes, image_h, image_w, input_h, input_w)
            do_nms(boxes, 0.5)
            draw_boxes(org_image, boxes, labels, class_threshold)
            cv2.imshow("fens", org_image)
            #cv2.imshow("crop", crop)

            #keys = key_check()

            #output = keys_to_output(keys)
            #training_data.append([screen/255,output])
            #last_time = time.time()


            #if len(training_data) % 250 == 0:
            #    print(len(training_data))

            #    if len(training_data) == 2500:
            #        np.save(file_name,training_data)
            #        print('SAVED')
            #        training_data = []
            #        starting_value += 1
            #        file_name = 'D:/Projects/self_driving_car/Training_data/training_data_final-{}.npy'.format(starting_value)

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

main()
