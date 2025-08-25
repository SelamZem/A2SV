class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        # n = len(nums)
        # ps = [0]*n
        # res = 0

        # for i in range(n):
        #     if i ==0:
        #         ps[0]=nums[i]
        #     else:
        #         ps[i] = ps[i-1] + nums[i]
        # print(ps)
        # for i in range(n):
        #     for j in range(i,n):

        #         if ps[j]%k==0:
        #             res+=1
        #         ps[j]=ps[j]-nums[i]

        # return res       

        #neetcodeio
        prefix_sum = 0
        res = 0
        rem_count = defaultdict(int)
        rem_count[0]=1

        for n in nums:
            prefix_sum+=n
            rem = prefix_sum%k

            res+=rem_count[rem]
            rem_count[rem]+=1

        return res
