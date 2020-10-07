import numpy as np
from Model_arch import alexnet
from random import shuffle

WIDTH = 480
HEIGHT = 160
LR = 1e-3
EPOCHS = 40
MODEL_NAME = 'D:/Projects/self_driving_car/Save_model/no_{}name-{}-epochs-{}.model'.format(LR, 'final_4',EPOCHS)

model = alexnet(WIDTH, HEIGHT, LR)
#model.load('D:/Projects/self_driving_car/Save_model/no_{}name-{}-epochs-{}.model'.format(LR, 'final_4',EPOCHS))

for k in range(EPOCHS):
    for i in range(1, 21):
        #file_names.append('C:/somthing_less/training_data_final-{}.npy'.format(i))
        temp = np.load('D:/Projects/self_driving_car/Final_data/training_data_9_final-{}.npy'.format(i))

        shuffle(temp)

        X = []
        Y = []

        test_x = []
        test_y = []

        train = temp[:-100]
        test = temp[-100:]

        shuffle(train)
        shuffle(test)

        for i in train:
            X.append(np.array(i[0]))
            Y.append(np.array(i[1]))

        for i in test:
            test_x.append(np.array(i[0]))
            test_y.append(np.array(i[1]))

        X = np.array(X).reshape(-1,WIDTH,HEIGHT,1)
        Y = np.array(Y)
        test_x = np.array(test_x).reshape(-1,WIDTH,HEIGHT,1)
        test_y = np.array(test_y)



            #X = np.array([i[0] for i in train]).reshape(-1,WIDTH,HEIGHT,1)
            #Y = [i[1] for i in train]

            #test_x = np.array([i[0] for i in test]).reshape(-1,WIDTH,HEIGHT,1)
            #test_y = [i[1] for i in test]

        model.fit({'input': X}, {'targets': Y}, n_epoch=2, validation_set=({'input': test_x}, {'targets': test_y}),
                    snapshot_step=2500, show_metric=True)

        model.save(MODEL_NAME)

model.save(MODEL_NAME)
