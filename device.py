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

devices= tf.python.client.device_lib.list_local_devices()
print(devices)
