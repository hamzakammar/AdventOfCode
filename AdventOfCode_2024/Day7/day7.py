f = open('Day7/Day7.txt', 'r')
code = f.read()

opList = code.split("\n")
for i in range(len(opList)):
    a = opList[i].split()
    #We need to do a combination of additions and multiplications to see if it works
f = open('Day7/Day7.txt', 'r')
code = f.read()

opList = code.split("\n")
for i in range(len(opList)):
    a = opList[i].split()
    
    def try_operations(numbers, target):
        def evaluate(nums, ops):
            result = nums[0]
            for i in range(len(ops)):
                if ops[i] == '+':
                    result += nums[i+1]
                else:
                    result *= nums[i+1]
            return result
            
        # Generate all possible combinations of + and * operations
        for ops in [''.join(p) for p in itertools.product('*+', repeat=len(numbers)-1)]:
            if evaluate(numbers, ops) == target:
                return True
        return False
    # + + + + +
    # * + + + +
    # * * + + +
    # * * * + + 
    # * * * * +
    # * * * * * 