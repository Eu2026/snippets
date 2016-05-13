import time

t0 = time.time()
cuvinte = open('cuvinte.txt','r+')
#alfabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y'
cuv = cuvinte.readline()
pref = cuv[0:2]
pref1 = ""
f = open(pref+'.txt','w')
f.write(cuv)
for cuv in cuvinte:
    if pref == pref1:
        f.write(cuv)
    else:
        f = open(pref1+'.txt','w')
        pref = pref1
        f.write(cuv)
print time.time() - t0
raw_input("Check the time and press any key to exit ")
