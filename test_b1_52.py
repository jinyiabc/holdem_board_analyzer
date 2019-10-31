import eval7
# https://pypi.org/project/eval7/
from pprint import pprint
import sys
import datetime
sys.path.insert(0, ".")
sys.path.insert(0, ".libs")
from pokereval import PokerEval
from tqdm import tqdm
pokereval = PokerEval()

# hr1 3-bet for value
# hr2 3-bet for lesser value
# hr3 for call

hr1 = eval7.HandRange("TT+, AQ+, KQ+")
hr2 = eval7.HandRange("77+, A9+, KT+, QT+, JT, T9s, 98s, 87s, 76s, 65s")
hr3 = eval7.HandRange("22+, A7o+, KT+, QT+, JT, T9, 98s, 87s, 76s, 65s, A2s+, K9s, K8s, Q9s, Q8s, \
64s, 75s, 86s, 97s, T8s, J9s")

rank1 = ["2h","3h","4h","5h","6h","7h","8h","9h","Th","Jh","Qh","Kh","Ah"]
rank2 = ["2d","3d","4d","5d","6d","7d","8d","9d","Td","Jd","Qd","Kd","Ad"]
rank3 = ["2c","3c","4c","5c","6c","7c","8c","9c","Tc","Jc","Qc","Kc","Ac"]
rank4 = ["2s","3s","4s","5s","6s","7s","8s","9s","Ts","Js","Qs","Ks","As"]

hr = eval7.HandRange("AsKs")
# hand vs hand 0.29s
# hr = hr1
# board = [b1, b2, b3, '__', '__']
scoop=total=tie=ev=0

# XXX rainbow repeat
#t1 = 0
t = datetime.datetime.now()
for b1 in tqdm(range(52)):
    # for b2 in range(len(rank2)):
    #     for b3 in range(len(rank3)):
    board = [b1, '__', '__', '__', '__']
    #pprint(board)
    #t1+=1
    pockets = [50, 51]
    test = [50, 51, 39, 40]
    test.extend(board)
    #pprint(pockets) test_eval5.py  eg. ['As', 'Ah']
    if len(test) != len(set(test))+3:
        print("err:There is duplicated card in pockets for %s" % test)
        continue
    result = pokereval.poker_eval(game='holdem', pockets=[pockets, ["2s", "3s"]], board=board)
    ev = ev + result['eval'][0]['ev']
    # pprint(result['eval'][0]['ev'])
    scoop = scoop + result['eval'][0]['scoop']
    tie = tie + result['eval'][0]['tiehi']
    total = total + result['info'][0]
    print(result['info'][0])

print("Equity: %18.9f " % ((scoop+tie*1.0/2)*1.0/total))
print("EV: %18.9f " % (ev*1.0/52))
print("total game: %d" % total)  # 48 * 178365 = 8561520
t1 = datetime.datetime.now()
print("Time elapsed: %s" % (t1-t))
