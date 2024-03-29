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
import re


rank = ['A','K','Q','J','T','9','8','7','6','5','4','3','2']

def hand_init(init):
    init_hand = {}
    for idx1,i in enumerate(rank):
        for idx2,j in enumerate(rank):
            if idx1==idx2:
                hand0 = rank[idx1] + rank[idx2]
                init_hand[hand0]=init
            if idx1<idx2:
                hand1 = rank[idx1] + rank[idx2] + 'o'
                init_hand[hand1]=init
                hand2 = rank[idx1] + rank[idx2] + 's'
                init_hand[hand2]=init
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

def good_hand(hand, benchmark):
    new_hand = [i for i in hand if hand[i]>=benchmark]
    return new_hand

def handlist(hand):
    new_hand = [i for i in hand]
    return new_hand

def hand_proceed(file):
    with open(file, "r") as ins:
        pos=[]
        for line in ins:
            pos.append(line.split(','))
    # cardStringList1 = [i[0] for i in pos ]
    # hand = [i[0] for i in pos if float(re.sub('\s','',i[1]))>0]
    # hand = percentile(cardStringList1,30)
    hand = {}
    for i in pos:
        hand[i[0]] = float(re.sub('\s','',i[1]))

    return hand


def percentile(cardStringList, n):
    hr=[]
    for i in range(len(cardStringList)):
        hr += eval7.HandRange(cardStringList[i]).hands

    i=len(hr)
    index=np.percentile(np.arange(i), n, interpolation='nearest')
    # print hr[index]
    # print( str(hr[index][0][0]) )
    if str(hr[index][0][0])[1] != str(hr[index][0][1])[1]:
        if str(hr[index][0][0])[0]!= str(hr[index][0][1])[0]:
            hand = str(hr[index][0][0])[0]+str(hr[index][0][1])[0] +'o'
        else:
            hand = str(hr[index][0][0])[0]+str(hr[index][0][1])[0]
    else:
        hand = str(hr[index][0][0])[0]+str(hr[index][0][1])[0] +'s'
    # print(hand)
    new_list=cardStringList[:(cardStringList.index(hand)+1)]
    # print(new_list)
    return new_list

########################################################
hand_preceed = 'proceed'
rounds=150
R1C=1  # Bet structure: Assume raise followed by call.
n = 1  # number of players except hero and bb.
iteration=200 # for each hand range eg. 89O
noise=np.zeros((rounds, 169))
benchmark = 3 # good hand benchmark for investigation.
##########################################################

if hand_preceed == 'proceed' :
    hand0=hand_proceed("./log3/guru_initial_palyers=3_betStruct=1_rounds=20_'2019-11-12T23:55:36'.txt")
    list_hands = good_hand(hand0, benchmark)     # update hands better than benchmark.
    # list_hands = handlist(hand_init(benchmark))  # update all hands

else:
    hand0=hand_init(benchmark)
    list_hands = handlist(hand_init(benchmark))   # update all hands

# pprint(good_hand(hand0))
# pprint(list_hands)


for round in tqdm(range(rounds)):
    report={}
    for index in range(len(list_hands)):
    # hand['32o']=-100
        hr = eval7.HandRange(list_hands[index])
        good_hand1 = good_hand(hand0, benchmark)
        number = iteration*len(hr.hands)
        sum=0
        # pprint(hand0)
        for itr in range(number):
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
            r1=[hands[2*n+5],hands[2*n+6]]
            '''
            For simplicity: Assume BB share good hand with other player.
            '''
            # n = 8
            # bb_play = False
            player=['','','','','','','']
            for i in range(n):
                list1 = [hands[2*i],hands[1+2*i]]
                hand = listToStringHand(list1)
                if hand in good_hand1:
                    player[i] = [hands[2*i],hands[1+2*i]]
                    # if i==0:
                    #     bb_play = True

            participation = [i for i in player if i!='']
            pockets = [hand1, r1] + participation
            board = [hands[2*n],hands[2*n+1],hands[2*n+2],hands[2*n+3],hands[2*n+4]]
            # pprint(hand1)
            # pprint(hands)
            # pprint(pockets)
            # pprint(board)
            # print(len(good_hand1))

            result = pokereval.poker_eval(game='holdem', pockets=pockets, board=board)
            # pprint(result['eval'])
            m = len(participation)
            pot = R1C*(m + 2)
            # if bb_play:
            #     pot = R1C*(m + 1)
            # else:
            #     pot = R1C*(m + 1) + 1   # 1BB from bb as dead money.
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
                sum = sum + pot*1.0/len(winners) - 1*R1C
            else:
                sum = sum - 1*R1C
            # Add diminishing noise factor.
            # print(np.random.uniform(-1,1)/(itr+1))
            # hand0[list_hands[index]]+=sum + 0.1*np.random.uniform(-1,1)/(round*itr+1)
        noise[round][index]= 0.5*np.random.uniform(-1,1)/(round+1)
        hand0[list_hands[index]]+=sum*1.0/number  #+ noise[round][index]
        report[list_hands[index]]= hand0[list_hands[index]] #,noise[round][index]]
        # print(list_hands[index],"=",hand0[list_hands[index]])
        # print(list_hands[index])
    # pprint(hand0)
    # pprint(good_hand(hand0))
    # pprint(len(good_hand(hand0)))
    pprint(report)

hand1={}
for i in list_hands:
    hand1[i] = hand0[i] #/rounds

rank_hand0 = sorted(hand1.items(), key=operator.itemgetter(1), reverse=True)
pprint(rank_hand0)
pprint(len(good_hand(hand0, benchmark)))

t1 = datetime.datetime.now()
f=open("./log3/guru_"+hand_preceed+"_palyers="+str(n+2)+"_"+"betStruct="+str(R1C)+"_"+"rounds="+str(rounds)+"_"+repr(t1.isoformat()[:19])+".txt","a+")
for i in range(len(rank_hand0)):
    f.write("%.4s, %s\n" % (str(rank_hand0[i][0]), str(rank_hand0[i][1])))
f.close()
