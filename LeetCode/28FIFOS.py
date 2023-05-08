class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        # haystack 만큼 반복하는데
        for i in range(len(haystack)):
            # 같으면 True
            same = True
            # haystack이 needle의 첫번째와 같으면
            if haystack[i] == needle[0]:
                # needle이랑 같은지 확인하고
                for j in range(1,len(needle)):
                    if i+j == len(haystack) or haystack[i+j] != needle[j]:
                        # 다르면 same을 False로
                        same = False
                        break
                # same이 True면 i를 반환
                if same:
                    return i
            # 다르면 다음으로 넘어감
            else:
                continue
        # needle과 같은 부분이 없으면 -1출력
        return -1