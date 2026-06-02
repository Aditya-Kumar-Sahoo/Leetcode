class Solution:
    def earliestFinishTime(
        self,
        landStartTime: List[int],
        landDuration: List[int],
        waterStartTime: List[int],
        waterDuration: List[int]
    ) -> int:

        ans = float('inf')

        # Land -> Water
        for i in range(len(landStartTime)):
            land_finish = landStartTime[i] + landDuration[i]

            for j in range(len(waterStartTime)):
                ans = min(
                    ans,
                    max(land_finish, waterStartTime[j]) + waterDuration[j]
                )

        # Water -> Land
        for j in range(len(waterStartTime)):
            water_finish = waterStartTime[j] + waterDuration[j]

            for i in range(len(landStartTime)):
                ans = min(
                    ans,
                    max(water_finish, landStartTime[i]) + landDuration[i]
                )

        return ans