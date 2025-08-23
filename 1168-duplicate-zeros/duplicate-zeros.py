class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        n = len(arr)
        ptr1, ptr2 = 0, n-1

        while ptr1<n:
            a = arr[ptr1]
            if arr[ptr1]!=0:
                ptr1+=1

            else:
                ptr2 = n-1

                while ptr2>ptr1:
                    arr[ptr2]=arr[ptr2-1]
                    ptr2-=1
                
                ptr1+=2

        return arr
            