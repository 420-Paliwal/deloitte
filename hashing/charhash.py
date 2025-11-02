def preHash(str, x):
    n = len(str)
    hassh = [0]* 26
    for i in str:
        hassh[ord(i) - ord('a')] += 1
    return hassh[ord(x)-ord('a')]

summ = preHash("abcbadae", 'a')
print(summ)