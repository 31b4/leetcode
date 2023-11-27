class Solution:
    def knightDialer(self, n: int) -> int:        
        arr = [1 for _ in range(10)]
        
        for i in range(n-1):
            tmp = [
                    arr[4]+arr[6],
                    arr[6]+arr[8],
                    arr[7]+arr[9],
                    arr[4]+arr[8],
                    arr[3]+arr[9]+arr[0],
                    0,
                    arr[1]+arr[7]+arr[0],
                    arr[2]+arr[6],
                    arr[1]+arr[3],
                    arr[2]+arr[4]
                  ]
            
            arr = tmp
        
        return sum(arr)%(10**9+7)
