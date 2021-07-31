class Solution:
    def canCompleteCircuit(self, gas: list, cost: list) -> int:
        n = len(gas)
        starts = []
        for i in range(n):
            if cost[i] <= gas[i]:
                starts.append(i)

        if len(starts) == 0:
            return -1
        for index, val in enumerate(starts):
            i = val
            tank = 0
            result = True
            for count in range(n):
                tank += gas[i] - cost[i]
                if tank < 0:
                    result = False
                    break
                if i == n - 1:
                    i = 0
                else:
                    i += 1
            if result:
                return val

        return -1
