# with open("sample.txt","r") as f: 
with open("input.txt","r") as f: 
    for line in f: 
        line = line.strip().split(",")
raw = [int(i) for i in line]
print("Initial state: {}".format(raw))

end_day = 80
day = 0
while day < end_day: 
    day += 1
    new_fish = []
    for idx, value in enumerate(raw): 
        raw[idx] -= 1
        if raw[idx] < 0: 
            raw[idx] = 6
            new_fish.append(8)
    raw += new_fish 
    # print("After{}day: {}".format(day, raw))
print("after {} days, there are a total of {} fish".format(day, len(raw)))

print("end")
