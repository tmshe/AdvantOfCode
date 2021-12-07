import numpy as np
# with open('sample.txt', 'r') as f: 
#     for line in f: 
#         raw = line.strip().split()
# raw = np.loadtxt('sample.txt', delimiter=",")
raw = np.loadtxt('input.txt', delimiter=",")

# ===== part 1 ===== 
center = np.median(raw)
movement = np.abs(raw - center)
print("Part1 fuel consumption = {}".format(np.sum(movement)))

# ===== part 2 =====
center1 = int(np.mean(raw))
center2 = round(np.mean(raw), 0)
def CalcFuelConsumption(raw, center): 
    movement = np.abs(raw - center)
    result = np.sum(np.divide(np.add(np.square(movement), movement), 2))
    return result 
result1 = CalcFuelConsumption(raw, center1)
result2 = CalcFuelConsumption(raw, center2)
result = min(result1, result2)
print("Part2 fuel consumption = {}".format(result))

print('end')