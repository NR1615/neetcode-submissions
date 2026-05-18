class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap={}

        for i in range(len(nums)):
            if nums[i] in hashmap:
                hashmap[nums[i]]+=1
            else:
                hashmap[nums[i]]=1
        
        sorted_key=sorted(hashmap,key=hashmap.get, reverse=True)
        return sorted_key[:k]
        

        