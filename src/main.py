# import Algo's
import CNN
import ViolaJones
import RectanglesCreator
from matplotlib import pyplot


def main(param=None):
    # Load Images
    img = pyplot.imread(param['imageDir'])

    if param['DetectionAlg'] == 'ViolaJones':
        faces = ViolaJones.violaJones(img)

    elif param['DetectionAlg'] == 'CNN':
        faces = list(face['box'] for face in CNN.detectCNN(img))
    else:
        raise IOError("Detection method does not specified.")

    if param['Show']:
        # print bounding box for each detected face
        RectanglesCreator.drawImage(param['imageDir'], faces)

    return len(faces)

if __name__ == '__main__':
    main()  # 'ViolaJones' or 'CNN'
