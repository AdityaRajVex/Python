# class Solution:
#     def lengthOfLongestSubstring(self, s: str) -> int:
#         left = max_length = 0
#         char_set = set()
#         for right in range(len(s)):
#             while s[right] in char_set:
#                 char_set.remove(s[left])
#                 left += 1
#             char_set.add(s[right])
#             max_length = max(max_length, right - left + 1)
#         return max_length
#
#
# class Solution:
#     def lengthOfLongestSubstring(self, s: str) -> int:
#         left = max_length = 0
#         count = {}
#         for right, c in enumerate(s):
#             count[c] = 1 + count.get(c, 0)
#             while count[c] > 1:
#                 count[s[left]] -= 1
#                 left += 1
#             max_length = max(max_length, right - left + 1)
#
#         return max_length
# lists = [1,2 ,3 ,4,5]
# print(4%2)
#
#
# class Solution:
#     def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
#         lists = nums1 + nums2
#         lists.sort()
#         length = len(lists)
#         print('length =', length)
#         print('list =', lists)
#         if length > 1:
#             if length % 2 == 0:
#                 print('remainder executed!')
#                 left = (length % 2) - 1
#                 right = left + 1
#                 print('left = ', left, '\nright = ', right)
#                 print('median =', lists[left], '+', lists[right], '/2')
#                 median = (lists[left] + lists[right]) / 2
#                 return median
#             else:
#                 print('integer executed!')
#                 median = lists[length // 2]
#                 return median
#         return lists[0]
#
#
#
# i = j = m1 = m2 = 0
# n = len(nums1)
# m = len(nums2)
#
# for count in range(0, ((n + m) // 2) + 1):
#     m2 = m1
#     if i < n and j < m:
#         if nums1[i] > nums2[j]:
#             m1 = nums2[j]
#             j += 1
#         else:
#             m1 = nums1[i]
#             i += 1
#     elif i < n:
#         m1 = nums1[i]
#         i += 1
#     else:
#         m1 = nums2[j]
#         j += 1
#
# if (n + m) % 2 != 0:
#     return m1
# else:
#     return (m1 + m2) / 2

print((3)//2 )