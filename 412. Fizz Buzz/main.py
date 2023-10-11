class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        ans = []
        for i in range(1,n+1):
            fizz = i % 3 == 0
            buzz = i % 5 == 0
            if fizz and buzz:
                ans.append("FizzBuzz")
            elif fizz:
                ans.append("Fizz")
            elif buzz:
                ans.append("Buzz")
            else:
                ans.append(str(i))
        return ans
