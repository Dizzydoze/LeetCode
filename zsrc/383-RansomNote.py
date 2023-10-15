class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        # counting with hashtable
        ran, mag = {}, {}
        for ch in ransomNote:
            if ch in ran:
                ran[ch] += 1
            else:
                ran[ch] = 1
        for ch in magazine:
            if ch in mag:
                mag[ch] += 1
            else:
                mag[ch] = 1
        for ch, cnt in ran.items():
            if ch not in mag:
                return False
            elif mag[ch] < ran[ch]:
                return False
        return True
