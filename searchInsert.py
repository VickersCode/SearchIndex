
def findIndex(nums, target):
    for x in range(len(nums)):
        print(x)
        if nums[x] > target:
            
            return x

        else:
            return len(nums)

def searchInsert(nums, target) -> int:
    
    if target in nums:
        ans = nums.index(target)
        
        return ans
    
    else:
        return findIndex(nums, target)
    

nums = [1, 3, 5, 6]
target = 2
       
print(searchInsert(nums, target))