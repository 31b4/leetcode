class Solution:
    def getWinner(self, arr: List[int], k: int) -> int:
        n=len(arr)
        cur=arr[0]
        count=0
        for i in range(1,n):
            if arr[i]>cur:
                cur=arr[i]
                count=0
            count+=1
            if count==k:
                break
        return cur
