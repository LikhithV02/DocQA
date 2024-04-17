import numpy as np
import time
from tensorflow.keras.preprocessing import image
# from tensorflow.keras.preprocessing.image import ImageDataGenerator
import tensorflow as tf

# with tf.device('/cpu:0'):
# Load the saved model
model = tf.keras.models.load_model('./best_resnet152_model.h5')

class_names = {0: '1099_Div', 1: '1099_Int', 2: 'Non_Form', 3: 'w_2', 4: 'w_3'}
# print(class_names)

# Load and preprocess the image
# img_path = '/app/filled_form_1.jpg'
def predict(pil_img):
    # Convert the PIL image to a NumPy array
    img_array = image.img_to_array(pil_img)
    img_array = np.expand_dims(img_array, axis=0)
    img_array /= 255.0  # Rescale pixel values

    # Predict the class
    start_time = time.time()
    predictions = model.predict(img_array)
    end_time = time.time()
    predicted_class_index = np.argmax(predictions, axis=1)[0]

    # Get the predicted class name
    predicted_class_name = class_names[predicted_class_index]
    print("Predicted class:", predicted_class_name)
    # print("Execution time: ", end_time - start_time)
    return predicted_class_name