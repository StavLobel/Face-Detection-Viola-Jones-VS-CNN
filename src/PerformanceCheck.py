# import libraries
import cProfile
import pstats

# import python script to check
from main import main

# func for checking performance of a python script
def perfCheck():
    # choose alg, 'ViolaJones' or 'CNN'
    detectAlg = 'CNN'
    toCheck = f"main('{detectAlg}')"
    saveTo = 'stats.txt'
    cProfile.run(toCheck, saveTo)

    p = pstats.Stats(saveTo)
    p.sort_stats('cumulative').print_stats(10)

perfCheck()