import copy
di = {'one': [1], 'two': [2], 'three': [3], 'four': [4]}
di2 = copy.deepcopy(di)

print(di)
print(di2)
di['four'][0] = 'cztery'
print(di)
print(di2)
