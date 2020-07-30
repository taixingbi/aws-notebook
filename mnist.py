import tensorflow as tf

gpus = tf.config.experimental.list_physical_devices('GPU')
for gpu in gpus:
    print("Name:", gpu.name, "  Type:", gpu.device_type)
# Name: /physical_device:GPU:0   Type: GPU

mirrored_strategy = tf.distribute.experimental.MultiWorkerMirroredStrategy(
    tf.distribute.experimental.CollectiveCommunication.NCCL)
print(mirrored_strategy)

# cpu
# WARNING:tensorflow:There are non-GPU devices in `tf.distribute.Strategy`, not using nccl allreduce.
# INFO:tensorflow:Using MirroredStrategy with devices ('/job:localhost/replica:0/task:0/device:CPU:0',)
# Number of devices: 1

# gpu1
# INFO:tensorflow:Using MirroredStrategy with devices ('/device:GPU:0',)
# INFO:tensorflow:Single-worker MultiWorkerMirroredStrategy with local_devices = ('/device:GPU:0',), communication = CollectiveCommunication.NCCL
# <tensorflow.python.distribute.collective_all_reduce_strategy.CollectiveAllReduceStrategy object at 0x7fd0606f4198>

import datetime

mnist = tf.keras.datasets.mnist
(x_train, y_train), (x_test, y_test) = mnist.load_data()
x_train, x_test = x_train / 255.0, x_test / 255.0

print(x_train.shape, x_test.shape)

with mirrored_strategy.scope():
    model = tf.keras.models.Sequential([
      tf.keras.layers.Flatten(input_shape=(28, 28)),
      tf.keras.layers.Dense(128, activation='relu'),
      tf.keras.layers.Dropout(0.2),
      tf.keras.layers.Dense(10)
    ])
    
loss_fn = tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True)

model.compile(optimizer='adam',
              loss=loss_fn,
              metrics=['accuracy'])
              
t1 = datetime.datetime.now()
model.fit(x_train, y_train, epochs=5, batch_size=64)
model.evaluate(x_test,  y_test, verbose=2)
print( datetime.datetime.now() - t1 )

# cpu 0:00:20.442683

print("done")
