alps = {}

for alp in input().lower():
    if alp in alps.keys():
        alps[alp] += 1
    else:
        alps[alp] = 1

max_cnt = max(alps.values())
final_alp = [k for k,v in alps.items() if v == max_cnt]

if len(final_alp) != 1:
    print('?')
else:
    print(final_alp[0].upper())