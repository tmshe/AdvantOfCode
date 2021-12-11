inp = open("input.txt").read().splitlines()
out = 0
out_idx = []
rows = len(inp)
cols = len(inp[0])
for r in range(rows):
    for c in range(cols):
        q = inp[r][c]
        adj=[]
        for dr, dc in [[-1, 0], [1, 0], [0, 1], [0, -1]]:
            nr = r + dr
            nc = c + dc
            if 0 <= nr < rows and 0 <= nc < cols:
                adj.append(inp[nr][nc])
        if all(i > q for i in adj):
            out += 1 + int(q)
            out_idx.append((r,c))
print(out)

# =====
raw = []
# with open('sample.txt','r') as f: 
with open('input.txt','r') as f: 
    for line in f: 
        line = list(line.strip())
        raw.append([int(i) for i in line])

local_min_idx = []
col_dim = len(raw[0]) 
row_dim = len(raw) 
idx_max = row_dim * col_dim - 1
for row in range(row_dim): 
    for col in range(col_dim): 
        if row == 0: # top row 
            if col == 0: idx_lst = ((row, col), (row, col + 1), (row + 1, col)) #top left 
            elif col == col_dim - 1: idx_lst = ((row, col - 1), (row, col), (row + 1, col)) #top right
            else: idx_lst = ((row, col - 1), (row, col), (row, col + 1), (row + 1, col)) # rest of top row
        elif row == row_dim - 1: # bottom row 
            if col == 0: idx_lst = ((row, col), (row, col + 1), (row - 1, col)) #bottom left 
            elif col == col_dim - 1: idx_lst = ((row, col - 1), (row, col), (row - 1, col)) #bottom right
            else: idx_lst = ((row, col - 1), (row, col), (row, col + 1), (row - 1, col)) # rest of bottom row
        elif col == 0: # left col (no corners)
            idx_lst = ((row, col), (row, col + 1), (row - 1, col), (row + 1, col)) # rest of left col
        elif col == col_dim - 1: # right col (no corners)
            idx_lst = ((row, col - 1), (row, col), (row - 1, col), (row + 1, col)) # rest of left col
        else: 
            idx_lst = ((row, col - 1), (row, col), (row, col + 1), (row - 1, col), (row + 1, col))

        # idx_lst contains all coordinates that adjacent to the point of interest 
        local_num = []
        for coord in idx_lst:
            local_num.append(raw[coord[0]][coord[1]]) # come up with a list of numbers correspond to the adjecent points 
        local_min_coord = idx_lst[local_num.index(min(local_num))]
        if local_min_coord == (row, col): 
            local_min_idx.append(local_min_coord)
        else: 
            continue # if the local min is not the point of interest, skip 

local_min_idx = sorted(set(local_min_idx)) # remove duplicate

local_min_values = []
for coord in local_min_idx:
    local_min_values.append(raw[coord[0]][coord[1]])

print('end')