import re

with open('input.txt', 'r') as file:
    text = file.read()

# print(text)

pattern = re.compile(r'mul\([0-9]{1,3},[0-9]{1,3}\)')

matches = pattern.finditer(text)

result = 0

for m in matches:
    nums = ((m.group() [str(m.group()).index('(') + 1:len(str(m.group())) - 1:]).split(","))
    result += int(nums[0]) * int(nums[1])

print(result)