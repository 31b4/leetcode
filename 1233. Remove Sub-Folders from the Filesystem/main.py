class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        folder.sort()
        
        result = []
        for f in folder:
            if not result or not f.startswith(result[-1] + '/'):
                result.append(f)
        
        return result
