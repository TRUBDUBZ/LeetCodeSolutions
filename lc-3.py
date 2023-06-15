# Given a string s, find the length of the longest substring without repeating characters.

class Solution:
    def lengthOfLongestSubstring(self, s):
        char_set = set()  # Set to store unique characters
        left = 0  # Left pointer of the sliding window
        max_length = 0  # Maximum length of substring without repeating characters

        for right in range(len(s)):
            while s[right] in char_set:  # Shrink the window until the repeating character is removed
                char_set.remove(s[left])
                left += 1
            char_set.add(s[right])  # Add the current character to the set
            max_length = max(max_length, right - left + 1)  # Update the maximum length

        return max_length
