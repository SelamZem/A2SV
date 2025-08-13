class Solution:
    def intToRoman(self, num: int) -> str:
        res = ""
        
        my_dict = {
            1:'I',
            5:'V',
            10:'X',
            50:'L',
            100:'C',
            500:'D',
            1000:'M',
        }

        n = len(str(num))-1

        for y in str(num):
            x = int(y)
            if x==4 or x==9:
                if x==4:
                    res += my_dict[10**n]
                    res += my_dict[5*(10**n)]
                else:
                    res += my_dict[10**n]
                    res += my_dict[10**(n+1)]
            else:
                if x>=5:
                    a = x%5
                    res += my_dict[5*(10**n)]
                    res += (my_dict[10**n])*a
                else:
                    res += (my_dict[10**n])*x

            n-=1

        return res
