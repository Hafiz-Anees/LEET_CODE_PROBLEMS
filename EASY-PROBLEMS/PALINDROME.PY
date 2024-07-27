class Solution:
    def isPalindrome(self, x: int) -> bool:
        # MAIN CODE IS HERE 
        if x < 0:
            return False
        a = x
        rev = str(x)[::-1]
        rev = int(rev)
        if rev == a:
            return True
