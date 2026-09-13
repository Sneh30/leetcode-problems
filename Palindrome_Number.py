class Solution:
    def isPalindrome(self, x: int) -> bool:
        n = x
        check =0
        while n>0:
            ld = n%10
            check = (check*10)+ld
            n=n//10
        return check == x
