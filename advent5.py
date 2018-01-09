import hashlib

doorId = 'ojvtpuvg'
# doorId = 'abc'

i = 0
count = 0
result = ['_'] * 8
while True:
    i += 1
    h = hashlib.md5()
    h.update(doorId + str(i))
    m = h.hexdigest()
    if m.startswith('00000'):
        if m[5] in '01234567':
            print m[5]
            print m[6]
            it = int(m[5])
            if result[it] == '_':
                result[it] = m[6]
                print str(count) + ':' + ''.join(result)
                count += 1
                if count >= 8:
                    break

print ''.join(result)
# Loop until m starts with 5 00000's
