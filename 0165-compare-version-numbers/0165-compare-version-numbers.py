class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        v1 = version1.split('.')
        v2 = version2.split('.')
        
        n1, n2 = len(v1), len(v2)
        
       
        for i in range(max(n1, n2)):
            rev1 = int(v1[i]) if i < n1 else 0
            rev2 = int(v2[i]) if i < n2 else 0
            
            if rev1 < rev2:
                return -1
            elif rev1 > rev2:
                return 1
                
        return 0