import cv2
from PIL import Image
import keras.utils as image
import numpy as np
from keras.models import load_model

# load model
model = load_model("kid_dose/ml_models/EmotionDModel/EmotionDModel.h5")

# face detection
face_haar_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')


def predict_emotion(image_file):
    # Read the image file as a numpy array
    np_image = np.frombuffer(image_file.read(), np.uint8)
    test_img = cv2.imdecode(np_image, cv2.IMREAD_COLOR)

    # Convert the image to grayscale
    gray_img = cv2.cvtColor(test_img, cv2.COLOR_BGR2RGB)

    faces_detected = face_haar_cascade.detectMultiScale(gray_img, 1.32, 5)

    predicted_emotion = ''

    for (x, y, w, h) in faces_detected:
        roi_gray = gray_img[y:y + w, x:x + h]  # cropping region of interest i.e. face area from  image
        roi_gray = cv2.resize(roi_gray, (224, 224))
        img_pixels = image.img_to_array(roi_gray)
        img_pixels = np.expand_dims(img_pixels, axis=0)
        img_pixels /= 255

        predictions = model.predict(img_pixels)

        # find max indexed array
        max_index = np.argmax(predictions[0])

        emotions = ('angry', 'disgust', 'fear', 'happy', 'sad', 'surprise', 'neutral')

        predicted_emotion = emotions[max_index]

        # add predicted emotion text to image
        cv2.putText(test_img, predicted_emotion, (int(x), int(y)), cv2.FONT_HERSHEY_DUPLEX, 1, (255, 165, 0), 2)

    # resize image
    # resized_img = cv2.resize(test_img, (1000, 700))

    return predicted_emotion, faces_detected