class Solution:
    def readBinaryWatch(self, turnedOn: int) -> List[str]:
        times = [(h, m) for h in range(12) for m in range(60)]
        valid_times = [t for t in times if bin(t[0]).count('1') + bin(t[1]).count('1') == turnedOn]
        return [f"{h}:{m:02d}" for h, m in valid_times]