import tensorflow as tf
from tensorflow import keras
import pandas as pd
import numpy as np
import os

from tensorflow.keras import layers
from tensorflow.python.keras.layers.core import Dropout
os.environ["CUDA_VISIBLE_DEVICES"] = "-1"
train_df = pd.read_csv(
    'E:/MyCodes/KeithG/neural-nets-master/examples/complex/data/train.csv')
np.random.shuffle(train_df.values)

print(train_df.head())

model = keras.Sequential([keras.layers.Dense(256, input_shape=(2,), activation='relu'),
                          keras.layers.Dense(256, activation='relu'),
                          keras.layers.Dense(256, activation='relu'),
                          keras.layers.Dense(2, activation='sigmoid')])

model.compile(optimizer='adam',
              loss=keras.losses.SparseCategoricalCrossentropy(
                  from_logits=True),
              metrics=['accuracy'])

x = np.column_stack((train_df.x.values, train_df.y.values))

model.fit(x, train_df.color.values, batch_size=10, epochs=10)

test_df = pd.read_csv(
    'E:/MyCodes/KeithG/neural-nets-master/examples/complex/data/test.csv')
test_x = np.column_stack((test_df.x.values, test_df.y.values))
print("Evaluation")
model.evaluate(test_x, test_df.color.values)
print(np.round(model.predict(np.array([[0, 3]]))))
