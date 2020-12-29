from matplotlib import pyplot
from matplotlib.patches import Rectangle
from cv2 import imshow
from cv2 import rectangle
from cv2 import waitKey
from cv2 import destroyAllWindows


# draw an image with detected objects
def draw_image_for_deep_learning(imageDir, result_list, detectionAlg):
    # load the image
    data = pyplot.imread(imageDir)
    # plot the image
    pyplot.imshow(data)
    # get the context for drawing boxes
    ax = pyplot.gca()

    # plot each box
    for result in result_list:
        print(result)
        # get coordinates
        x, y, width, height = result['box']
        # create the shape
        rect = Rectangle((x, y), width, height, fill=False, color='red')
        # draw the box
        ax.add_patch(rect)
    # show the plot
    pyplot.show()


def draw_image_for_haar_cascade(imageDir, result_list):
    for box in result_list:
        print(box)
        # extract
        x, y, width, height = box
        x2, y2 = x + width, y + height
        # draw a rectangle over the pixels
        rectangle(imageDir, (x, y), (x2, y2), (0, 0, 255), 1)

    # show the image
    imshow('face detection', imageDir)
    # pyplot.show()
    # keep the window open until we press a key
    waitKey(0)
    # close the window
    destroyAllWindows()
