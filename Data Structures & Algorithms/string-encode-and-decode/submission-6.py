class Solution:
    def encode(self, strs: List[str]) -> str:
        def enc(s):
            return f"{len(s)};{s}"
        return "".join(enc(s) for s in strs)
        

    def decode(self, s: str) -> List[str]:
        # print(s)
        out = []
        c, i, buf = "", 0, ""
        while i < len(s):
            while s[i] != ";": # len(s)
                buf += s[i]
                i += 1
            i += 1 # skip delim
            if buf == "":
                break
            sz = int(buf)
            buf = ""
            os = ""
            j = 0
            while j < sz:
                os += s[j + i]
                j += 1
            i += j
            out.append(os)
        return out