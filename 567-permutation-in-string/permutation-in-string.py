class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        hash1 = Counter(s1)

        n = len(s1)
        m = len(s2)
   
        if m<n:
            return False

        window =  Counter(s2[:n])

        i = 0
        while i+n<=m:

            if window == hash1:
                return True
           
            if i + n < m:
                window[s2[i+n]]+=1
                window[s2[i]]-=1
                if window[s2[i]]==0:
                    del window[s2[i]]
            i+=1
        
        return False


