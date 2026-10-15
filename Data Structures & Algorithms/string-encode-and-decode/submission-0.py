import json

class Solution:
    KEYNUMBER: Final[int] = 66

    def encode(self, strs: List[str]) -> str:
        strsJson = json.dumps(strs)
        output: str = ""

        for char in strsJson:
            output += chr(ord(char)^ self.KEYNUMBER)

        return output
        

    def decode(self, s: str) -> List[str]:
        json_str: str = ""
        for char in s:
            json_str += chr(ord(char)^ self.KEYNUMBER)

        output: List[str] = json.loads(json_str)

        return output