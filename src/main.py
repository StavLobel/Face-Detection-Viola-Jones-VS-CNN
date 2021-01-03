# import Algo's
import DeepLearning
import HaarCascade
import RectanglesCreator
from matplotlib import pyplot

# Image PTAH
imagePath = '../public/images/'
imageDir = imagePath + 'test2.jpg'

# choose detection algo
detectionAlg = 'DeepLearn'  # Haar or DeepLearn

def main():
    img = pyplot.imread(imageDir)

    if detectionAlg == 'Haar':
        faces = HaarCascade.haar_cascade(img)

    elif detectionAlg == 'DeepLearn':
        faces = (face['box'] for face in DeepLearning.detectFaces(img))
    else:
        raise IOError("Detection method does not specified.")

    # print bounding box for each detected face
    RectanglesCreator.draw_image(imageDir, faces)


if __name__ == '__main__':
    main()
