class Solution:
    def repeatedStringMatch(self, a: str, b: str) -> int:
        repeat = -(-len(b) // len(a)) 
        s = a * repeat
        if b in s:
            return repeat
        if b in s + a:
            return repeat + 1
        return -1