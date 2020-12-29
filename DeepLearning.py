# face detection with mtcnn on a photograph
from mtcnn.mtcnn import MTCNN
from matplotlib import pyplot

def detectFaces(img):
    detector = MTCNN()
    # detect faces in the image
    faces = detector.detect_faces(img)
    return faces
