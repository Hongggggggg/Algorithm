#https://leetcode-cn.com/problems/long-pressed-name/
class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        name_len = len(name)
        typed_len = len(typed)
        i, j = 0, 0
        if name[i] != typed[j]:
            return False
        else:
            i += 1
            j += 1

        while(i < name_len and j < typed_len):
            if name[i] == typed[j]:
                i += 1
                j += 1
            else:
                while j < typed_len and typed[j] == typed[j - 1]:
                    j += 1
                
                if name[i] == typed[j]:
                    i += 1
                    j += 1
                else:
                    return False
        
        if i < name_len:
            return False
        else:
            while j < typed_len:
                if typed[j] == typed[j - 1]:
                    j += 1
                else:
                    return False
        return True
                    
            

