class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        num_set = set(nums)
        longest = 0

        for num in num_set:
            # Only start counting if `num` is the start of a sequence
            if num - 1 not in num_set:
                current = num
                length = 1

                # Count forward while the next number is in the set
                while current + 1 in num_set:
                    current += 1
                    length += 1

                longest = max(longest, length)

        return longest
                    
