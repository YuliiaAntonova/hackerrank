def pangrams(s):
    c='pangram'
    b='not pangram'
    if not set('abcdefghijklmnopqrstuvwxyz')-set(s.lower()):
        return c
    else:
        return b
print(pangrams('We promptly judged antique ivory buckles for the next prize'))
