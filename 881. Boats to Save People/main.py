class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        sorted_people = sorted(people)
        res = 0
        print(sorted_people)

        i,j = 0,len(sorted_people) - 1
        while i <= j:
            if sorted_people[j] == limit:
                res += 1
                j -= 1
            elif sorted_people[i] + sorted_people[j] > limit:
                res += 1
                j -= 1
            else:
                res += 1
                j -= 1
                i += 1

        return res


        """ Idiota vagyok
        # remove limit numbers
        for x in sorted_people[::-1]:
            if x < limit:
                break
            res += 1
            sorted_people.pop(-1)


        dict_people = defaultdict(int)
        # county each num
        for x in sorted_people:
            dict_people[x] += 1
   
        

        while sorted_people:
            curr = sorted_people.pop(0)
            dict_people[curr] -= 1

            if curr == limit:
                res+=1
            else:
                for i in range(limit-curr, 0, -1):
                    if dict_people[i] > 0:
                        sorted_people.pop(sorted_people.index(i))
                        dict_people[i] -= 1
                        break
                res += 1 
        return res
        """
