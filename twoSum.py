
def two_sum(nums, target):
    
    seen = {} 
     
    for i, x in enumerate(nums):
        
        want = target - x
        
        if want in seen:
            
            return [seen[want], i]
        
        seen[x] = i



