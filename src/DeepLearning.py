# face detection with mtcnn on a photograph
from mtcnn.mtcnn import MTCNN


def detectFaces(img):
    detector = MTCNN()
    # detect faces in the image
    faces = detector.detect_faces(img)
    return faces
