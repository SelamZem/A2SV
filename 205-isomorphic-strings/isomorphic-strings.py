class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        # s_dict = Counter(s)
        # t_dict = Counter(t)


        # for x, y in zip(s_dict.keys(), t_dict.keys()):
        #     if s_dict[x] != t_dict[y]:
        #         return False
        # return True

        if len(s)!=len(t):
            return False

        my_dict = {}

        n = len(s)
        for i in range(n):
            a , b = s[i], t[i]
            if a in my_dict:
                if my_dict[a]!=b:
                    return False
            else:
                if b in my_dict.values():
                    return False
            my_dict[a] = b
        return True
 