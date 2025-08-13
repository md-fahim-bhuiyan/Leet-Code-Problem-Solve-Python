class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        res = []
        line = []
        line_len = 0
        
        for w in words:
            if line_len + len(w) + len(line) > maxWidth:
                if len(line) == 1:
                    res.append(line[0] + ' ' * (maxWidth - line_len))
                else:
                    total_spaces = maxWidth - line_len
                    spaces_between = total_spaces // (len(line) - 1)
                    extra_spaces = total_spaces % (len(line) - 1)
                    justified_line = ''
                    for i in range(len(line) - 1):
                        justified_line += line[i]
                        justified_line += ' ' * (spaces_between + (1 if i < extra_spaces else 0))
                    justified_line += line[-1]
                    res.append(justified_line)
                line = []
                line_len = 0
            line.append(w)
            line_len += len(w)
        
        last_line = ' '.join(line)
        last_line += ' ' * (maxWidth - len(last_line))
        res.append(last_line)
        
        return res
