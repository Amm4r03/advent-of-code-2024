with open('input.txt', 'r') as file:
    text = file.readlines()

def diff_can_be_safe(nums: list[int]) -> bool:
    return all(1 <= abs(nums[j] - nums[j + 1]) <= 3 for j in range(len(nums) - 1))

def can_be_safe(nums: list[int]) -> bool:
    for i in range(len(nums)):
        res = nums[:i] + nums[i + 1:]
        # Check if res is strictly increasing or decreasing, and passes the difference check
        if (
            all(res[j] < res[j + 1] for j in range(len(res) - 1)) or
            all(res[j] > res[j + 1] for j in range(len(res) - 1))
        ):
            if diff_can_be_safe(res):  # Apply diff check to modified array
                return True
    return False

inp = []
for line in text:
    res = [int(x) for x in line.split(" ")]
    inp.append(res)

incdec = []

for rec in inp:
    print(f"current array: {rec} -> ", end="")
    if (
        (  # Condition 1: Already strictly increasing/decreasing and passes diff check
            (rec == sorted(rec) or rec == sorted(rec, reverse=True)) and 
            diff_can_be_safe(rec)
        ) or 
        can_be_safe(rec)  # Condition 2: Can be made strictly increasing/decreasing
    ):
        print("safe")
        incdec.append(rec)
    else:
        print("unsafe")

# Output results
# print(f"\nsafe arrays: {incdec}")
print(f"safe arrays count: {len(incdec)}")