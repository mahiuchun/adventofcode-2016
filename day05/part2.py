import hashlib

inp = 'reyedfim'

index = 0
password = [None]*8
rem = 8
while rem > 0:
    h = hashlib.new('md5')
    h.update((inp + str(index)).encode('ascii'))
    s = h.hexdigest()
    if s.startswith('00000'):
        pos = s[5]
        if ord('0') <= ord(pos) <= ord('7'):
            pos = int(pos)
            if password[pos] is None:
                password[pos] = s[6]
                rem -= 1
    index += 1

print(''.join(password))
