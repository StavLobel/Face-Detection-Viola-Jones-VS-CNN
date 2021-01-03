# import libraries
import cProfile
import pstats

# import python script to check
import main

# func for checking performance of a python script
def perfCheck():
    # perform the performance check
    toCheck = 'main.main()'
    saveTo = 'stats.txt'
    cProfile.run(toCheck, saveTo)

    p = pstats.Stats(saveTo)
    p.sort_stats('cumulative').print_stats(10)

perfCheck()