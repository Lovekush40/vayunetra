import numpy as np
import tensorflow as tf

X = np.array([[120],[130],[140],[150],[160]])
y = np.array([130,140,150,160,170])

model = tf.keras.Sequential([
    tf.keras.layers.Dense(8, activation='relu'),
    tf.keras.layers.Dense(1)
])

model.compile(optimizer='adam', loss='mse')
model.fit(X, y, epochs=200)

model.save("model/tf_model.h5")