# week 1 hw
class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        products = [] 
        total = 1 
        for num in nums: 
            if num != 0: 
                total *= num
        
        zeros = 0 
        for i in range(len(nums)): 
            if nums[i] == 0: 
                zeros += 1 
        if zeros == 0: 
            for i in range(len(nums)): 
                if nums[i] != 0: 
                    new = total/nums[i]
                    products.append(new)
        elif zeros == 1: 
            for i in range(len(nums)): 
                if nums[i] != 0: 
                    products.append(0)
                else: 
                    products.append(total)
        else: 
            for i in range(len(nums)): 
                products.append(0)

        return products
