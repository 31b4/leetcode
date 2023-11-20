class Solution:
    def garbageCollection(self, garbage: List[str], travel: List[int]) -> int:
        def pickUp(garbage_type):
            i = 0
            time = 0
            sv = 0
            for g in garbage:
                for t in g:
                    if t == garbage_type:
                        time += 1
                        time += sv
                        sv = 0
                if i < len(travel):
                    sv+=travel[i]
                    i+=1
            return time
                


        return pickUp("M") + pickUp("P") + pickUp("G")
