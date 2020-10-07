from YOLO_V3 import make_yolov3_model, WeightReader
from keras.models import Model

model = make_yolov3_model()

weight_reader = WeightReader('D:/Projects/self_driving_car/Save_model/yolov3.weights')

weight_reader.load_weights(model)

model.save('D:/Projects/self_driving_car/Save_model/model.h5')
