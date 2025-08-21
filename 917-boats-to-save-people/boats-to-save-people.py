class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        # given array of ppl
        # <=2 ppl at a time
        # return the minimum number of boats need
        n = len(people)
        boats =0 

        sorted_desc = sorted(people, reverse=True)

        ptr1, ptr2 = 0, n-1

        while ptr1<=ptr2:
            num1 = sorted_desc[ptr1]
            num2 = sorted_desc[ptr2]
            total = num1 + num2
            if total>limit:
                if num1<=limit:
                    boats+=1
                    ptr1 +=1
            else: 
                if total<=limit:
                    boats +=1
                    ptr1+=1
                    ptr2-=1

        return boats
