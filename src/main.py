# import Algo's
import DeepLearning
import HaarCascade
import RectanglesCreator
from matplotlib import pyplot

# Image PTAH
imagePath = '../public/images/'
imageDir = imagePath + 'test2.jpg'


def main(detectionalg=None):
    img = pyplot.imread(imageDir)

    if detectionalg == 'Haar':
        faces = HaarCascade.haar_cascade(img)

    elif detectionalg == 'DeepLearn':
        faces = (face['box'] for face in DeepLearning.detectFaces(img))
    else:
        raise IOError("Detection method does not specified.")

    # print bounding box for each detected face
    RectanglesCreator.draw_image(imageDir, faces)


if __name__ == '__main__':
    main()  # Haar or DeepLearn
