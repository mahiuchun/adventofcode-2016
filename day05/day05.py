import hashlib

inp = 'reyedfim'

index = 0
password = []
while len(password) < 8:
    h = hashlib.new('md5')
    h.update((inp + str(index)).encode('ascii'))
    s = h.hexdigest()
    if s.startswith('00000'):
        password.append(s[5])
    index += 1

print(''.join(password))
