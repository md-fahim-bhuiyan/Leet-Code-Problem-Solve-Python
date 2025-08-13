class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        from collections import Counter
        if not s or not words: return []

        word_len = len(words[0])
        total_len = word_len * len(words)
        word_count = Counter(words)
        res = []

        for i in range(word_len):
            left = i
            cur_count = Counter()
            for j in range(i, len(s) - word_len + 1, word_len):
                word = s[j:j + word_len]
                if word in word_count:
                    cur_count[word] += 1
                    while cur_count[word] > word_count[word]:
                        cur_count[s[left:left + word_len]] -= 1
                        left += word_len
                    if j + word_len - left == total_len:
                        res.append(left)
                else:
                    cur_count.clear()
                    left = j + word_len
        return res
