# with open("sample.txt", 'r') as f: 
with open("input.txt", 'r') as f: 
    raw_lst = f.read().splitlines()
# raw_lst = list(map(int, raw_lst))
x = 0
y = 0
aim = 0
for i in raw_lst: 
    i = i.split()
    if i[0] == "forward": 
        x = x + int(i[1])
        y = y + aim * int(i[1]) 
    elif i[0] == "up": aim = aim - int(i[1])
    else: aim = aim + int(i[1])
    # print(i, x, y, aim)

print("a horizontal position of {} and a depth of {}. \n(Multiplying these together produces {}.)"\
    .format(x, y, x * y))
print(raw_lst)