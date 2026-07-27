class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        check={}
        for i,num in enumerate(nums):
            checked = target-num
            if checked in check:
                return check[checked],i
            check[num]=i
        return []