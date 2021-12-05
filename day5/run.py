import re
raw = []
grid_x_lim = 0
grid_y_lim = 0

# with open("sample.txt",'r') as f: 
with open("input.txt",'r') as f: 
    for line in f: 
        line = line.strip()
        line = re.split(r',| -> ', line)
        line = [int(i) for i in line]
        raw.append(line)
        if line[0] > grid_x_lim: grid_x_lim = line[0]
        if line[2] > grid_x_lim: grid_x_lim = line[2]
        if line[1] > grid_y_lim: grid_y_lim = line[1]
        if line[3] > grid_y_lim: grid_y_lim = line[3]
grid_x_lim += 1
grid_y_lim += 1

# retain horizontal and vertical lines
hv_lines = []
diag_lines = []
for line in raw: 
    if (line[0] == line[2]) or (line[1] == line[3]): 
        hv_lines.append(line)
        continue 
    x_dis = abs(line[2] - line[0])
    y_dis = abs(line[3] - line[1])
    if x_dis == y_dis: 
        diag_lines.append(line)

# come up with coordinates of all points 
points_lst = []
for line in hv_lines:
    x_displacement = line[2] - line[0] # x2 - x1
    y_displacement = line[3] - line[1] # y2 - y1
    try: 
        x_sign = int(x_displacement / abs(x_displacement))
        x_steps = list(range(0, x_displacement + 1 * x_sign, x_sign))
    except: 
        x_steps = [0]
    try: 
        y_sign = int(y_displacement / abs(y_displacement))
        y_steps = list(range(0, y_displacement + 1 * y_sign, y_sign))
    except: 
        y_steps = [0]
    for x_increment in x_steps: 
        for y_increment in y_steps: 
            points_lst.append([line[0] + x_increment, line[1] + y_increment]) # x1 + x_inc, y1 + y_inc

for line in diag_lines: 
    x_displacement = line[2] - line[0] # x2 - x1
    y_displacement = line[3] - line[1] # y2 - y1 
    # assert abs(x_displacement) != abs(y_displacement), "diag_line: x_step does not equal to y_step"
    # x and y can step in different directions 
    x_sign = int(x_displacement / abs(x_displacement))
    x_steps = list(range(0, x_displacement + 1 * x_sign, x_sign))
    y_sign = int(y_displacement / abs(y_displacement))
    y_steps = list(range(0, y_displacement + 1 * y_sign, y_sign))
    assert len(x_steps) == len(y_steps) 
    for idx in range(0,len(x_steps)): 
        x_increment = x_steps[idx]
        y_increment = y_steps[idx]
        points_lst.append([line[0] + x_increment, line[1] + y_increment]) 

# create map 
map = []   
for i in range(0, (grid_y_lim)): 
    map.append([0] * (grid_x_lim)) 
# add lines to map
for coord in points_lst: 
    map[coord[1]][coord[0]] += 1
# # print map
# for i in map: print(i)

# count danger points
danger_count = 0
for row in map:
    for point in row: 
        if point >= 2: 
            danger_count += 1
        
print("anywhere in the diagram with a 2 or larger - a total of {} points".\
    format(danger_count))

print(line)
        
    