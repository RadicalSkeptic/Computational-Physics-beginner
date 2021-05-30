from tensorflow.python.keras.layers.core import Dropout
from tensorflow.python.ops.gen_array_ops import one_hot
import numpy as np
import pandas as pd
from tensorflow import keras
import tensorflow as tf
import os
os.environ["CUDA_VISIBLE_DEVICES"] = "-1"


train_df = pd.read_csv(
    'E:/MyCodes/KeithG/neural-nets-master/examples/clusters_two_categories/data/train.csv')
one_hot_colors = pd.get_dummies(train_df.color).values
one_hot_markers = pd.get_dummies(train_df.marker).values
one_hot_data = np.concatenate((one_hot_colors, one_hot_markers), axis=1)

model = keras.Sequential([keras.layers.Dense(64, input_shape=(2,), activation='relu'),
                          keras.layers.Dropout(.2),
                          keras.layers.Dense(64, activation='relu'),
                          keras.layers.Dropout(.2),
                          keras.layers.Dense(9, activation='sigmoid')])

model.compile(optimizer='adam', loss=keras.losses.BinaryCrossentropy(
    from_logits=False), metrics=['accuracy'])

x = np.column_stack((train_df.x.values, train_df.y.values))
'''np.random.RandomState(seed=42).shuffle(one_hot_data)
np.random.RandomState(seed=42).shuffle(x)'''

model.fit(x, one_hot_data, batch_size=1, epochs=5)

test_df = pd.read_csv(
    'E:/MyCodes/KeithG/neural-nets-master/examples/clusters_two_categories/data/test.csv')
one_hot_colors_test = pd.get_dummies(test_df.color).values
one_hot_markers_test = pd.get_dummies(test_df.marker).values
one_hot_data_test = np.concatenate(
    (one_hot_colors_test, one_hot_markers_test), axis=1)
x_test = np.column_stack((test_df.x.values, test_df.y.values))

print("Evaluation")
model.evaluate(x_test, one_hot_data_test)
print(np.round(model.predict(np.array([[0, 3]]))))
