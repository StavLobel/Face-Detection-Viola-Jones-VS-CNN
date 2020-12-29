# import Algo's
import DeepLearning, HaarCascade, RectanglesCreator
from matplotlib import pyplot

# Image PTAH
imageDir = '../public/images/test3.png'

# choose detection algo
detectionAlg = 'Haar'  # Haar or DeepLearn


# Should i create a switch case?!
def printerSwitch(img, imgdir, result_list, Algorithm):
    RectanglesCreator.draw_image_for_haar_cascade(img, result_list) if detectionAlg == 'Haar' \
        else RectanglesCreator.draw_image_for_deep_learning(imgdir, result_list, Algorithm)


def main():
    img = pyplot.imread(imageDir)
    print('Image vectors:\n', img)
    if detectionAlg == 'Haar':
        haar_face = HaarCascade.haar_cascade(img)

        # # print bounding box for each detected face
        # RectanglesCreator.draw_image_with_boxes(filename, res)
        printerSwitch(None, imageDir, haar_face, None)

    elif detectionAlg == 'DeepLearn':
        deep_faces = DeepLearning.detectFaces(img)

        # # print bounding box for each detected face
        # RectanglesCreator.draw_image_with_boxes(filename, faces)
        printerSwitch(None, imageDir, deep_faces, detectionAlg)


if __name__ == '__main__':
    main()
