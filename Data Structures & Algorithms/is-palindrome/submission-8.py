class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        #recreate string s with only alphanumeric characters
        s=s.lower()
        s2=""
        for char in s:
            if char.isalnum():
                s2+=char

        for i in range(0, len(s2)//2):
            if s2[i]!=s2[-(i+1)]:
                print(s2[i], s2[-(i+1)])
                return False

        return True