from typing import List


def twoSum(nums: List[int], target: int) -> List[int]:
    for i in range(0, len(nums) - 1):
        for j in range(i+1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]
            else:
                continue


if __name__ == "__main__":
    print(twoSum(nums=[2, 5, 5, 11], target=10))
