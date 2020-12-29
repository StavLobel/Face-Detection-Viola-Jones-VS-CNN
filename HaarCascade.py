# plot photo with detected faces using opencv cascade classifier
import cv2
from matplotlib import pyplot
from matplotlib.patches import Rectangle

def draw_image_with_boxes(filename, result_list):
	# load the image
	data = pyplot.imread(filename)
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
	# show the plot
	pyplot.show()

# load the pre-trained model
classifier =\
	cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
# perform face detection
results = classifier.detectMultiScale(pixels)

# print bounding box for each detected face
draw_image_with_boxes(filename,results)

