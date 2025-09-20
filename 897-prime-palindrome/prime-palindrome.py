class Solution:
    def primePalindrome(self, n: int) -> int:
        def is_prime(x):
            if x < 2:
                return False
            if x % 2 == 0:
                return x == 2
            r = int(x**0.5)
            for i in range(3, r + 1, 2):
                if x % i == 0:
                    return False
            return True

        if n <= 2:
            return 2
        if n <= 3:
            return 3
        if n <= 5:
            return 5
        if n <= 7:
            return 7
        if n <= 11:
            return 11

        for length in range(1, 10**8):  
            s = str(length)
            # reverse the string except the last character
            
            palindrome = int(s + s[-2::-1])
            if palindrome >= n and is_prime(palindrome):
                return palindrome