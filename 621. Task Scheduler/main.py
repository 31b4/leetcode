class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # Count the frequency of each task
        task_counts = Counter(tasks)
        max_count = max(task_counts.values())
        
        # Calculate the number of tasks that have the maximum count
        max_count_tasks = sum(1 for count in task_counts.values() if count == max_count)
        
        # Calculate the number of intervals needed for tasks with cooling time
        intervals_needed = (max_count - 1) * (n + 1) + max_count_tasks
        
        # Return the maximum of intervals_needed and the length of tasks list
        return max(intervals_needed, len(tasks))
        
