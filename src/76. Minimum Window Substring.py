import collections


class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        # need = collections.defaultdict(int)
        # window = collections.defaultdict(int)
        # for c in t:
        #     need[c] += 1
        # left = 0
        # right = 0
        # cnt = 0
        # res = ""
        # while right < len(s):
        #     c = s[right]
        #     right += 1
        #     if c in need:
        #         window[c] += 1
        #         if window[c] == need[c]:
        #             cnt += 1
        #     # print("cnt", cnt, "len(need)", len(need))
        #     while cnt == len(need):
        #         if not res or right - left < len(res):
        #             res = s[left:right]
        #             # print(res)
        #         d = s[left]
        #         left += 1
        #         if d in need:
        #             if need[d] == window[d]:
        #                 cnt -= 1
        #         window[d] -= 1
        # return res

        need = collections.defaultdict(int)
        for c in t:
            need[c] += 1
        cnt = len(t)
        left = 0
        right = 0
        res = ""
        while right < len(s):
            if need[s[right]] > 0:
                cnt -= 1
            need[s[right]] -= 1
            if cnt == 0:
                while need[s[left]] != 0:
                    need[s[left]] += 1
                    left += 1
                if not res or right - left + 1 < len(res):
                    res = s[left:right + 1]
                cnt += 1
                need[s[left]] += 1
                left += 1
            right += 1
        return res
