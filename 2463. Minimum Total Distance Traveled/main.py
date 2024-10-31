from typing import List
from functools import lru_cache

class Solution:
    def minimumTotalDistance(self, robot: List[int], factory: List[List[int]]) -> int:
        # Sort robots and factories based on their positions
        robot.sort()
        factory.sort()
        
        # Extract factory positions and limits into separate lists
        factory_positions = [f[0] for f in factory]
        factory_limits = [f[1] for f in factory]
        
        # Memoized recursive function
        @lru_cache(None)
        def dp(robot_idx: int, factory_idx: int) -> int:
            # If all robots are assigned, no more distance to add
            if robot_idx == len(robot):
                return 0
            # If we run out of factories, return an arbitrarily large number (infeasible path)
            if factory_idx == len(factory_positions):
                return float('inf')
            
            # Option 1: Move to the next factory without assigning the current robot to this factory
            min_distance = dp(robot_idx, factory_idx + 1)
            
            # Option 2: Assign robots to this factory up to its limit
            total_distance = 0
            for i in range(factory_limits[factory_idx]):
                # Calculate distance if we assign `robot[robot_idx + i]` to `factory[factory_idx]`
                if robot_idx + i < len(robot):
                    total_distance += abs(robot[robot_idx + i] - factory_positions[factory_idx])
                    # Recursive call to check further assignments
                    min_distance = min(min_distance, total_distance + dp(robot_idx + i + 1, factory_idx + 1))
                else:
                    break
            
            return min_distance
        
        # Start the recursion from the first robot and first factory
        return dp(0, 0)
