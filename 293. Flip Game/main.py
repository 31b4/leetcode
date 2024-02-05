class Solution:
    def generatePossibleNextMoves(self, currentState: str) -> List[str]:
        next_states = []
        for i in range(1, len(currentState)):
            if currentState[i - 1] == currentState[i] == "+":
                new_state = currentState[:i - 1] + "--" + currentState[i + 1:]
                next_states.append(new_state)

        return next_states
