import hashlib
import re

TRIPLET = re.compile(r'([0-9a-f])\1\1')
FIVEINAROW = re.compile(r'([0-9a-f])\1\1\1\1')

SALT = 'ahsbgdzn'
# SALT = 'abc'
memo_ = dict()

def hashat(index):
    if index in memo_:
        return memo_[index]
    m = hashlib.md5()
    m.update((SALT + str(index)).encode('ascii'))
    memo_[index] = m.hexdigest()
    return memo_[index]

index = 0
nkeys = 0
while nkeys < 64:
    h = hashat(index)
    m = TRIPLET.search(h)
    if m:
        count = 0
        for j in range(index+1, index+1001):
            hh = hashat(j)
            mm = FIVEINAROW.search(hh)
            if mm and m.group(1) == mm.group(1):
                count += 1
        if count == 1:
            nkeys += 1
    index += 1
print(index-1)
