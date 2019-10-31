import sys
sys.path.insert(0, ".")
sys.path.insert(0, ".libs")
from pokereval import PokerEval

pokereval = PokerEval()

# print ""
# board = [ 'Jc', '4c', '3c', '__', '__' ]
# hand = [ '2c', 'Ac', '5h', '9d' ]
# best_hand = pokereval.best_hand("hi", hand, board)

# (['Ad', 'Qh'], ['3h', '8d', 'Tc'])

board = ['As', '8d', 'Tc']    #  >=3
hand = ['Ad', 'Qh','Ac', '5c','Tc', '8d']  # >=4
hand = ['Ad', 'Qh','Ac', '5c','Tc']  # >=4

'''
if board != None:
    board>=3, hand=4,6,8
if board == None:
    hand>=5
'''

best_hand = pokereval.best_hand("hi", hand)
print(best_hand)
# print "hi hand from %s / %s = %s" % ( hand, board, pokereval.best("hi", hand, board) )
# print "best hi hand from %s / %s = (%s) %s " % (hand, board, best_hand[0], pokereval.card2string(best_hand[1:]))



'''
A list is returned. The first element is the numerical value
of the hand (better hands have higher values if "side" is "hi" and
lower values if "side" is "low"). The second element is a list whose
first element is the strength of the hand among the following:

example:
print "hi hand from %s / %s = %s" % ( hand, board, pokereval.best("hi", hand, board) )
print "best hi hand from %s / %s = (%s) %s " % (hand, board, best_hand[0], pokereval.card2string(best_hand[1:]))
output:
hi hand from ['2c', 'Ac', '5h', '9d'] / ['Jc', '4c', '3c', '5c', '9c'] = [134414336, ['StFlush', 29, 28, 27, 26, 38]]
best hi hand from ['2c', 'Ac', '5h', '9d'] / ['Jc', '4c', '3c', '5c', '9c'] = (StFlush) ['5c', '4c', '3c', '2c', 'Ac']

Nothing (only if "side" equals "low")
NoPair
OnePair
TwoPair
Trips
Straight
Flush
FlHouse
Quads
StFlush
'''
