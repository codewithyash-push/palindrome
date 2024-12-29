class Solution:
    def isPalindrome(self, x):
        # If the number is negative or ends with 0 (but isn't 0), it's not a palindrome
        if x < 0 or (x % 10 == 0 and x != 0):
            return False

        reversed_half = 0
        while x > reversed_half:
            reversed_half = reversed_half * 10 + x % 10
            x //= 10
        
        # For even length numbers, x should be equal to reversed_half
        # For odd length numbers, reversed_half // 10 will remove the middle digit
        return x == reversed_half or x == reversed_half // 10