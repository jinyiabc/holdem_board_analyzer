import eval7
from tqdm import tqdm
import traceback
import sys
from pprint import pprint
sys.path.insert(0, "../")
sys.path.insert(0, "../.libs")
from pokereval import PokerEval
pokereval = PokerEval()
from pprint import pprint
import numpy as np
import operator
from tqdm import tqdm
import datetime

rank = ['A','K','Q','J','T','9','8','7','6','5','4','3','2']

def hand_init():
    init_hand = {}
    for idx1,i in enumerate(rank):
        for idx2,j in enumerate(rank):
            if idx1==idx2:
                hand0 = rank[idx1] + rank[idx2]
                init_hand[hand0]=0
            if idx1<idx2:
                hand1 = rank[idx1] + rank[idx2] + 'o'
                init_hand[hand1]=0
                hand2 = rank[idx1] + rank[idx2] + 's'
                init_hand[hand2]=0
    # print(len(init_hand))
    # pprint(init_hand)
    return init_hand

def listToStringHand(cardList):
    card1=eval7.Card(cardList[0])
    card2=eval7.Card(cardList[1])
    if card1.rank < card2.rank:
        temp=card1
        card1=card2
        card2=temp
    if card1.suit != card2.suit:
        if card1.rank != card2.rank:
            hand = str(card1)[0]+str(card2)[0]+'o'
        else:
            hand = str(card1)[0]+str(card2)[0]
    else:
        hand = str(card1)[0]+str(card2)[0]+'s'
    return hand

def good_hand(hand):
    new_hand = [i for i in hand if hand[i]>=0]
    return new_hand


hand0=hand_init()
list_hands = good_hand(hand0)
rounds=10
# print(len(list_hands))
for round in tqdm(range(rounds)):
    for index in range(len(list_hands)):
    # hand['32o']=-100
        hr = eval7.HandRange(list_hands[index])
        good_hand1 = good_hand(hand0)
        number = 100*len(hr.hands)
        sum=0
        # print(len(good_hand1))
        for iteration in range(number):
            # good_hand1 = good_hand(hand0)
            # pprint(good_hand1)

            deck = eval7.Deck()
            deck.shuffle()
            cards = deck.cards
            # print(list_hands[index])
            # hr = eval7.HandRange(list_hands[index])
            # pprint(hr.hands)  #[((Card("Qc"), Card("7c")), 1.0),
            # pprint(hr.string) #'Q7s'

            select_one = np.random.randint(len(hr.hands))
            remove_card1 = hr.hands[select_one][0][0]
            remove_card2 = hr.hands[select_one][0][1]
            # print(select_one)
            # print(remove_card1,remove_card2)
            cards.remove(remove_card1)
            cards.remove(remove_card2)
            # print(len(cards))
            dealt_cards = cards[:21]
            # print(len(dealt_cards))
            hands = [str(i) for i in dealt_cards]

            hand1=[str(remove_card1),str(remove_card2)]
            r1=[hands[0],hands[1]]
            n = 7
            player=['','','','','','','']
            for i in range(n):
                list1 = [hands[2+2*i],hands[3+2*i]]
                hand = listToStringHand(list1)
                # card1=eval7.Card(hands[2+2*i])
                # card2=eval7.Card(hands[3+2*i])
                # if card1.rank < card2.rank:
                #     temp=card1
                #     card1=card2
                #     card2=temp
                # if card1.suit != card2.suit:
                #     if card1.rank != card2.rank:
                #         hand = str(card1)[0]+str(card2)[0]+'o'
                #     else:
                #         hand = str(card1)[0]+str(card2)[0]
                # else:
                #     hand = str(card1)[0]+str(card2)[0]+'s'


                if hand in good_hand1:
                    player[i] = [hands[2+2*i],hands[3+2*i]]
                # if hand not in good_hand1:
                #     print(hand)
                #     print(good_hand1)

            participation = [i for i in player if i!='']
            pockets = [hand1, r1] + participation
            board = [hands[2*n+2],hands[2*n+3],hands[2*n+4],hands[2*n+5],hands[2*n+6]]
            # pprint(hand1)
            # pprint(hands)
            # pprint(pockets)
            # pprint(board)
            # print(len(good_hand1))

            result = pokereval.poker_eval(game='holdem', pockets=pockets, board=board)
            # pprint(result['eval'])
            m = len(participation)
            pot = m + 2
            winners = [i for i in result['eval'] if int(i['ev'])>0]
            # for index, value in enumerate(result['eval']):
            #     if value['ev']>0:
            #         # print(pockets[index], "wins", pot*1.0/len(winners))
            #         stringHand=listToStringHand(pockets[index])
            #         # print(stringHand)
            #         hand0[stringHand]+=pot*1.0/len(winners)
            #     else:
            #         # print(pockets[index], "lose 1")
            #         stringHand=listToStringHand(pockets[index])
            #         hand0[stringHand]-=1
            # pprint(good_hand(hand0))
            # pprint(len(good_hand(hand0)))

            if  result['eval'][0]['ev']>0:
                sum = sum + pot*1.0/len(winners)-1
            else:
                sum = sum - 1
        if sum>0:
            hand0[list_hands[index]]+=sum*1.0/number
        else:
            hand0[list_hands[index]]+=sum*1.0/number
        # print(list_hands[index],"=",hand0[list_hands[index]])
        # print(list_hands[index])
    # pprint(hand0)
    # pprint(good_hand(hand0))
    # pprint(len(good_hand(hand0)))

rank_hand0 = sorted(hand0.items(), key=operator.itemgetter(1), reverse=True)
pprint(rank_hand0)
pprint(len(good_hand(hand0)))

t1 = datetime.datetime.now()
f=open("guru_fictious_"+str(n+2)+"__"+str(rounds)+"__"+repr(t1.isoformat()[:10])+".txt","a+")
for i in range(len(rank_hand0)):
    f.write("%.4s, %s\n" % (str(rank_hand0[i][0]), str(rank_hand0[i][1])))
f.close()



        # print(len(winners))
        # if(len(winners)>1):
        #     pprint(winners)






















# card1=eval7.Card('9s')
# card2=eval7.Card('Ah')
# if card1.rank < card2.rank:
#     temp=card1
#     card1=card2
#     card2=temp
#
# hand1 = str(card1)+str(card2)
# hr = eval7.HandRange(hand1)
# # pprint(hr.hands[0][0][0])
# # pprint(hr.hands[0][0][1])
# print(hr.hands)         # [((Card("Ah"), Card("9s")), 1.0)]
# hr_string = hr.string
# print(hr_string)        # Ah9s
