import numpy as np 

# with open("sample.txt","r") as f: 
with open("input.txt","r") as f: 
    for line in f: 
        line = line.strip().split(",")
raw = [int(i) for i in line]
raw = np.array(raw, dtype=np.int32)
print("Initial state: {}".format(raw))

end_day = 256
day = 0
count = np.array([0] * 9, dtype=np.int64)
for i in raw: 
    count[i] += 1

while day < end_day: 
    day += 1
    count = np.roll(count, -1)
    count[6] += count[-1]
    # print("after {} days, there are a total of {} fish".format(day, count))
print("after {} days, there are a total of {} fish".format(day, np.sum(count)))
print("end")