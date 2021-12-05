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

# retain horizontal and vertical lines
hv_lines = []
for line in raw: 
    if (line[0] == line[2]) or (line[1] == line[3]): 
        hv_lines.append(line)

# come up with coordinates of all points 
points_lst = []
for line in hv_lines:
    x1 = line[0]
    x2 = line[2]
    y1 = line[1]
    y2 = line[3]
    x_displacement = x2 - x1
    y_displacement = y2 - y1
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
            points_lst.append([x1 + x_increment, y1 + y_increment])


# create map 
map = []   
for i in range(0, (grid_y_lim + 1)): 
    map.append([0] * (grid_x_lim + 1)) 
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
        
    