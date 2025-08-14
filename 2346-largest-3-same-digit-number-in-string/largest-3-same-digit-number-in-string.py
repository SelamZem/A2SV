class Solution:
    def largestGoodInteger(self, num: str) -> str:
        # given string of nums
        ## good??
            #if substring num is len 3
            # consists only one unique digit
        # return good integer as string or empty string if none

        n = len(num)
        if n<3:
           return ""

        res = ""
        for i in range(n-2):
            sub_str = num[i:i+3]
            if sub_str[0]==sub_str[1]==sub_str[2]:
                if res:
                    if int(res[-1])<int(sub_str[0]):
                        res=sub_str
                else:
                    res = sub_str
        return res
                