class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:

        for i in range(1, len(arr)):
            arr[i] ^= arr[i - 1]
        
  
        return [arr[end] ^ arr[start - 1] if start > 0 else arr[end] 
                for start, end in queries]

def kdsmain():
    input_data = sys.stdin.read().strip()
    lines = input_data.splitlines()
    
    num_test_cases = len(lines) // 2
    results = []

    for i in range(num_test_cases):
        arr = json.loads(lines[i*2])
        queries = json.loads(lines[i*2 + 1])
        
        result = Solution().xorQueries(arr, queries)
        results.append(json.dumps(result, separators=(',', ':')))

    with open('user.out', 'w') as f:
        for result in results:
            f.write(f"{result}\n")

if __name__ == "__main__":
    kdsmain()
    exit(0)
