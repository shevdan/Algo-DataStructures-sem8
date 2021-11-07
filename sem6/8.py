#works in O(n)
from typing import List


def solve(nums: List[int], k: int) -> bool:
    current_sum, sum_count = 0, 0
    sum_hash = {}

    for num in nums:
        # increase sum accumulated so far by current number, divide it by k
        current_sum = (current_sum + num) % k
        if num % k == 0 and current_sum != 0:
            continue
        # if value of subarray sum mod k is not zero - we have added in some subarray k. Return true
        if sum_hash.get(current_sum, 0):
            return True

        # increase current sum's number of occurrencess in hashmap by 1
        sum_hash[current_sum] = sum_hash.get(current_sum, 0) + 1

    return False


if __name__ == "__main__":
    print(solve([13, 1, 13, 1, 13, 13], 13))
