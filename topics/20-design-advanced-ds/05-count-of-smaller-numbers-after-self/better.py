# Merge sort, counting cross-inversions during the merge step — Time: O(n log n), Space: O(n)
from typing import List


class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        n = len(nums)
        counts = [0] * n
        indices = list(range(n))

        def merge_sort(idx_list: List[int]) -> List[int]:
            if len(idx_list) <= 1:
                return idx_list

            mid = len(idx_list) // 2
            left = merge_sort(idx_list[:mid])
            right = merge_sort(idx_list[mid:])

            merged = []
            i = j = 0
            while i < len(left) and j < len(right):
                if nums[left[i]] <= nums[right[j]]:
                    # every right-half element already merged (there are j of them) is < nums[left[i]]
                    counts[left[i]] += j
                    merged.append(left[i])
                    i += 1
                else:
                    merged.append(right[j])
                    j += 1
            while i < len(left):
                counts[left[i]] += j
                merged.append(left[i])
                i += 1
            while j < len(right):
                merged.append(right[j])
                j += 1

            return merged

        merge_sort(indices)
        return counts


if __name__ == "__main__":
    sol = Solution()
    print("Expected: [2,1,1,0], Got:", sol.countSmaller([5, 2, 6, 1]))
    print("Expected: [0], Got:", sol.countSmaller([-1]))
    print("Expected: [0,0], Got:", sol.countSmaller([-1, -1]))
