import numpy as np
tree =  [
                [0,0,1,0,0,1,1,1],
                [0,0,0,0,0,0,0,1],
                [0,1,1,0,1,0,0,1],
                [0,1,0,0,1,1,0,1],
                [0,0,0,0,1,1,0,1],
            ]

tree = np.array(tree)

[rows, cols] = tree.shape

index = 1

for raw in range(rows):
    for col in range(cols):
        if tree[raw, col] == 1:
            tree[raw, col] = index
            index += 1

tree = np.insert(tree, 0, 0, 0)
tree = np.insert(tree, rows + 1, 0, 0)
tree = np.insert(tree, 0, 0, 1)
tree = np.insert(tree, cols + 1, 0, 1)

for raw in range(1, tree.shape[0]-1):
    for col in range(1, tree.shape[1]-1):
        
        if tree[raw, col] > 0:
            if tree[raw - 1, col] > 0:    #up
                tree[raw, col] = tree[raw - 1, col]
                    
            elif tree[raw, col - 1] > 0:  #left
                tree[raw, col] = tree[raw, col - 1] 

dic = {1:0}
for raw in range(1, tree.shape[0]-1):
    for col in range(1, tree.shape[1]-1):
        if tree[raw, col] > 0:
            if tree[raw, col] in dic:
                dic[tree[raw, col]] += 1
            else:
                dic[tree[raw, col]] = 1
print(max(dic.values()))
                    
            
            
            

            
            

        
    
