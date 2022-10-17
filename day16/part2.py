INIT = '11011110011011101'
LEN = 35651584

def dragon(s):
    t = s[::-1]
    t = t.replace('0', 't')
    t = t.replace('1', '0')
    t = t.replace('t', '1')
    return s + '0' + t

def checksum(s):
    n = len(s)
    buf = []
    for i in range(0, n, 2):
        pair = s[i:i+2]
        buf.append(str(1-(int(pair[0])^int(pair[1]))))
    t = ''.join(buf)
    if len(t) % 2 == 0:
        return checksum(t)
    else:
        return t

s = INIT
while len(s) < LEN:
    s = dragon(s)
print(checksum(s[:LEN]))
