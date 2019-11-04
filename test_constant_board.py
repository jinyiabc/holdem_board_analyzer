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

hr1 = eval7.HandRange("TT+, AQ+, KQ+")  # 78 combo
hr2 = eval7.HandRange("77+, A9+, KT+, QT+, JT, T9s, 98s, 87s, 76s, 65s")
hr3 = eval7.HandRange("22+, A7o+, KT+, QT+, JT, T9, 98s, 87s, 76s, 65s, A2s+, K9s, K8s, Q9s, Q8s, \
64s, 75s, 86s, 97s, T8s, J9s")

scoop=total=tie=0
board = ['7s', 'Qd', 'Ac', '__', '__']
hr = hr1
op_hr = eval7.HandRange("KK, JJ")

pairs = []
for i in range(len(hr)):
    for j in range(len(op_hr)):
        pairs.append( dict([('me',[str(hr.hands[i][0][0]),str(hr.hands[i][0][1])]),  \
                     ('op',[str(op_hr.hands[j][0][0]),str(op_hr.hands[j][0][1])])
                     ]))

# report = {}

# Constant board
for pair in pairs:
    me = pair['me']
    op = pair['op']
    # op = ['__','__']
    test = []
    test.extend(me)
    test.extend(op)
    test.extend(board)
    matches = [x for x in board if x == '__']
    if len(test) != len(set(test)) + len(matches) - 1 :
        print("err:There is duplicated card in pockets&boards for %s" % test)
        continue
    result = pokereval.poker_eval(game='holdem', pockets=[me, op], board=board)
    name = me[0]+me[1]+op[0]+op[1]
    # scoop1 = result['eval'][0]['scoop']
    # tie1 = result['eval'][0]['tiehi']
    # total1 = result['info'][0]
    # report[name] = (scoop1, tie1, total1)
    scoop = scoop + result['eval'][0]['scoop']
    tie = tie + result['eval'][0]['tiehi']
    total = total + result['info'][0]

print("Equity: %18.9f " % ((scoop+tie*1.0/2)*1.0/total))
print("total game: %s" % total)
print("tie: %s" % tie)
print("scoop: %s" % scoop)
# pprint(report)



# t = datetime.datetime.now()
# result = pokereval.poker_eval(game = "holdem", pockets = [ ["Td", 'Tc'],  ["Ah", "Ac"]], dead = [], board =board)
# print("scoop: %s" % scoop)

# scoop = result['eval'][0]['scoop']
# tie = result['eval'][0]['tiehi']
# total = result['info'][0]
# # t1 = datetime.datetime.now()
# # print (t1-t)
# pprint(result)
# pprint((scoop+tie*1.0/2)*1.0/total)
# print(total)    # 1,712,304 board = xxxxxx
#                 # 990       board = ABCxx  13*13*13*990 = 2,175,030
#                 # 178365    board = Axxxx  13/48 * 178365 = 2,318,745/8,561,520

# hr1 = eval7.HandRange("TT+, AQ+, KQ+")  # 78 combo
# pprint(len(hr1.hands))

# def colorShape(r1,r2,r3,r4,n,m):
#     '''
#     n equals number of board cards.
#     m equals the number of colors displayed in board.
#     r1,r2,r3,r4 represents rank1,rank2,rank3,rank4
#     '''
#     board=[[0,0] for i in range(n)]
#
#
# rb={}
# for idx1,b1 in enumerate(rank1):  #949,104
#     for idx2, b2 in enumerate(rank1):
#         for idx3, b3 in enumerate(rank2):
#             for idx4, b4 in enumerate(rank2):
#                 for idx5, b5 in enumerate(rank3):
#                     if idx1==idx3<idx2<idx4<idx5:  # 715 orderShape = 2+2+1  (C2,5*C2,3/2 - 1*C2,3)*colorShape(6)*C3,4
#                         # pass
#                         rb[(b1+b3+b2+b4+b5)]=384
#
# pprint(rb)
# print(len(rb))












# # XXX rainbow repeat
# #t1 = 0
# t = datetime.datetime.now()
# for b1 in tqdm(range(len(rank1))):
#     for b2 in range(len(rank2)):
#         for b3 in range(len(rank3)):
#             board = [rank1[b1], rank2[b2], rank3[b3], '__', '__']
#             #board = [rank1[b1],'__', '__' , '__', '__']
#             #pprint(board)
#             #t1+=1
#             for i in (range(len(hr))):
#                 pockets = [str(hr.hands[i][0][0]), str(hr.hands[i][0][1])]
#                 #pprint(pockets)   eg. ['As', 'Ah']
#                 test = []
#                 test.extend(pockets)
#                 test.extend(board)
#                 if len(test) != len(set(test))+1:
#                     print("err:There is duplicated card in pockets for %s" % board)
#                     continue
#                 result = pokereval.poker_eval(game='holdem', pockets=[pockets, ["2s", "3s"]], board=board)
#                 # pprint(result['eval'][0]['ev'])
#                 pprint(result['info'][0])
#                 scoop = scoop + result['eval'][0]['scoop']
#                 tie = tie + result['eval'][0]['tiehi']
#                 total = total + result['info'][0]
#
# print("Equity: %18.9f " % ((scoop+tie*1.0/2)*1.0/total))
# print("total game: %s" % total)   # 13*13*13* 990 == 2175030
# t1 = datetime.datetime.now()
# print("Time elapsed: %s" % (t1-t))
