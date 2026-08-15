class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        n = len(s) 
        # print(f"First: {s[0]}")
        left = 0 
        substring = ""
        finalSubstring = s[0]
        for right in range(n):
            while s[right] in substring:
                # print(f"Duplicate found: '{current_char}' at index {i}")
                left += 1 
                substring = substring[1:]
            substring = substring + s[right]
            # print(f"Substring: {substring}")
            if len(substring) > len(finalSubstring):
                finalSubstring = substring
            # print(f"After loop: {finalSubstring}")
            
        return len(finalSubstring)