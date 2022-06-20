class Solution:
	def maxOperations(self, nums: List[int], k: int) -> int:
		count = 0
		hash = {}

		for num in nums:
			if k - num in hash:
				count += 1
				hash[k - num] -= 1

				if hash[k - num] == 0:
					hash.pop(k-num)

				continue

			if num in hash:
				hash[num] += 1
			else:
				hash[num] = 1

		return count
