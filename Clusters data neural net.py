import tensorflow as tf
from tensorflow import keras
import pandas as pd
import numpy as np

train_df = pd.read_csv(
    'E:/MyCodes/KeithG/neural-nets-master/examples/clusters/data/train.csv')
color_dict = {'red': 0, 'blue': 1, 'green': 2,
              'teal': 3, 'orange': 4, 'purple': 5}
train_df['color'] = train_df.color.apply(lambda x: color_dict[x])
np.random.shuffle(train_df.values)

print(train_df.head())

model = keras.Sequential([keras.layers.Dense(32, input_shape=(2,), activation='relu'),
                          keras.layers.Dense(32, activation='relu'),
                          keras.layers.Dense(6, activation='sigmoid')])

model.compile(optimizer='adam',
              loss=keras.losses.SparseCategoricalCrossentropy(
                  from_logits=True),
              metrics=['accuracy'])

x = np.column_stack((train_df.x.values, train_df.y.values))

model.fit(x, train_df.color.values, batch_size=10, epochs=10)

test_df = pd.read_csv(
    'E:/MyCodes/KeithG/neural-nets-master/examples/clusters/data/test.csv')
test_df['color'] = test_df.color.apply(lambda x: color_dict[x])
test_x = np.column_stack((test_df.x.values, test_df.y.values))
print("Evaluation")
model.evaluate(test_x, test_df.color.values)
print(np.round(model.predict(np.array([[0, 3]]))))
