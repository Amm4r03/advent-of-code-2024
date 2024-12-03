# get the input from the file
with open("input.txt", "r") as file:
    text = file.readlines()

l1, l2 = [], []

# store both lists in separate py lists
for line in text :
    line = line.split("  ")
    l1.append(int(line[0]))
    l2.append(int(line[1]))

# part 2 sol
# create dict for numbers in second list and multiply number in first list with second list freq

freq = {}
for num in l2:
    # print(num)
    # print(freq.keys())
    if num in freq.keys():
        freq[num] += 1
    else :
        freq[num] = 1

# print(freq)

sim = 0
for num in l1:
    try:
        sim += num * freq[num]
    except KeyError:
        pass

print(sim)