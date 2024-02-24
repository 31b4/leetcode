class Solution:
    def findAllPeople(self, n: int, meetings: List[List[int]], firstPerson: int) -> List[int]:
        q = [(0, 0), (0, firstPerson)]

        graph = collections.defaultdict(list)
        for person_i, person_ii, time in meetings:
            graph[person_i].append((person_ii, time))
            graph[person_ii].append((person_i, time))

        answer = set()
        while q:
            time, person_i = heapq.heappop(q)
            if person_i in answer:
                continue
            answer.add(person_i)
            for person_ii, meeting_time in graph[person_i]:
                if meeting_time >= time:
                    heapq.heappush(q, (meeting_time, person_ii))
        return list(answer)
