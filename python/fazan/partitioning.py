import time

t0 = time.time()
cuvinte = open('words.txt', 'r+')
cuv = cuvinte.readline()
pref = cuv[0:2]
pref1 = ""
f = open(pref+'.txt', 'w')
f.write(cuv)
for cuv in cuvinte:
    pref1 = cuv[0:2]
    if pref == pref1:
        f.write(cuv)
    else:
        f = open(pref1+'.txt', 'w')
        pref = pref1
        f.write(cuv)
print time.time() - t0
raw_input("Check the time and press any key to exit ")
