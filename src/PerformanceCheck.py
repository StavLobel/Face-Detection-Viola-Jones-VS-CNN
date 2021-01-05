# import libraries
import cProfile
import pstats

# import python script to check
from main import main

# func for checking performance of a python script
def perfCheck():
    # choose alg, 'ViolaJones' or 'CNN'
    detectAlg = 'ViolaJones'

    # The performance check
    toCheck = f"main('{detectAlg}')"
    saveTo = 'stats.txt'
    cProfile.run(toCheck, saveTo)

    # Printing the results
    p = pstats.Stats(saveTo)
    p.sort_stats('cumulative').print_stats(10)

perfCheck()