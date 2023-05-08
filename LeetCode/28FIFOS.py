class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        # needle의 길이를 담고
        j = len(needle)
        # i+j가 haystack의 길이를 넘어가면 불가능 하므로
        # i-j+1만큼만 반복하고
        for i in range(len(haystack)-j+1):
            # haystack의 i번부터 i+j-1번까지의 단어가
            # needle과 같다면 현재 i를 반환
            if haystack[i:i+j] == needle:
                return i
        # 다 돌았지만 같지 않다면 -1을 반환
        return -1
