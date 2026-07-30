class Solution:
    def encode(self, strs: List[str]) -> str:
        out = []
        for s in strs:
            curr = ""
            for c in s:
                if c == '[':
                    curr += '\\['
                elif c == ']':
                    curr += '\\]'
                elif c == '\\':
                    curr += '\\\\'
                else:
                    curr += c
            out.append('[' + curr + ']')
        return "".join(out)

    def decode(self, s: str) -> List[str]:
        out = []
        i = 0
        if len(s) == 0:
            return out
        curr = None
        while i < len(s):
            if s[i] == '\\':
                if i + 1 < len(s):
                    if s[i + 1] in ['[', ']', '\\']:
                        curr += s[i + 1]
                        i += 1
            elif s[i] == '[':
                curr = ""
            elif s[i] == ']':
                out.append(curr)
            else:
                curr += s[i]
            i += 1
        return out

