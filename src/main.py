# import Algo's
import CNN
import ViolaJones
import RectanglesCreator
from matplotlib import pyplot

# Image PTAH
imagePath = '../public/images/'
imageDir = imagePath + 'test2.jpg'


def main(detectionalg=None):
    img = pyplot.imread(imageDir)

    if detectionalg == 'ViolaJones':
        faces = ViolaJones.violaJones(img)

    elif detectionalg == 'CNN':
        faces = (face['box'] for face in CNN.detectCNN(img))
    else:
        raise IOError("Detection method does not specified.")

    # print bounding box for each detected face
    RectanglesCreator.draw_image(imageDir, faces)


if __name__ == '__main__':
    main()  # 'ViolaJones' or 'CNN'
