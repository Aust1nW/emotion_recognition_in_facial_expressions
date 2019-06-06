import numpy as np
from keras import backend as K
from keras.preprocessing import image
import os
from keras.applications.vgg16 import VGG16
from keras import layers
import matplotlib.pyplot as plt
import cv2

# TODO LIST
# 1. Separate data into validation data and store that in a validation directory
# 2. Try other model architectures, ResNet and VGG-Face
# 3. Test Heatmap in Jupyter Notebook


def vgg_build_model():
    m = VGG16(weights='imagenet', include_top=False, input_shape=(44, 44, 3))
    m.add(layers.Flatten())
    m.add(layers.Dense(128, activation='relu'))
    m.add(layers.Dropout(0.5))
    m.add(layers.Dense(8, activation='sigmoid'))
    return m


# Set up generators train_gen and val_gen
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

# Build the model and train using train_gen and val_gen
model = vgg_build_model()
model.compile(optimizer='rmsprop', loss='categorical_crossentropy', metrics=['acc'])
history = model.fit_generator(train_gen,
                              steps_per_epoch=100,
                              epochs=20,
                              validation_data=val_gen,
                              validation_steps=500)

# Plot the results
acc = history.history['acc']
val_acc = history.history['val_acc']
loss = history.history['loss']
val_loss = history.history['val_loss']

epochs = range(len(acc))
plt.plot(epochs, acc, 'bo', label='Training acc')
plt.plot(epochs, val_acc, 'b', label='Validation acc')
plt.title('Training and validation accuracy')
plt.legend()

plt.figure()

plt.plot(epochs, loss, 'bo', label='Training loss')
plt.plot(epochs, val_loss, 'b', label='Validation loss')
plt.title('Training and validation loss')
plt.legend()

plt.show()


# Values set to 0 are placeholders
sample_image = 0
preds = model.predict(sample_image)
x = np.argmax(preds[0])
output = model.output[:, 386]

# Start the Heatmap
last_conv_layer = model.get_layer('block5_conv3')
grads = K.gradients(output, last_conv_layer.output)[0]
pooled_grads = K.mean(grads, axis=(0, 1, 2))
iterate = K.function([model.input], [pooled_grads, last_conv_layer.output[0]])
pooled_grads_value, conv_layer_output_value = iterate([sample_image])

for i in range(512):
    conv_layer_output_value[:, :, i] *= pooled_grads_value[i]


# Visualize the heatmap
heatmap = np.mean(conv_layer_output_value, axis=-1)
heatmap = np.maximum(heatmap, 0)
heatmap /= np.max(heatmap)
plt.matshow(heatmap)
plt.show()


# Start layering the heatmap on top of the original image
# The local path to our target image
img_path = './test_dat/7b.jpg'
img = image.load_img(img_path, target_size=(44, 44))

# `x` is a float32 Numpy array of shape (44, 44, 3)
x = image.img_to_array(img)


x = np.expand_dims(x, axis=0)

preds = model.predict(x)

img = cv2.imread(img_path)

# We resize the heatmap to have the same size as the original image
heatmap = cv2.resize(heatmap, (img.shape[1], img.shape[0]))

# We convert the heatmap to RGB
heatmap = np.uint8(255 * heatmap)

# We apply the heatmap to the original image
heatmap = cv2.applyColorMap(heatmap, cv2.COLORMAP_JET)

# 0.4 here is a heatmap intensity factor
superimposed_img = heatmap * 0.4 + img

# Save the image to disk
cv2.imwrite('./heatmap/heatmap_output.jpg', superimposed_img)
