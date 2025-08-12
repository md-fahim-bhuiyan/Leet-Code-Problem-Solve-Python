class Solution:
    def generateParenthesis(self,n):
        r=[]
        def b(o,c,s):
            if o==n==c:
                r.append(s);return
            if o<n: b(o+1,c,s+"(")
            if c<o: b(o,c+1,s+")")
        b(0,0,"")
        return r
