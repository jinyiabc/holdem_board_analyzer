import eval7
# https://pypi.org/project/eval7/
from pprint import pprint
import sys
import datetime
sys.path.insert(0, ".")
sys.path.insert(0, ".libs")
from pokereval import PokerEval
pokereval = PokerEval()
from tqdm import tqdm
# import a new API to create a thread pool
# from concurrent.futures import ThreadPoolExecutor as PoolExecutor   #real	1m11.866s
from concurrent.futures import ProcessPoolExecutor as PoolExecutor    #real	0m32.562s
import concurrent.futures
# create a thread pool of 4 threads
executor = PoolExecutor(max_workers=4)


# deck = eval7.Deck()
# deck.shuffle()
# hand = deck.deal(7)
# pprint(hand)

hr1 = eval7.HandRange("TT+, AQ+, KQ+")  # 78 combo
hr2 = eval7.HandRange("77+, A9+, KT+, QT+, JT, T9s, 98s, 87s, 76s, 65s")
hr3 = eval7.HandRange("22+, A7o+, KT+, QT+, JT, T9, 98s, 87s, 76s, 65s, A2s+, K9s, K8s, Q9s, Q8s, \
64s, 75s, 86s, 97s, T8s, J9s")

scoop=total=tie=0
board = ['__', '__', '__', '__', '__']
hr = hr1
op_hr = eval7.HandRange("AA")

pairs = []
for i in range(len(hr)):
    for j in range(len(op_hr)):
        pairs.append( dict([('me',[str(hr.hands[i][0][0]),str(hr.hands[i][0][1])]),  \
                     ('op',[str(op_hr.hands[j][0][0]),str(op_hr.hands[j][0][1])])
                     ]))

# print(len(pairs))  # 78 * 6 = 468

# Multi-Processing
def try_my_operation(pair):
        try:
            me = pair['me']
            op = pair['op']
            #pprint(pair)
            f=open("guru99.txt","a+")
            # pprint(hand)
            test = []
            test.extend(me)
            test.extend(op)
            test.extend(board)
            matches = [x for x in board if x == '__']
            if len(test) != len(set(test)) + len(matches) - 1 :
                #f.write("err:There is duplicated card in pockets&boards for %s" % test)
                f.close()
            result = pokereval.poker_eval(game='holdem', pockets=[me, op], board=board)
            #pprint(result)
            # # pprint(result['info'][0])
            scoop = result['eval'][0]['scoop']
            tie = result['eval'][0]['tiehi']
            total = result['info'][0]
            name = me[0]+me[1]+op[0]+op[1]

            # f=open("guru99.txt","a+")
            #print hand[0][0], hand[0][1]
            t1 = datetime.datetime.now()
            f.write("%s %s %s %s\n " %  (name,scoop,tie,total))
            f.close()

        except Exception as e:
            print('Caught exception in worker thread %s' % pair)

            # This prints the type, value, and stack trace of the
            # current exception being handled.
            # traceback.print_exc()
            # print()

            #raise e

futures = [executor.submit(try_my_operation, pair) for pair in pairs]
concurrent.futures.wait(futures)
