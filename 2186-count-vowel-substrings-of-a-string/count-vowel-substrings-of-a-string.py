class Solution:
    def countVowelSubstrings(self, word: str) -> int:
        vowels=['a','e','i','o','u']
        res = 0
        n = len(word)

        if n<5:
            return res
        for i in range(n):
            my_dict = defaultdict(int)
            for j in range(i,n):

                if word[j] not in vowels:
                    break

                my_dict[word[j]]+=1
                if len(my_dict.keys())==5:
                    res+=1
                

        return res
        

        

