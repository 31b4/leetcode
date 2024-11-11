from typing import List
import bisect

class Solution:
    def primeSubOperation(self, nums: List[int]) -> bool:
        # Helper function to generate list of primes up to max_num using Sieve of Eratosthenes
        def sieve(max_num):
            is_prime = [True] * (max_num + 1)
            is_prime[0] = is_prime[1] = False
            for i in range(2, int(max_num**0.5) + 1):
                if is_prime[i]:
                    for j in range(i * i, max_num + 1, i):
                        is_prime[j] = False
            return [i for i in range(2, max_num + 1) if is_prime[i]]
        
        # Generate all primes up to 1000
        primes = sieve(1000)
        
        # Iterate over nums and apply the operation as needed
        prev = 0  # Initialize the previous number in the strictly increasing sequence
        for i in range(len(nums)):
            # Find the largest prime less than nums[i] that makes nums[i] - prime > prev
            pos = bisect.bisect_left(primes, nums[i])
            success = False
            
            # Try possible primes in reverse order to find the largest possible prime
            for j in range(pos - 1, -1, -1):
                prime = primes[j]
                if nums[i] - prime > prev:
                    nums[i] -= prime
                    success = True
                    break
            
            # If no valid prime found, check if nums[i] is still greater than prev without change
            if not success and nums[i] <= prev:
                return False
            
            # Update prev to current element's value
            prev = nums[i]
        
        # If we succeeded in making the array strictly increasing, return True
        return True
