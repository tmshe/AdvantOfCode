# with open("sample.txt", 'r') as f: 
with open("input.txt", 'r') as f: 
    raw_lst = f.read().splitlines()
raw_lst = list(map(int, raw_lst))

diff_lst = []
for count, value in enumerate(raw_lst): 
    try: 
        diff = sum(raw_lst[count+1:count+4]) - sum(raw_lst[count:count+3])
    except: 
        break 
    if diff <= 0: 
        continue 
    else:  
        diff_lst.append(diff)
print("there are {} measurements that are larger than the previous measurement.".format(len(diff_lst)))
print(raw_lst)