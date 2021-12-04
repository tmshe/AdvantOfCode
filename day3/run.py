
# with open("sample.txt", 'r') as f: 
with open("input.txt", 'r') as f: 
    raw_lst = f.read().splitlines()
# raw_lst = list(map(int, raw_lst))
total_bit = len(raw_lst[0])
# ===== part 1 ===== 
bit_ct = 0
common_bit = 0
gamma_rate = str()
epsilon_rate = str()
total_row = len(raw_lst)
sum = 0
while bit_ct < total_bit: 
    for i in raw_lst: 
        sum = sum + int(i[bit_ct])
    if sum > total_row / 2: common_bit = 1
    else: common_bit = 0
    gamma_rate = gamma_rate + str(common_bit)
    bit_ct = bit_ct + 1
    sum = 0
for i in gamma_rate: 
    if int(i) == 0: epsilon_rate = epsilon_rate + "1"
    else: epsilon_rate = epsilon_rate + "0"
print("Multiplying the gamma rate ({}) by the epsilon rate ({}) produces the power consumption, {}."\
    .format(int(gamma_rate, 2), int(epsilon_rate, 2), int(gamma_rate, 2) * int(epsilon_rate, 2)))

# ===== Part2 =====
def FindCommonBit(raw_lst, bit_ct): 
    sum = 0
    for i in raw_lst:
        sum = sum + int(i[bit_ct])
    if sum > len(raw_lst) / 2: common_bit = 1
    elif sum < len(raw_lst) / 2: common_bit = 0
    else: common_bit = 1
    return common_bit

o2_rate = raw_lst 
wip_lst = list()
bit_ct = 0
while bit_ct < total_bit:
    if len(o2_rate) == 1: break 
    common_bit = FindCommonBit(o2_rate, bit_ct)
    # print(bit_ct, common_bit)
    for value in o2_rate: 
        if value[bit_ct] == str(common_bit): 
            wip_lst.append(value)
    # print(wip_lst)
    o2_rate = wip_lst
    wip_lst = list() 
    bit_ct = bit_ct + 1
print("the oxygen generator rating is {}, or {} in decimal".format(o2_rate, int(o2_rate[0], 2)))

co2_rate = raw_lst 
wip_lst = list()
bit_ct = 0
while bit_ct < total_bit:
    if len(co2_rate) == 1: break 
    common_bit = FindCommonBit(co2_rate, bit_ct)
    # print(bit_ct, common_bit)
    for value in co2_rate: 
        if value[bit_ct] != str(common_bit): 
            wip_lst.append(value)
    # print(wip_lst)
    co2_rate = wip_lst
    wip_lst = list() 
    bit_ct = bit_ct + 1
print("the CO2 scrubber rating is {}, or {} in decimal.".format(co2_rate, int(co2_rate[0], 2)))

print("multiply the oxygen generator rating ({}) by the CO2 scrubber rating ({}) to get {}."\
    .format(int(o2_rate[0], 2), int(co2_rate[0], 2), int(o2_rate[0], 2) * int(co2_rate[0], 2)))
print('end')