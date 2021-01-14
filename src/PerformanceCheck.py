# import python script to check
from main import main

# import avg function
from statistics import mean
# import time library
import time

# import sys for manipulating output
import sys

# Creat results directory
import os
try:
    os.stat('../public/images/results')
except:
    os.mkdir('../public/images/results')

# ***The test parameters***
# Images DB type
imageType = 'multi_face'
# Images path
imagePath = '../public/images/' + imageType + '/'
# choose alg, 'ViolaJones' or 'CNN'
detectAlg = 'CNN'
# show detection results on screen
show = True
# var for storing times
times = []


# open the results file for writing
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

# closing file, change back stdout and print results
def endOfTest():
    global f
    sys.stdout = original_stdout
    f.close()

    f = open('test.txt', 'r')
    print(f.read())
    f.close()


test()
endOfTest()
