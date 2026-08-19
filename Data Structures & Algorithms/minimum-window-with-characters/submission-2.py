class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""
        need = {} 
        window = {}
        
        l = 0
        for char in t:
            need[char] = need.get(char, 0) + 1
        need_count = len(need)
        have = 0
        min_len = float("inf")
        res = ""
        for r in range(len(s)):
            # add s[r] to window
            window[s[r]] = window.get(s[r], 0) + 1
            if s[r] in need and window[s[r]] == need[s[r]]:
                have += 1
           
            # if the window now contains everything needed:
            while have == need_count:
                window_length = r - l + 1

                if window_length < min_len:
                    min_len = window_length
                    res = s[l:r + 1]

                window[s[l]] -= 1

                if s[l] in need and window[s[l]] < need[s[l]]:
                    have -= 1
                l += 1
        return res
        