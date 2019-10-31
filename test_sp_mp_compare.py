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
import test_read as readmp
# import a new API to create a thread pool
# from concurrent.futures import ThreadPoolExecutor as PoolExecutor   #real	1m11.866s
from concurrent.futures import ProcessPoolExecutor as PoolExecutor    #real	0m32.562s
import concurrent.futures
# create a thread pool of 4 threads
executor = PoolExecutor(max_workers=4)

mp= readmp.mp

# deck = eval7.Deck()
# deck.shuffle()
# hand = deck.deal(7)
# pprint(hand)

hr1 = eval7.HandRange("TT+, AQ+, KQ+")  # 78 combo
hr2 = eval7.HandRange("77+, A9+, KT+, QT+, JT, T9s, 98s, 87s, 76s, 65s")
hr3 = eval7.HandRange("22+, A7o+, KT+, QT+, JT, T9, 98s, 87s, 76s, 65s, A2s+, K9s, K8s, Q9s, Q8s, \
64s, 75s, 86s, 97s, T8s, J9s")

scoop=total=tie=0
scoop1=total1=tie1=0

board = ['__', '__', '__', '__', '__']
hr = eval7.HandRange("TT+")
op_hr = eval7.HandRange("AA")

pairs = []
for i in range(len(hr)):
    for j in range(len(op_hr)):
        pairs.append( dict([('me',[str(hr.hands[i][0][0]),str(hr.hands[i][0][1])]),  \
                     ('op',[str(op_hr.hands[j][0][0]),str(op_hr.hands[j][0][1])])
                     ]))

report = {}

# Constant board
for pair in pairs:
    me = pair['me']
    op = pair['op']
    test = []
    test.extend(me)
    test.extend(op)
    test.extend(board)
    matches = [x for x in board if x == '__']
    if len(test) != len(set(test)) + len(matches) - 1 :
        print("err:There is duplicated card in pockets&boards for %s" % test)
        continue
    result = pokereval.poker_eval(game='holdem', pockets=[me, op], board=board)

 '''
 Define report dictionary:  {name:(scoop,tie,game)}
 '''
    scoop1 = result['eval'][0]['scoop']
    tie1 = result['eval'][0]['tiehi']
    total1 = result['info'][0]
    name = me[0]+me[1]+op[0]+op[1]
    report[name] = (scoop1,tie1,total1)

    scoop = scoop + result['eval'][0]['scoop']
    tie = tie + result['eval'][0]['tiehi']
    total = total + result['info'][0]

print("Equity: %18.9f " % ((scoop+tie*1.0/2)*1.0/total))
print("total game: %s" % total)
print("tie: %s" % tie)
print("scoop: %s" % scoop)
pprint(report)

scoop_mp = scoop_report = 0
for key in report:
    # if report[key] != mp[key]:
    scoop_mp +=   int(mp[key])
    scoop_report += int(report[key])
    print(key, report[key], mp[key], (int(report[key][0]) -int(mp[key][0])) )
print(scoop_mp, scoop_report)
