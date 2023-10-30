

def isPalindrome(x):
    
    rev = ''.join(reversed(str(x)))

    if(x == int(rev)):
        return True
    else:
        return False

print(isPalindrome(21))