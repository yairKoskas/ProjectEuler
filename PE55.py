def isPalindrome(n):
    s = str(n)
    if len(s)%2 == 0:
        partO = s[0:int(len(s)/2)]
        partT = s[int(len(s)/2) :len(s)]
        if partT[::-1] == partO:
            return True
        return False
    else:
        partO = s[0:int(len(s) / 2)+1]
        partT = s[int(len(s) / 2):len(s)]
        if partT[::-1] == partO:
            return True
        return False
print(isPalindrome(14541))
print(isPalindrome(145541))