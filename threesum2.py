def threeSum(nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        output = []
        size = len(nums)

        map_ = {}

        for i_idx, i in enumerate(nums):
            if not i in map_:
                map_[i] = [i_idx]
            else:
                map_[i].append(i_idx)

        print map_

                
        for i_idx, i in enumerate(nums[0:len(nums) - 2]):
            for j_idx in range(i_idx + 1, size - 1):
                j = nums[j_idx]
                sum_ = j + i

                remains = 0 - sum_

                if remains in map_:
                    for k_idx in map_[remains]:
                        print (i_idx, j_idx, k_idx, i, j, nums[k_idx])

                        if k_idx != i_idx and k_idx != j_idx:
                            output.append(sorted([i, j, nums[k_idx]]))
        
        distinct_output = []
        
        for o in output:
            if o not in distinct_output:
                distinct_output.append(o)
        
        return distinct_output

print threeSum([0,0,0])