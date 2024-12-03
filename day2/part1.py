with open('input.txt', 'r') as file:
    text = file.readlines()

inp = []
for line in text:
    res = [int(x) for x in line.split(" ")]
    inp.append(res)

incdec = []

for rec in inp:
    if rec == sorted(rec) or rec == sorted(rec, reverse=True):
        incdec.append(rec)


safe = 0
row_safe = 1

for r in incdec:
    # print(r)
    row_safe = 1
    for i in range(1, len(r)):
        # print(abs(r[i] - r[i - 1]))
        if abs(r[i] - r[i - 1]) < 1 or abs(r[i] - r[i - 1]) > 3:
            row_safe = 0
    if row_safe:
        safe += 1

print(safe, "rows")