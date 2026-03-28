class Solution:
    def checkRecord(self, s: str) -> bool:
        # Rule 1: fewer than 2 absences
        if s.count('A') >= 2:
            return False
        
        # Rule 2: no "LLL" substring
        if "LLL" in s:
            return False
        
        return True
