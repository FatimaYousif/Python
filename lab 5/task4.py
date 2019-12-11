#task4
def reverse(s): 
    return s[::-1] 
  
def Palindrome(s): 
    rev = reverse(s) 
  
    if (s == rev): 
        return True
    return False
s=Palindrome("mom")
print(s)