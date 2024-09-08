PALAVRA = 'target'

def inv(s):
    if s == '': return s
    return s[-1] + inv(s[:-1])

print(inv(PALAVRA))
