import json

class Solution:
    KEYNUMBER: Final[int] = 66

    def encode(self, strs: List[str]) -> str:
        strs_bytes = json.dumps(strs).encode('utf-8')
        output = bytearray(b^ self.KEYNUMBER for b in strs_bytes)
        
        return output.hex()

    def decode(self, s: str) -> List[str]:
        s_bytes = bytes.fromhex(s)
        s_bytearray = bytearray(b^ self.KEYNUMBER for b in s_bytes)
        s_json = s_bytearray.decode('utf-8')
        
        return  json.loads(s_json)