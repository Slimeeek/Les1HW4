s = 'smooms'
def func(s):
    s = s
    for i in range(len(s)-1):
        if s[i] == s[i - i*2 - 1]:
            return True
        else:
            return False
print(func(s))