class Solution:
    def romanToInt(self, s: str) -> int:
        my_dict = {
            'I':1,
            'V':5,
            'X':10,           
            'L':50,            
            'C':100,            
            'D':500,          
            'M':1000           
        }


        res = 0
        n = len(s)
        i = n-1
        while i>=0:
            a = s[i]
            if i!=0:
                b = s[i-1]
                if my_dict[b]<my_dict[a]:
                    res +=(my_dict[a]-my_dict[b])
                    i-=2
                    continue
            res += my_dict[a]
            i-=1

        return res