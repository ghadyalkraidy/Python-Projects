def longestPalSubsA(s):
    start = s[:1]
    end = s[::-1]
    for i in range(len(s)):
        for j in range(i,len(s) - 1):
            t = s[i:j + 1]
            if t == t[::-1]:
                start = t
                end = t[::-1]
    return start
def longestPalSubsB(s,start,end):
    if s[start:end + 1] == s[start:end + 1:-1]:
        return s[start:end + 1]
s = input()
print(longestPalSubsA)
print(longestPalSubsB)


