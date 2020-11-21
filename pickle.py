#%%

f = ' ./ttt.txt'
with open(f, 'r') as infile:
    line = infile.readline()
    while line:
    print(line)
    line = infile.readline()

#%%
# Paths
Relative path vs. Absolute Path

#%%
fw = 't2.txt'
with open(fw, 'w') as outfile:
    outfile.write('Abc\n')
    outfile.write('def')


import _pickle
a = 60
b = 78
fw = 't3.dat'
with open(fw, wb') as outfile:
    _pickle.dump(a, outfile)


#%%

import _pickle
fw = 't3.dat'
with open(fw,'rb') as infile:
    out_a = _pickle.load(infile)
    print('Got from file: ' + str(out_a))


#%%