# import python script to check
from main import main
from statistics import mean
import time
import sys

# Images type
imageType = 'MultiFace'
# Image PTAH
imagePath = '../public/images/' + imageType + '/'
# choose alg, 'ViolaJones' or 'CNN'
detectAlg = 'CNN'
# show detection results
show = True
# var for times
times = []

# open results file
f = open('test.txt', 'w')
if not f:
    raise IOError("Can't open file.")
# change stdout to file
original_stdout = sys.stdout
sys.stdout = f

# the test
def test():
    print(f"***Testing {detectAlg} algorithm with {imageType} images***\n")

    for i in range(10):
        imageDir = imagePath + f"{i + 1}" + '.jpg'
        test = {'DetectionAlg': detectAlg, 'imageDir': imageDir, 'Show': show}
        t = time.time()
        faces = main(test)
        t2 = time.time() - t
        times.append(t2)
        print(f"Picture num {i + 1} found {faces} faces in {round(t2, 2)} seconds.")

    print(f"\nAverage time is: {round(mean(times), 2)}")

def endOfTest(f):
    # closing file, change back stdout and print results
    sys.stdout = original_stdout
    f.close()

    f = open('test.txt', 'r')
    print(f.read())
    f.close()

test()
endOfTest(f)