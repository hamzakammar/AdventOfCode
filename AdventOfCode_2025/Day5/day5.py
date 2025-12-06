#Part 1
with open("input.txt") as file:
    lines = file.readlines()
    total = 0
    check = []
    for line in lines:
        line = line.strip()
        nums = line.split('-')
        if (len(nums) == 2):
            check.append((int(nums[0]), int(nums[1])))
        elif (nums[0] != ''):
            for i in range(len(check)):
                if (int(nums[0]) >= check[i][0] and int(nums[0]) <= check[i][1]):
                    total += 1
                    break
    print(total)

#Part 2
with open("input.txt") as file:
    lines = file.readlines()
    ranges = []
    for line in lines:
        line = line.strip()
        nums = line.split('-')
        if len(nums) == 2:
            ranges.append((int(nums[0]), int(nums[1])))
    
    # Sort ranges by start point
    ranges.sort()
    
    # Merge overlapping ranges
    merged = []
    for start, end in ranges:
        if merged and start <= merged[-1][1] + 1:
            # Overlapping or adjacent, merge them
            merged[-1] = (merged[-1][0], max(merged[-1][1], end))
        else:
            # Non-overlapping, add new range
            merged.append((start, end))
    
    # Count total numbers in merged ranges
    total = sum(end - start + 1 for start, end in merged)
    print(total)