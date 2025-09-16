class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        ans = [-1]* len(score)
        my_dict = defaultdict()
        for i, x in enumerate(score):
            my_dict[i]=x
        sort_dict = dict(sorted(my_dict.items(), key=lambda x:x[1], reverse=True))
        top_3 = 0

        for x in sort_dict:
            if top_3==0:
                ans[x]="Gold Medal"
            elif top_3==1:
                ans[x]="Silver Medal"
            elif top_3==2:
                ans[x]="Bronze Medal"
            else:
                ans[x]=str(top_3+1)
            top_3+=1

        return ans
        