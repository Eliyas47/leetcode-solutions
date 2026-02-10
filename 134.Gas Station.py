class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        total_tank = 0   # Net gas balance across all stations
        curr_tank = 0    # Current gas balance while traveling
        start_index = 0  # Candidate starting station

        for i in range(len(gas)):
            total_tank += gas[i] - cost[i]
            curr_tank += gas[i] - cost[i]

            # If we run out of gas, reset start point
            if curr_tank < 0:
                start_index = i + 1
                curr_tank = 0

        # If overall gas is enough, return start_index; otherwise -1
        return start_index if total_tank >= 0 else -1
