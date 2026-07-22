class Solution:
    def mirrorFrequency(self, s: str) -> int:
        cnt = {} 

        for c in s:
            target = None
            
            if c.isdigit():
                target = str(9 - int(c))

            elif c.isalpha():
                target = chr(219 - ord(c))

            if target and target in cnt:
                cnt[target] -= 1
                if cnt[target] == 0:
                    del cnt[target]
            else:
                cnt[c] = cnt.get(c, 0) + 1
            
        return sum(cnt.values())
        