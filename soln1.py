
# Trivial approach

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if s == "":
            return 0

        # characters in str
        chars: list[str] = list(s)

        # list of substrings
        subs: list[str] = []

        curr: str = ""
        curr_max: int = 0
        i: int = 0
        save: int = 0

        while i < len(chars):
            if chars[i] not in curr:
                curr += chars[i]
                i += 1
            else:
                subs.append(curr)
                if len(subs[len(subs) - 1]) >= len(subs[curr_max]):
                    curr_max = len(subs) - 1
                curr = ""
                i = save + 1
                save += 1

        subs.append(curr)
        if len(subs[len(subs) - 1]) >= len(subs[curr_max]):
            curr_max = len(subs) - 1
            curr = ""

        return len(subs[curr_max])
