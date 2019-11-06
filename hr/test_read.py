from pprint import pprint
import eval7
import re
import sys
# import test_constant_board as const
'''
usage:
python test_read.py <number>
number: r in sim function
'''
def Diff(li1, li2):
    return (list(set(li1) - set(li2)))

def refine_hr(raw):
    '''
    Refine the raw Range
    eg. 77o => 77
        ' ' => ','
    '''
    refined_range = re.sub('(?<=[A-Za-z0-9]{2})o','',raw)  # 22o -> 22
    refined_range = re.sub('\s+',',',refined_range)
    string = str(refined_range[:-1])
    # hr = eval7.hr_sim(string)
    return string

def main():
    with open("test_an=0.5_bl=0.5_lim=1_r=" + sys.argv[1] + "_liv=1_nr=5_pr=6.log", "r") as ins:
        pos = []
        for idx,line in enumerate(ins):
            if '--- CR0C ---' in line:
                pos.append(idx+1)
            if '--- R1C ---' in line:
                pos.append(idx+1)
            if '--- CR1C ---' in line:
                pos.append(idx+1)
            if '--- R2C ---' in line:
                pos.append(idx+1)
            if '--- CR2C ---' in line:
                pos.append(idx+1)
            if '--- R3C ---' in line:
                pos.append(idx+1)

    # pprint(pos)

    with open("test_an=0.5_bl=0.5_lim=1_r=" + sys.argv[1] + "_liv=1_nr=5_pr=6.log", "r") as ins:
        # hr_BB_R1C = ''
        hr_SB_R1C = ''
        hr_SB_R2C = ''
        hr_SB_R3C = ''
        hr_SB_CR0C = ''
        hr_SB_CR1C = ''
        hr_SB_CR2C = ''

        for idx,line in enumerate(ins):

            # if idx == pos[0]:
            #     hr_BB_R1C=(line)
            if idx == pos[3]:
                hr_SB_CR0C=(line)
            if idx == pos[4]:
                hr_SB_R1C=(line)
            if idx == pos[5]:
                hr_SB_CR1C=(line)
            if idx == pos[6]:
                hr_SB_R2C=(line)
            if idx == pos[7]:
                hr_SB_CR2C=(line)
            if idx == pos[8]:
                hr_SB_R3C=(line)

    hr_sim={}
    hr_sim['hr_SB_CR0C']=hr_SB_CR0C.split()
    hr_sim['hr_SB_R1C']=hr_SB_R1C.split()
    hr_sim['hr_SB_CR1C']=hr_SB_CR1C.split()
    hr_sim['hr_SB_R2C']=hr_SB_R2C.split()
    hr_sim['hr_SB_CR2C']=hr_SB_CR2C.split()
    hr_sim['hr_SB_R3C']=hr_SB_R3C.split()

    if sys.argv[1] == '3':
        hr_sim['hr_SB_R1C'] += ['Q2o','Q3o','66o','87o','T5s']
        hr_sim['hr_SB_CR1C'] += ['JJo','KQs']
        # hr_sim['hr_SB_CR2C'] += ['KK','AA']
        hr_sim['hr_SB_R2C'] += ['88o','99o','TTo','ATo']
    if sys.argv[1] == '2':
        hr_sim['hr_SB_R1C'] += ['KQs','A9s']
        # hr_sim['hr_SB_CR1C'] += []
        # hr_sim['hr_SB_CR2C'] += []
        hr_sim['hr_SB_R2C'] += ['KK']
    if sys.argv[1] == '1.5':
        hr_sim['hr_SB_CR0C'] += ['Q4o']
        hr_sim['hr_SB_R1C'] += ['ATo']
        hr_sim['hr_SB_CR1C'] += ['KQo']
        # hr_sim['hr_SB_CR2C'] += []
        hr_sim['hr_SB_R2C'] += ['77','AQo','KK']
    if sys.argv[1] == '0.5':
        # hr_sim['hr_SB_CR0C'] += ['Q4o']
        hr_sim['hr_SB_R1C'] += ['KTo']
        hr_sim['hr_SB_CR1C'] += ['ATo']
        hr_sim['hr_SB_CR2C'] += ['KK', 'AA']
        hr_sim['hr_SB_R2C'] += ['AKo']
    if sys.argv[1] == '6':
        # hr_sim['hr_SB_CR0C'] += ['Q4o']
        hr_sim['hr_SB_R1C'] += ['AJo']
        hr_sim['hr_SB_CR0C'] += ['K8o']
        hr_sim['hr_SB_CR1C'] += ['66o']

    f=open("guru104.txt","a+")
    f.write("%s \n" % hr_sim['hr_SB_CR0C'])
    f.write("%s \n" % hr_sim['hr_SB_R1C'])
    f.write("%s \n" % hr_sim['hr_SB_CR1C'])
    f.write("%s \n" % hr_sim['hr_SB_R2C'])
    f.write("%s \n" % hr_sim['hr_SB_CR2C'])
    f.write("%s \n" % hr_sim['hr_SB_R3C'])
    f.close()
    '''
    Convert list into String
    '''
    # test1 = [reduce(lambda i, j: i+','+j,hr_sim['hr_SB_R1C'][:])]
    '''
    Refine hand format
    '''
    # refined_data=refine_hr(test1[0])
    # eval7.HandRange(refined_data)

    #pprint(hr_sim)
    raise1_r2c =         ['A2o', '33o', 'A3o', '44o', 'K4o', 'A4o', '55o', 'J5o', 'Q5o', 'K5o', 'A5o', '66o', 'T6o', 'J6o', 'Q6o', 'K6o', 'A6o', '97o', 'T7o', 'J7o', 'Q7o', 'K7o', 'A7o', '87s', '98o', 'T8o', 'J8o', 'Q8o', 'K8o', 'A8o', '95s', '96s', '97s', '98s', 'T9o', 'J9o', 'Q9o', 'K9o', 'A9o', 'T4s', 'T5s', 'T6s', 'T7s', 'T8s', 'T9s', 'JTo', 'QTo', 'KTo', 'J2s', 'J3s', 'J4s', 'J5s', 'J6s', 'J7s', 'J8s', 'J9s', 'JTs', 'QJo', 'KJo', 'Q2s', 'Q3s', 'Q4s', 'Q5s', 'Q6s', 'Q7s', 'Q8s', 'Q9s', 'QTs', 'QJs', 'K2s', 'K3s', 'K4s', 'K5s', 'K6s', 'K7s', 'K8s', 'K9s', 'KTs', 'KJs', 'A2s', 'A3s', 'A4s', 'A5s', 'A6s', 'A7s', 'A8s', 'A9s', 'ATo']

    raise2_r2c =         ['22o', 'A2o', '33o', 'K3o', 'A3o', '44o', 'Q4o', 'K4o', 'A4o', '55o', 'J5o', 'Q5o', 'K5o', 'A5o', '66o', 'T6o', 'J6o', 'Q6o', 'K6o', 'A6o', '76s', '87o', '97o', 'T7o', 'J7o', 'Q7o', 'K7o', 'A7o', '86s', '87s', '98o', 'T8o', 'J8o', 'Q8o', 'K8o', 'A8o', '95s', '96s', '97s', '98s', 'T9o', 'J9o', 'Q9o', 'K9o', 'A9o', 'T4s', 'T5s', 'T6s', 'T7s', 'T8s', 'T9s', 'JTo', 'QTo', 'KTo', 'J2s', 'J3s', 'J4s', 'J5s', 'J6s', 'J7s', 'J8s', 'J9s', 'JTs', 'QJo', 'KJo', 'Q2s', 'Q3s', 'Q4s', 'Q5s', 'Q6s', 'Q7s', 'Q8s', 'Q9s', 'QTs', 'QJs', 'KQo', 'K2s', 'K3s', 'K4s', 'K5s', 'K6s', 'K7s', 'K8s', 'K9s', 'KTs', 'KJs', 'A2s', 'A3s', 'A4s', 'A5s', 'A6s', 'A7s', 'A8s', 'KQs', 'A9s']

    raise3_r2c =         ['22o', 'K2o', 'A2o', '33o', 'K3o', 'A3o', '44o', 'Q4o', 'K4o', 'A4o', '54s', '55o', 'Q5o', 'K5o', 'A5o', '65s', 'Q6o', 'K6o', 'A6o', '75s', '76s', '97o', 'T7o', 'J7o', 'Q7o', 'K7o', 'A7o', '85s', '86s', '87s', '98o', 'T8o', 'J8o', 'Q8o', 'K8o', 'A8o', '95s', '96s', '97s', '98s', 'T9o', 'J9o', 'Q9o', 'K9o', 'A9o', 'T6s', 'T7s', 'T8s', 'T9s', 'JTo', 'QTo', 'KTo', 'J2s', 'J3s', 'J4s', 'J5s', 'J6s', 'J7s', 'J8s', 'J9s', 'JTs', 'QJo', 'KJo', 'Q2s', 'Q3s', 'Q4s', 'Q5s', 'Q6s', 'Q7s', 'Q8s', 'Q9s', 'QTs', 'QJs', 'KQo', 'K2s', 'K3s', 'K4s', 'K5s', 'K6s', 'K7s', 'K8s', 'K9s', 'KTs', 'KJs', 'A2s', 'A3s', 'A4s', 'A5s', 'A6s', 'A7s', 'A8s', 'A9s', 'Q2o', 'Q3o', '66o', '87o', 'T5s']

    raise6_r2c =          ['22o', 'A2o', '33o', 'A3o', '44o', 'A4o', '54s', '55o', 'A5o', '64s', '65s', 'A6o', '75s', '76s', 'A7o', '85s', '86s', '87s', 'A8o', '96s', '97s', '98s', 'T9o', 'K9o', 'A9o', 'T6s', 'T7s', 'T8s', 'T9s', 'JTo', 'QTo', 'KTo', 'ATo', 'J8s', 'J9s', 'JTs', 'QJo', 'KJo', 'Q5s', 'Q8s', 'Q9s', 'QTs', 'QJs', 'KQo', 'K2s', 'K3s', 'K4s', 'K5s', 'K6s', 'K7s', 'K8s', 'K9s', 'KTs', 'A2s', 'A3s', 'A4s', 'A5s', 'A6s', 'A7s']

    print("Diff between r=2 and 3 :%s" % Diff(raise2_r2c, raise3_r2c))
    print("Diff between r=1.5 and 2 :%s" % Diff(raise1_r2c, raise2_r2c))
    print("Diff between r=1.5 and 6 :%s" % Diff(raise1_r2c, raise6_r2c))




if __name__ == "__main__":
    main()
    print("Number of arguments: %d" % len(sys.argv))
    print ('Argument list: %s' % str(sys.argv))
