from matplotlib import pyplot
from matplotlib.patches import Rectangle
import ntpath


# draw an image with detected objects
def drawImage(imageDir, result_list):
    resDir = '../public/images/results/'
    # load the image
    data = pyplot.imread(imageDir)
    name = resDir + ntpath.basename(imageDir)
    # plot the image
    pyplot.imshow(data)
    # get the context for drawing boxes
    ax = pyplot.gca()

    # plot each box
    for result in result_list:
        # get coordinates
        x, y, width, height = result
        # create the shape
        rect = Rectangle((x, y), width, height, fill=False, color='red')
        # draw the box
        ax.add_patch(rect)
    pyplot.savefig(name)
    # show the plot
    pyplot.show()
