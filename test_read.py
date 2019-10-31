from pprint import pprint
# import test_constant_board as const

with open("guru100.txt", "r") as ins:
    array = []
    for line in ins:
        array.append(line.split())
# pprint(array)
mp={}

for i in range(len(array)-1):
    mp[array[i][0]]=(array[i][1],array[i][2],array[i][3])
pprint((mp))
print(len(mp))

scoop=tie=total=0
for key in mp:
    scoop = scoop + int(mp[key][0])
    tie = tie + int(mp[key][1])
    total = total + int(mp[key][2])
#     # test_scoop.append(const.list_test[i] - int(nArray[i][0]))
print("Equity: %18.9f " % ((scoop+tie*1.0/2)*1.0/total))
print("total game: %s" % total)
print("tie: %s" % tie)
print("scoop: %s" % scoop)

# Equity:        0.192509332
# total game: 585607968
