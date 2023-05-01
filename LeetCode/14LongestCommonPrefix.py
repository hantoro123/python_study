class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # 들어오는 strs의 길이와 비교할 문자열을 compare 변수에 넣는다.
        strs_len = len(strs)
        compare = strs[0]
        
        # strs 리스트에 1개 이상이 있다면 
        if strs_len > 1:
            # 길이만큼 반복하며
            for i in range(strs_len):
                # 반복될 prefix를 담을 변수
                prefix= ""
                try:
                    for j in range(len(compare)):
                        # compare과 같이 반복하며 비교하고
                        if compare[j] == strs[i][j]:
                            # 같으면 prefix에 더하고
                            prefix += strs[i][j]
                        else:
                            # 아니라면 compare을 prefix로 하고 break
                            compare = prefix
                            break
                # indexError가 난다면
                except IndexError:
                    # compare를 prefix를 넣고 다음으로 반복
                    compare = prefix
            # 반복이 종료되면 compare를 return
            return compare
                            
        else:
            # strs가 한개라면 strs의 문자열을 그대로 return
            return strs[0]