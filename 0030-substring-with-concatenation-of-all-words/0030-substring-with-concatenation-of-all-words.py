class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        target_map = {}
        if len(words)==0:
            return []
        for word in words:
            if word in target_map:
                target_map[word] = target_map[word] + 1
            else:
                target_map[word] = 1
        
        L = len(words[0])
        total_words = len(words)
        window_len = total_words * L
        res = []
        
        for i in range(L):
            right = i
            left = i
            window_words = {}
            count = 0

            while right + L <=len(s):
                word = s[right:right+L]
                right += L
                
                if word in target_map:
                    if word in window_words:
                        window_words[word] +=1
                    else:
                        window_words[word] = 1
                    count+=1
                    while window_words[word] > target_map[word]:
                        left_word = s[left:left+L]
                        window_words[left_word] -=1
                        count -=1
                        left+=L
                    if count == total_words:
                        res.append(left)
                else:
                    count = 0
                    window_words = {}
                    left = right
        return res