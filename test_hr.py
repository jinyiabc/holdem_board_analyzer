import eval7
from pprint import pprint
import sys
sys.path.insert(0, ".")
sys.path.insert(0, ".libs")
from pokereval import PokerEval
pokereval = PokerEval()
from multiprocessing import freeze_support
from multiprocessing import Pool



def operation(hand):
    f=open("guru99.txt","a+")
    #print hand[0][0], hand[0][1]
    f.write("This is line %s\r\n" % hand[0][0])
    f.close()

'''Define function to run mutiple processors and pool the results together'''
def run_multiprocessing(func, i, n_processors):
    pool = Pool(processes=n_processors)
    return pool.map(func, i)


def main():
    # hr1 3-bet for value
    # hr2 3-bet for lesser value
    # hr3 for call
    hr1 = eval7.HandRange("TT+, AQ+, KQ+")
    hr2 = eval7.HandRange("77+, A9+, KT+, QT+, JT, T9s, 98s, 87s, 76s, 65s")
    hr3 = eval7.HandRange("22+, A7o+, KT+, QT+, JT, T9, 98s, 87s, 76s, 65s, A2s+, K9s, K8s, Q9s, Q8s, \
    64s, 75s, 86s, 97s, T8s, J9s")
    hands = hr1.hands

    '''
    pass the task function, followed by the parameters to processors
    '''
    out = run_multiprocessing(operation, hands, 6)


if __name__ == "__main__":
    freeze_support()   # required to use multiprocessing
    main()
