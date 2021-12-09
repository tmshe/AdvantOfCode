from os import error


raw = []
# with open('sample.txt', 'r') as f: 
with open('input.txt', 'r') as f: 
    for line in f: 
        line = line.strip().split(" ")
        for count, value in enumerate(line): 
            line[count] = ''.join(sorted(value))
        raw.append(line)

# set(a).intersection(set(b))
def FindProfile(map, input): 
    output = [0] * 4
    output[0] = len(set(input).intersection(set(map[1])))
    output[1] = len(set(input).intersection(set(map[4])))
    output[2] = len(set(input).intersection(set(map[7])))
    output[3] = len(set(input).intersection(set(map[8])))
    return output

def Decode(map, input): 
    output = ""
    for i in input: 
        output += str(map.index(i))
    return str(output)

# pattern = raw[0][:10]
# input = raw[0][11:]
counter = [0] * 10 
answer = []
for line in raw: 
    map = [""] * 10 
    # for i in line[11:]:
    pattern = line[:10]
    for i in pattern:  
        if len(i) == 2: 
            # counter[1] += 1
            map[1] = i
            continue
        elif len(i) == 3: 
            # counter[7] += 1
            map[7] = i
            continue
        elif len(i) == 4: 
            # counter[4] += 1
            map[4] = i
            continue
        elif len(i) == 7: 
            # counter[8] += 1
            map[8] = i
            continue

    for i in pattern: 
        if i in map: continue 
        output = FindProfile(map, i)
        if output == [1,2,2,5]: map[2] = i
        elif output == [2,3,3,5]: map[3] = i
        elif output == [1,3,2,5]: map[5] = i
        elif output == [2,3,3,6]: map[0] = i
        elif output == [1,3,2,6]: map[6] = i
        elif output == [2,4,3,6]: map[9] = i
    
    # decode
    output_str = Decode(map, line[11:])
    answer.append(int(output_str))
    print("{}: {}".format(line[11:], output_str))

print("part2 answer = {}".format(sum(answer)))
# for count, value in enumerate(counter): 
#     print("{} --> {}".format(count, value))
# print("there are {} instances of digits that use a unique number of segments".\
#     format(sum(counter)))
print('end')
