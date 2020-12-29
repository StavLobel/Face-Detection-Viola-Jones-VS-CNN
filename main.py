# import Algo's
import DeepLearning
import HaarCascade
import RectanglesCreator
# import pyplot
from matplotlib import pyplot

# import file name
filename = 'test3.jpg'

# choose detection algo
detectionAlg = 'Haar'  # Haar or DeepLearn


def main():
    img = pyplot.imread(filename)
    if detectionAlg == 'Haar':
        None
    elif detectionAlg == 'DeepLearn':
        faces = DeepLearning.detectFaces(img)

    RectanglesCreator.draw_image_with_boxes(faces)



if __name__ == '__main__':
    main()
