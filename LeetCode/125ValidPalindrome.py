class Solution:
    def isPalindrome(self, s: str) -> bool:
        # 컴프리헨션을 통해 문자열의 알파벳과 숫자만 받아서 배열에 넣는다.
        palindrome = [i.lower() for i in s if i.isalnum()]
        # 뽑아낸 문자열과 거꾸로가 같으면 True 다르면 False를 반환한다.
        return palindrome == palindrome[::-1] 