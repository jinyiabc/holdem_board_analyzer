import eval7
from pprint import pprint
import sys
import re
sys.path.insert(0, ".")
sys.path.insert(0, ".libs")
from pokereval import PokerEval
pokereval = PokerEval()
from multiprocessing import freeze_support
from multiprocessing import Pool



def operation():
    with open("./hr/test1.log", "r") as ins:
        hr=[]
        for line in ins:
            if len(line.split()) != 0:
                hr.append(line)
    hr_list=[]
    for i in range(len(hr)):
        refined_hr = refine_hr(hr[i])
        hr_list.append([refined_hr])
    return hr_list

def refine_hr(raw):
    '''
    Refine the raw Range
    eg. 77o => 77
        ' ' => ','
    '''
    refined_range = re.sub('(?<=[A-Za-z0-9]{2})o','',raw)  # 22o -> 22
    refined_range = re.sub('\s+',',',refined_range)
    string = str(refined_range[:-1])
    hr = eval7.HandRange(string)
    return hr


def main():
    # hr1 3-bet for value
    # hr2 3-bet for lesser value
    # hr3 for call
    hr1 = eval7.HandRange("TT+, AQ+, KQ+")
    hr2 = eval7.HandRange("77+, A9+, KT+, QT+, JT, T9s, 98s, 87s, 76s, 65s")
    hr3 = eval7.HandRange("22+, A7o+, KT+, QT+, JT, T9, 98s, 87s, 76s, 65s, A2s+, K9s, K8s, Q9s, Q8s, \
    64s, 75s, 86s, 97s, T8s, J9s")

    hr_list = operation()
    for i in range(len(hr_list)):
        pprint(hr_list[i][0].hands)


if __name__ == "__main__":
    freeze_support()   # required to use multiprocessing
    main()
