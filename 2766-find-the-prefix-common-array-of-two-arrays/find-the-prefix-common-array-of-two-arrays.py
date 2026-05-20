class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:

        seenA = set()
        seenB = set()

        result = []

        for i in range(len(A)):

            seenA.add(A[i])
            seenB.add(B[i])

            common = seenA & seenB

            result.append(len(common))

        return result