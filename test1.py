import eval7
# https://pypi.org/project/eval7/
from pprint import pprint
import sys
sys.path.insert(0, ".")
sys.path.insert(0, ".libs")
from pokereval import PokerEval
pokereval = PokerEval()

deck = eval7.Deck()
deck.shuffle()
hand = deck.deal(7)

pprint(hand)

hr = eval7.HandRange("AQs+, 0.4(AsKs)")
# pprint(hr.hands)
# [((Card("Ac"), Card("Qc")), 1.0),
#  ((Card("Ad"), Card("Qd")), 1.0),
#  ((Card("Ah"), Card("Qh")), 1.0),
#  ((Card("As"), Card("Qs")), 1.0),
#  ((Card("Ac"), Card("Kc")), 1.0),
#  ((Card("Ad"), Card("Kd")), 1.0),
#  ((Card("Ah"), Card("Kh")), 1.0),
#  ((Card("As"), Card("Ks")), 1.0),
#  ((Card("As"), Card("Ks")), 0.4)]

hr1 = eval7.HandRange("AJ+, ATs, KQ+, 33-JJ, 0.8(QQ+, KJs)")
# pprint(len(hr1))
scoop=total=tie=0
board = ['7h', '6h', '6c', '__', '__']
hr2 = eval7.HandRange("AJ+, ATs, KQ+, 33-JJ, 0.8(QQ+, KJs)")

#hr2 = eval7.HandRange("89s")
for i in range(len(hr2)):
    pockets = [str(hr2.hands[i][0][0]), str(hr2.hands[i][0][1])]
    #pprint(pockets)   eg. ['As', 'Ah']
    result = pokereval.poker_eval(game='holdem', pockets=[pockets, ["__", "__"]], board=board)
    #pprint(result['eval'][0]['scoop'])
    #pprint(result['info'][0])
    scoop = scoop + result['eval'][0]['scoop']
    tie = tie + result['eval'][0]['tiehi']
    total = total + result['info'][0]
pprint((scoop+tie*1.0/2)*1.0/total)


# pprint(hr2.hands)
# [((Card("Ac"), Card("Jd")), 1.0),
#  ((Card("Ac"), Card("Jh")), 1.0),
#  ((Card("Ac"), Card("Js")), 1.0),
#  ((Card("Ad"), Card("Jc")), 1.0),
#  ((Card("Ad"), Card("Jh")), 1.0),
#  ((Card("Ad"), Card("Js")), 1.0),
#  ((Card("Ah"), Card("Jc")), 1.0),
#  ((Card("Ah"), Card("Jd")), 1.0),
#  ((Card("Ah"), Card("Js")), 1.0),
#  ((Card("As"), Card("Jc")), 1.0),
#  ((Card("As"), Card("Jd")), 1.0),
#  ((Card("As"), Card("Jh")), 1.0),
#  ((Card("Ac"), Card("Jc")), 1.0),
#  ((Card("Ad"), Card("Jd")), 1.0),
#  ((Card("Ah"), Card("Jh")), 1.0),
#  ((Card("As"), Card("Js")), 1.0)]


board = [ 'Ks', 'Jd', '7s', '4d', 'Js' ]
hand = [ '2d', '6c', 'Ac', '5c' ]
best_hand = pokereval.best_hand("low", hand, board)
print "6/ low hand from %s / %s = %s" % ( hand, board, pokereval.best("low", hand, board) )
print "best low hand from %s / %s = (%s) %s " % (hand, board, best_hand[0], [ pokereval.card2string(i) for i in best_hand[1:] ])

result = pokereval.poker_eval(game='holdem', pockets = [['As','Kd'], ['2h','2c']], iterations=10000, board=['7h', '6h', '6c', '__', '__'])
pprint(result)

# So As, Kd:
# - wins - 3657 times,
# - lose - 6244 times,
# - tie - 99 times.
#
# And 2h, 2c:
# - win - 6244 times,
# - lose - 3657 times,
# - tie - 99 times.

# {'eval': [{'ev': 371,
#            'losehi': 6237,
#            'loselo': 0,
#            'scoop': 3657,
#            'tiehi': 106,
#            'tielo': 0,
#            'winhi': 3657,
#            'winlo': 0},
#           {'ev': 629,
#            'losehi': 3657,
#            'loselo': 0,
#            'scoop': 6237,
#            'tiehi': 106,
#            'tielo': 0,
#            'winhi': 6237,
#            'winlo': 0}],
#  'info': (10000, 0, 1)}

result = pokereval.poker_eval(game='holdem', pockets = [['As','Kd'], ['2h','2c']], board=['7h', '6h', '6c', '__', '__'])
pprint(result)

# {'eval': [{'ev': 373,
#            'losehi': 616,
#            'loselo': 0,
#            'scoop': 365,
#            'tiehi': 9,
#            'tielo': 0,
#            'winhi': 365,
#            'winlo': 0},
#           {'ev': 626,
#            'losehi': 365,
#            'loselo': 0,
#            'scoop': 616,
#            'tiehi': 9,
#            'tielo': 0,
#            'winhi': 616,
#            'winlo': 0}],
#  'info': (990, 0, 1)}
