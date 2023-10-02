class Solution:
    def winnerOfGame(self, colors: str) -> bool:
        who = False #Alice start
        colors = list(colors)
        i = 1
        while i < len(colors)-1:
            if not who:#alice
                if colors[i-1] == "A" and colors[i+1] == "A" and colors[i] == "A":
                    del colors[i]
                    i = 0
                    who = True
                elif i == len(colors)-2:
                    return who
            else:
                if colors[i-1] == "B" and colors[i+1] == "B" and colors[i] == "B":
                    del colors[i]
                    i = 0
                    who = False
                elif i == len(colors)-2:
                    return who
            i += 1
        return who
