import tensorflow as tf
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D
from tensorflow.keras.layers import Activation, Dropout, Flatten, Dense
from tensorflow.keras.optimizers import SGD
import os

# Путь к папке с данными
data_dir = 'images'

# Параметры для предобработки изображений
image_size = (224, 224)
batch_size = 40

# Создание генераторов данных для обучения и валидации
train_datagen = ImageDataGenerator(
    rescale=1.0 / 255.0,
    rotation_range=20,
    width_shift_range=0.2,
    height_shift_range=0.2,
    shear_range=0.2,
    zoom_range=0.2,
    horizontal_flip=True,
    fill_mode='nearest'
)

train_generator = train_datagen.flow_from_directory(
    os.path.join(data_dir, 'train'),
    target_size=image_size,
    batch_size=batch_size,
    class_mode='binary'
)

validation_datagen = ImageDataGenerator(rescale=1.0 / 255.0)

validation_generator = validation_datagen.flow_from_directory(
    os.path.join(data_dir, 'val'),
    target_size=image_size,
    batch_size=batch_size,
    class_mode='binary'
)

# Создание модели
model = Sequential()
model.add(Conv2D(32, (3, 3), input_shape=(224, 224, 3)))
model.add(Activation('relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))

model.add(Conv2D(64, (3, 3)))
model.add(Activation('relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))

model.add(Conv2D(128, (3, 3)))
model.add(Activation('relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))

model.add(Flatten())
model.add(Dense(512))
model.add(Activation('relu'))
model.add(Dense(1))
model.add(Activation('sigmoid'))

# Компиляция модели
model.compile(
    loss='binary_crossentropy',
    optimizer=SGD(lr=0.01, momentum=0.99),
    metrics=['accuracy']
)

# Обучение модели
num_epochs = 20
history = model.fit(
    train_generator,
    steps_per_epoch=len(train_generator),
    epochs=num_epochs,
    validation_data=validation_generator,
    validation_steps=len(validation_generator)
)

# Сохранение модели
model.save('cat_classification_model.h5')

# Классификация нового изображения
from tensorflow.keras.preprocessing import image

def classify_image(image_path):
    img = image.load_img(image_path, target_size=(224, 224))
    x = image.img_to_array(img)
    x = x / 255.0
    x = x.reshape((1, 224, 224, 3))
    pred = model.predict(x)
    print(pred)
    if pred[0][0] > 0.5:
        return 'cat'
    else:
        return 'not cat'

# Пример использования фун       кции classify_image для классификации новых изображений


new_image_path = 'images/dog2.jpg'
predicted_class = classify_image(new_image_path)
print(str(new_image_path), f'Predicted Class: {predicted_class}')

