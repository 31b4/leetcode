class Solution:
    def rotateTheBox(self, box: List[List[str]]) -> List[List[str]]:
        
        n = len(box[0])-1
        
        for row in box:

            i,j = n,n             
            while i >= 0:
                
                if row[i] == '#':
                    if i < j: row[i], row[j] = '.', '#'                 
                    j -= 1

                elif row[i] == '*': j = i - 1 
                i -= 1

        return  map(list, zip(*(box[::-1])))   
