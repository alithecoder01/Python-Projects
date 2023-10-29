
def twoSum(nums,target):
    lenght = len(nums)
    for i in range(lenght):
        for j in range(i+1,lenght):
            if( nums[i]+nums[j] == target):
                return[i,j]
            


nums =[2,9,8,1]
print(twoSum(nums,9))




