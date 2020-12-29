# plot photo with detected faces using opencv cascade classifier
import cv2


def haar_cascade(pixels):
    # load the pre-trained model
    classifier = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
    # perform face detection
    faces = classifier.detectMultiScale(pixels)
    return faces
