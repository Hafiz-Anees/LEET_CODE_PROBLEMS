class solution:
    def twoSum(self,nums:list[int],target:int):
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i]+nums[j]==target:
                    return [i,j]
                
s1 = solution()
print(s1.twoSum([3,2,4],6))
