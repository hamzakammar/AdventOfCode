f = open('day2.txt', 'r')
code = f.read()

fulllist = code.split('\n')

def is_safe_sequence(seq):
    # Check if sequence is increasing or decreasing
    is_increasing = all(k < l for k, l in zip(seq, seq[1:]))
    is_decreasing = all(k > l for k, l in zip(seq, seq[1:]))
    
    # Check if differences are between 1 and 3
    valid_differences = all(1 <= abs(k - l) <= 3 for k, l in zip(seq, seq[1:]))
    
    return (is_increasing or is_decreasing) and valid_differences

safecount = 0
for line in fulllist:
    if not line:  # Skip empty lines
        continue
        
    report = [int(x) for x in line.split()]
    
    # Check if sequence is already safe
    if is_safe_sequence(report):
        safecount += 1
        continue
    
    # Try removing each number to see if sequence becomes safe
    for i in range(len(report)):
        test_sequence = report[:i] + report[i+1:]
        if is_safe_sequence(test_sequence):
            safecount += 1
            break

print("Safe reports:", safecount)