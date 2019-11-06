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

    f=open("guru104.txt","a+")
    f.write("%s \n" % hr_sim['hr_SB_CR0C'])
    f.write("%s \n" % hr_sim['hr_SB_R1C'])
    f.write("%s \n" % hr_sim['hr_SB_CR1C'])
    f.write("%s \n" % hr_sim['hr_SB_R2C'])
    f.write("%s \n" % hr_sim['hr_SB_CR2C'])
    f.write("%s \n" % hr_sim['hr_SB_R3C'])
    f.close()

    # test1 = [reduce(lambda i, j: i+','+j,hr_sim['hr_SB_R1C'][:])]
    # refined_data=refine_hr(test1[0])
    # eval7.HandRange(refined_data)
    pprint(hr_sim)




if __name__ == "__main__":
    main()
    print("Number of arguments: %d" % len(sys.argv))
    print ('Argument list: %s' % str(sys.argv))
