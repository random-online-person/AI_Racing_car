import numpy as np
import pandas as pd

file_name = 'D:/Projects/self_driving_car/Training_data/output-probs-normal-{}.npy'.format(4)
data = np.load(file_name)

df = pd.DataFrame(data)
print(df.describe())
