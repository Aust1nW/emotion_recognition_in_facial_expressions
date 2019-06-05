from keras.preprocessing import image
import os
import matplotlib.pyplot as plt

train_datagen = image.ImageDataGenerator(
    rotation_range=10,
    width_shift_range=0.1,
    height_shift_range=0.1,
    shear_range=0.1,
    zoom_range=0.1,
    horizontal_flip=True,
    fill_mode='nearest')

val_datagen = image.ImageDataGenerator()

dir_path = os.path.dirname(os.path.realpath(__file__))
train_dir = os.path.join(dir_path, 'train')
val_dir = os.path.join(dir_path, 'validation')

train_gen = train_datagen.flow_from_directory(
    train_dir,
    target_size=(44, 44),
    batch_size=32,
    color_mode='grayscale',
    class_mode='categorical')

val_gen = val_datagen.flow_from_directory(
    val_dir,
    target_size=(44, 44),
    batch_size=32,
    color_mode='grayscale',
    class_mode='categorical')
