class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        oldarr = -1

        for i in range(len(arr) - 1, -1, -1):
            newMax = max(oldarr, arr[i])
            arr[i] = oldarr
            oldarr = newMax
        return arr