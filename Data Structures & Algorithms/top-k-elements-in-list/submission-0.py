class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # one pass and you iteratively update a stack k long <-- this doesnt work 
        # hashmap, key is num in nums, value is count, go through map and pick k keys with highest count.
        # how to i pick k elements though?
        #       sort?
        # ^^ this is a solution

        # Tree based on counts?
        #   reorganizes based on count, like  2-> 3 then 2 becomes left child if k=2 and 3 becomes parent.
        # this is on the way to a solution. key is to use a heap.

        count = {}

        for num in nums:
            count[num] = 1 +count.get(num, 0)


        # arr = []
        # for k, v in count: 
        #     arr.append([k,v])
        # arr.sort()
        # can also sort hashmap by 
        res = sorted(count.items(), key=lambda x: x[1], reverse=True)
        k_keys = res[:k]
        return [key for key, _ in res[:k]]