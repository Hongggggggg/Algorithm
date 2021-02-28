step = [2, 3, 1, 1, 4, 2, 0, 0, 0]

def canJump(array):
    cover = 0
    if len(array) == 1 :
        return True
    i = 0
    while(i <= cover):
        cover = max(i + array[i], cover)
        i += 1
        if cover >= len(array) - 1: 
            return True

    return False

print(canJump(step))
