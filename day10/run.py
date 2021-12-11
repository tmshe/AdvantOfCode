import statistics

raw = []
# with open('sample.txt','r') as f: 
with open('input.txt','r') as f: 
    for line in f: 
        line = list(line.strip())
        raw.append(line)

open_lst = ['(','[','{','<']
close_lst = [')',']','}','>']
expected_char_lst = []
illegal_char_lst = [] 
incomplete_lst = []

def FindandRemoveCompletePair(line): 
    wip = []
    for idx, value in enumerate(line): 
        if value in open_lst: 
            wip.append(value)
        if value in close_lst: 
            opposite = open_lst[close_lst.index(value)]
            if wip[- 1] == opposite: 
                wip.pop(-1)
                # print("pair_found: {}{}".format(opposite, value))
            else: 
                expected_char = wip[- 1]
                illegal_char = value 
                return expected_char, illegal_char,[]
    return 'x', 'x', wip

for line in raw: 
    expected_char, illegal_char, incomplete =  FindandRemoveCompletePair(line)  
    expected_char_lst.append(expected_char)    
    illegal_char_lst.append(illegal_char)
    incomplete_lst.append(incomplete)
    # print("expect {}, found {} instead".format(expected_char, illegal_char))

sum = 0 
keep_idx = []
for idx, char in enumerate(illegal_char_lst): 
    if char == ')': sum = sum + 3
    elif char == ']': sum = sum + 57
    elif char == '}': sum = sum + 1197
    elif char == '>': sum = sum + 25137
    else: keep_idx.append(idx)
print(sum)

total_score = []
point_dict = {'(':1, '[':2, '{':3, '<':4}
# ): 1 point.
# ]: 2 points.
# }: 3 points.
# >: 4 points.
for incomplete in incomplete_lst: 
    if len(incomplete) == 0: continue
    score = 0
    while len(incomplete) > 0: 
        char = incomplete.pop(-1)
        score = score * 5 + point_dict[char]
    total_score.append(score)
print("median total score = {}".format(statistics.median(total_score)))
print('end')
