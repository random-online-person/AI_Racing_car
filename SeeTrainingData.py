import cv2
import numpy as np
import pandas as pd

#training_data = np.load("D:/Projects/self_driving_car/Save_data/training_data-1.npy")
training_data = np.load("D:/Projects/self_driving_car/Final_data/training_data_9_final-26.npy")
print(len(training_data))
#df = pd.DataFrame(training_data)
#print(df.describe())
print(training_data[0][0].shape)
print(training_data[0][1])
print(training_data[100][0])
print(training_data[0][1])
'''
for i in range(len(training_data)):
    cv2.imshow("fens", training_data[i][0])
    print(training_data[i][1])
    if cv2.waitKey(25) & 0xFF == ord('q'):
        cv2.destroyAllWindows()
'''
#for i in training_data:
#    print(i[0])
