with open("input.txt", "r") as file:
    text = file.readlines()

l1, l2 = [], []

for line in text :
    line = line.split("  ")
    l1.append(int(line[0]))
    l2.append(int(line[1]))

l1.sort()
l2.sort()

distance = 0
for i in range(len(l1)):
    distance += abs(l1[i] - l2[i])

print(distance)