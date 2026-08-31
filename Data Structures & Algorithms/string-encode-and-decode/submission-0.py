class Solution:

    def encode(self, strs: List[str]) -> str:
        fstr = ""
        for i in strs:
            fstr += i
            fstr += "|||"
        return fstr

    def decode(self, s: str) -> List[str]:
        return s.split("|||")[:-1]